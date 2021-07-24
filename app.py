import fitz
import itertools
import pdb
import re
from flask import Flask, render_template, request, flash, url_for, make_response

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1000 * 1000
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
  return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/hello")
def hello_world():
  return "<p>Hello, World</p>"


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/processar_nota', methods=['POST'])
def process_note():
  files = request.files.getlist('files[]')
  if not all([file.filename == '' for file in files]):
    note_info = []
    for file in files:
      if file.filename == '' or not allowed_file(file.filename):
        flash('Inserir documentos no formato .pdf', 'error')
        return { 'redirect_url': url_for('index')}

      fitz_file = fitz.Document(stream=file.stream.read(), filetype=file.mimetype)
      note_info.extend(get_note_info(fitz_file))
      fitz_file.close()
      print(note_info)
    return {'stocks': note_info, 'message': 'Sucesso'}
  else:
    flash('Inserir documentos no formato .pdf', 'error')
  
  return { 'redirect_url': url_for('index') }, 422


def get_note_info(fitz_file):
  pages_number = fitz_file.page_count
  for page in range(0, pages_number):
    text_content = fitz_file[page].get_text()

    if 'easynvest' in text_content.lower():
        raw_stocks, date, cblc_taxes, b3_taxes, doc_no = get_easynvest_data(text_content)
        stocks = [sanitize_stock(stock) for stock in raw_stocks]
        broker = 'Easynvest'
    else:
        raw_stocks, date, cblc_taxes, b3_taxes, doc_no = get_clear_data(text_content)
        stocks = [sanitize_stock(stock) for stock in raw_stocks]
        broker = 'Clear'

    stocks_with_taxes = create_stock_with_taxes(stocks, cblc_taxes, b3_taxes)
    stocks_with_broker = create_stock_lines(stocks_with_taxes, date, broker, doc_no)
  return stocks_with_broker


def get_easynvest_data(text_content):
    number_regex = '[\d\.]+,*[\d]*'
    raw_stocks = re.findall(rf"BOVESPA\n(\w)\n(\w+)\n([a-zA-Z0-9_ ]+)\n?.*\n({number_regex})\n({number_regex})\n({number_regex})", text_content)
    date = re.search(r"Pregão\n(\d{2}/\d{2}/\d{2,4})", text_content).group(1)
    cblc_taxes = re.search(r"\nTaxa de Liquidação\n-*(\d+,\d+)\nTaxa de Registro\n-*(\d+,\d+)\n", text_content).groups()
    b3_taxes = re.search(r"Total Bolsa\n(-*\d+,\d+)\n", text_content).groups()
    document_number = re.search(r"Número da nota\n(\d+)\n", text_content).group(1)
    return raw_stocks, date, cblc_taxes, b3_taxes, document_number

def sanitize_stock(raw_stock):
    return {
        'operation': raw_stock[0],
        'market': raw_stock[1],
        'ticker': raw_stock[2].split()[0].rstrip('F'),
        'quantity': int(raw_stock[3]),
        'unit_cost': float(raw_stock[4].replace('.', '').replace(',', '.')),
        'total_cost_before_tax': float(raw_stock[5].replace('.', '').replace(',', '.'))
    }

def create_stock_with_taxes(stocks, *taxes):
    total_taxes = sum([abs(float(tax.replace(',', '.'))) for tax in itertools.chain(*taxes)])
    total_stocks = sum([stock['total_cost_before_tax'] for stock in stocks])
    for stock in stocks:
        stock['total_cost_after_tax'] = round(stock['total_cost_before_tax'] * (1 + total_taxes / total_stocks ), 2)
    return stocks

def create_stock_lines(stocks_with_taxes, date, broker, doc_no):
    return format_data(stocks_with_taxes, date, broker, doc_no)

def format_data(stocks_with_taxes, date, broker, doc_no):
    return [
        [
            date,
            s['ticker'],
            s['operation'],
            s['quantity'],
            s['unit_cost'],
            s['total_cost_after_tax'],
            broker,
            doc_no
        ] for s in stocks_with_taxes
    ]

def get_clear_data(text_content):
    raw_stocks = re.findall(r"BOVESPA\n(\w)[\s\n](\w+)\n([a-zA-Z0-9_ ]+)\n(\d+)\n(\d*,*\d*)\n(\d*,*\d)", text_content)
    date = re.search(r"pregão\n(\d{2}/\d{2}/\d{2,4})", text_content).group(1)
    cblc_taxes = re.search(r"(-*\d+,\d+)\nTaxa de liquidação\n\w\n(-*\d+,\d+)\nTaxa de Registro\n", text_content).groups()
    b3_taxes = re.search(r"(\d+,\d+)\nTotal Bovespa / Soma\n", text_content).groups()
    document_number = re.search(r"Nr\. nota\n(\d+)\n", text_content).group(1)
    return raw_stocks, date, cblc_taxes, b3_taxes, document_number
