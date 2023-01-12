import fitz
from .parser_factory import ParserFactory

class NoteParser:
  def __init__(self, file):
    self.file = file
    self.fitz_file = fitz.Document(stream=file.stream.read(), filetype=file.mimetype)

  def get_note_info(self):
    parser_factory = ParserFactory(self.fitz_file)
    self.parser = parser_factory.fabricate()

    pages_number = self.fitz_file.page_count
    stocks_with_broker = []
    for page in range(0, pages_number):
      text_content = self.fitz_file[page].get_text()

      raw_stocks, date, cblc_taxes, b3_taxes, brokerage, doc_no = self.parser.get_data(text_content)
      broker = self.parser.broker

      stocks = [self.parser.sanitize_stock(stock) for stock in raw_stocks]
      stocks_with_taxes = self.parser.create_stock_with_taxes(stocks, brokerage, cblc_taxes, b3_taxes)
      stocks_with_broker.extend(self.parser.create_stock_lines(stocks_with_taxes, date, broker, doc_no))
    return stocks_with_broker

  def close_file(self):
    self.parser.close_file()