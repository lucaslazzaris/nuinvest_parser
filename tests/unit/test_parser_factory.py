from parser.parser_factory import ParserFactory
from parser.easynvesting_parser import EasynvestingParser
from parser.clear_parser import ClearParser

class TestParserFactory():
  def test_easynvest_fabrication(self, fitz_file_easynvesting):
    parser = ParserFactory(fitz_file_easynvesting).fabricate()

    assert type(parser) == EasynvestingParser
  
  def test_clear_fabrication(self, fitz_file_clear):
    parser = ParserFactory(fitz_file_clear).fabricate()

    assert type(parser) == ClearParser