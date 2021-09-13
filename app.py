import os
from flask import Flask, render_template, send_from_directory, request, flash, url_for
from flask_cors import CORS #comment this on deployment
from parser.note_parser import NoteParser

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
  return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app(test_config=None):
  app = Flask(__name__, static_url_path='', static_folder='frontend/build')
  # I know I should hide this info,but I'll use it just to let the flash message works
  app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
  app.config['MAX_CONTENT_LENGTH'] = 50 * 1000 * 1000
  CORS(app) #comment this on deployment

  if test_config is None:
    pass
    # app.config.from_pyfile("config.py", silent=True)
  else:
    app.config.update(test_config)

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
          flash('Inserir documentos no formato .pdf', 'danger')
          return { 'redirect_url': url_for('index')}, 422

        note_parser = NoteParser(file)
        note_info.extend(note_parser.get_note_info())
        note_parser.close_file()
      flash('Sucesso', 'success')
      return {'stocks': note_info, 'template': render_template('flash_message.html')}
    else:
      flash('Inserir documentos no formato .pdf', 'danger')
    
    return { 'redirect_url': url_for('index') }, 422

  @app.route('/sobre')
  def about():
    return render_template('about.html')
  
  return app

app = create_app()