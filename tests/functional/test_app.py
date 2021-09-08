import os
from werkzeug.datastructures import FileStorage
from app import create_app

class TestApp():
  def test_empty_test_config(self):
    app = create_app()
    response_class = app.test_client().get('/')
    assert response_class.status_code == 200

  def test_Home(self, client):
    response_class = client.get('/')
    
    assert b"Selecione os arquivos" in response_class.data
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
        'Easynvesting',
        '384268'
    ]] == response_json['stocks']
    assert "Sucesso" in response_json['template']

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

    assert  {'redirect_url': '/' } == response_json

  def test_no_pdf(self, client, empty_file):
    data = {'files[]': [empty_file]}

    response_class = client.post(
      '/processar_nota',
      data=data,
      content_type='multipart/form-data'
    )

    response_json = response_class.get_json()

    with client.session_transaction() as session:
      flash_message = dict(session['_flashes']).get('danger')

    assert 'Inserir documentos no formato .pdf' == flash_message
    assert  {'redirect_url': '/' } == response_json
    assert 422 == response_class.status_code


  def test_about(self, client):
    response_class = client.get('/sobre')

    assert b"Esse projeto tem como objetivo facilitar a" in response_class.data
    assert response_class.status_code == 200

