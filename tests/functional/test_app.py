import os
from werkzeug.datastructures import FileStorage
from app import create_app

class TestApp():
  def test_Home(self, client):
    response_class = client.get('/')
    
    assert response_class.status_code == 200

  def test_process_note(self, client, easynvesting_file):
    data = {'files[]': [easynvesting_file]}

    response_class = client.post(
      '/processar_nota',
      data=data,
      content_type='multipart/form-data'
    )

    response_json = response_class.get_json()
    assert [[
        '24/08/2021',
        'IVVB11',
        'C',
        4,
        259.66,
        1038.94,
        'Nu invest',
        '384268'
    ]] == response_json['stocks']
    assert {
      'content': 'Sucesso',
      'class': 'success'
    } == response_json['flash_message']

  def test_no_filename(self, client):
    file_path = os.path.join('tests/assets/Invoice_384268.pdf')
    
    pdf_file = FileStorage(
      stream= open(file_path, "rb"),
      filename='',
      content_type='application/pdf',
    )

    data = {'files[]': [pdf_file]}

    response_class = client.post(
      '/processar_nota',
      data=data,
      content_type='multipart/form-data'
    )

    response_json = response_class.get_json()

    assert {
      'content': 'Inserir documentos no formato .pdf',
      'class': 'danger'
    } == response_json['flash_message']
    assert  '/' == response_json['redirect_url']
    assert 422 == response_class.status_code

  def test_no_pdf(self, client, empty_file):
    data = {'files[]': [empty_file]}

    response_class = client.post(
      '/processar_nota',
      data=data,
      content_type='multipart/form-data'
    )

    response_json = response_class.get_json()

    assert {
      'content': 'Inserir documentos no formato .pdf',
      'class': 'danger'
    } == response_json['flash_message']
    assert  '/' == response_json['redirect_url']
    assert 422 == response_class.status_code
