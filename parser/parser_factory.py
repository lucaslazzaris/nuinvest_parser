from .clear_parser import ClearParser
from .easynvesting_parser import EasynvestingParser

class ParserFactory:
  def __init__(self, fitz_file):
    self.fitz_file = fitz_file

  def fabricate(self):
    text_content = self.fitz_file[0].get_text()

    if 'easynvest' in text_content.lower():
      return EasynvestingParser(self.fitz_file)
    else:
      return ClearParser(self.fitz_file)

