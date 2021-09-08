import itertools

class BaseParser:
  def __init__(self, fitz_file):
    self.fitz_file = fitz_file

  def close_file(self):
    self.fitz_file.close()

  def sanitize_stock(self, raw_stock):
      return {
          'operation': raw_stock[0],
          'market': raw_stock[1],
          'ticker': raw_stock[2].split()[0].rstrip('F'),
          'quantity': int(raw_stock[3]),
          'unit_cost': float(raw_stock[4].replace('.', '').replace(',', '.')),
          'total_cost_before_tax': float(raw_stock[5].replace('.', '').replace(',', '.'))
      }

  def create_stock_with_taxes(self, stocks, *taxes):
      total_taxes = sum([abs(float(tax.replace(',', '.'))) for tax in itertools.chain(*taxes)])
      total_stocks = sum([stock['total_cost_before_tax'] for stock in stocks])
      for stock in stocks:
          if stock['operation'].lower().startswith('c'):
            stock['total_cost_after_tax'] = round(stock['total_cost_before_tax'] * (1 + total_taxes / total_stocks ), 2)
          else:
            stock['total_cost_after_tax'] = round(stock['total_cost_before_tax'] * (1 - total_taxes / total_stocks ), 2)
      return stocks

  def create_stock_lines(self, stocks_with_taxes, date, broker, doc_no):
      return self.format_data(stocks_with_taxes, date, broker, doc_no)

  def format_data(self, stocks_with_taxes, date, broker, doc_no):
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
