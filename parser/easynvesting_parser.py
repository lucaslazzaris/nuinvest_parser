import re
from .base_parser import BaseParser

class EasynvestingParser(BaseParser):
  broker = 'Easynvesting'

  def get_data(self, text_content):
    number_regex = '[\d\.]+,*[\d]*'
    raw_stocks = re.findall(rf"BOVESPA\n(\w)\n(\w+)\n([a-zA-Z0-9_ ]+)\n?.*\n({number_regex})\n({number_regex})\n({number_regex})", text_content)
    date = re.search(r"Pregão\n(\d{2}/\d{2}/\d{2,4})", text_content).group(1)
    cblc_taxes = re.search(r"\nTaxa de Liquidação\n-*(\d+,\d+)\nTaxa de Registro\n-*(\d+,\d+)\n", text_content).groups()
    b3_taxes = re.search(r"Total Bolsa\n-*(\d+,\d+)\n", text_content).groups()
    document_number = re.search(r"Número da nota\n(\d+)\n", text_content).group(1)
    return raw_stocks, date, cblc_taxes, b3_taxes, document_number