from flask import Flask, send_from_directory, request, url_for
from parser.note_parser import NoteParser

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
  return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
  app = Flask(__name__, static_url_path='', static_folder='frontend/build')
  # I know I should hide this info,but I'll use it just to let the flash message works
  app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
  app.config['MAX_CONTENT_LENGTH'] = 50 * 1000 * 1000

  @app.route("/", defaults={'path':''})
  def serve(path):
      return send_from_directory(app.static_folder,'index.html')

  @app.route('/processar_nota', methods=['POST'])
  def process_note():
    files = request.files.getlist('files[]')
    if not all([file.filename == '' for file in files]):
      note_info = []
      for file in files:
        if file.filename == '' or not allowed_file(file.filename):
          return { 
            'redirect_url': url_for('serve'),
            'flash_message': {
              'content': 'Inserir documentos no formato .pdf',
              'class': 'danger'
            }
          }, 422

        note_parser = NoteParser(file)
        note_info.extend(note_parser.get_note_info())
        note_parser.close_file()
      return {'stocks': note_info, 'flash_message': {'content': 'Sucesso', 'class': 'success'}}
    return { 
      'redirect_url': url_for('serve'),
      'flash_message': {
        'content': 'Inserir documentos no formato .pdf',
        'class': 'danger'
      }
    }, 422
  
  return app

app = create_app()