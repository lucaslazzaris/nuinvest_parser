import re
from .base_parser import BaseParser

class BtgParser(BaseParser):
  broker = 'Btg'

  def get_data(self, text_content):
    number_regex = '[\d\.]+,*[\d]*'
    raw_stocks = re.findall(rf"BOVESPA\n(\w)\n(\w+)\n([a-zA-Z0-9_ ]+)\n?.*\n({number_regex})\n({number_regex})\n({number_regex})", text_content)
    date = re.search(r"Folha\n(\d{2}/\d{2}/\d{2,4})", text_content).group(1)
    cblc_taxes = re.search(r"-*(\d+,\d+)\nTaxa de liquidação\n\w\n-*(\d+,\d+)", text_content).groups()
    b3_taxes = re.search(r"-*(\d+,\d+)\nTotal Bovespa / Soma\n", text_content).groups()
    document_number = re.search(r"(\d+)\n Nr. nota\n", text_content).group(1)
    brokerage = 4.5
    return raw_stocks, date, cblc_taxes, b3_taxes, brokerage, document_number