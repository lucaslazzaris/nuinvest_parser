import re
from .base_parser import BaseParser

class ClearParser(BaseParser):
  broker = 'Clear'

  def get_data(self, text_content):
    number_regex = '[\d\.]+,*[\d]*'
    raw_stocks = re.findall(rf"BOVESPA\n(\w)[\s\n](\w+)\n([a-zA-Z0-9_ ]+)\n?.*\n({number_regex})\n({number_regex})\n({number_regex})", text_content)
    date = re.search(r"pregão\n(\d{2}/\d{2}/\d{2,4})", text_content).group(1)
    cblc_taxes = re.search(r"(-*\d+,\d+)\nTaxa de liquidação\n\w\n(-*\d+,\d+)\nTaxa de Registro\n", text_content).groups()
    b3_taxes_regex = re.search(r"(\d+,\d+)\nTotal Bovespa / Soma\n", text_content)
    b3_taxes = b3_taxes_regex.groups() if b3_taxes_regex else ['0']
    document_number_regex = re.search(r"Nr\. nota\n(\d+)\n", text_content)
    document_number = document_number_regex.group(1) if document_number_regex else 0
    return raw_stocks, date, cblc_taxes, b3_taxes, document_number