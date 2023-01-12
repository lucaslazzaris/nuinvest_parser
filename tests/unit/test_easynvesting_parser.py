
class TestEasynvestingParser():
  def test_get_data(self, easyvesing_parser, easynvesting_pdf_text):
    stocks_data = easyvesing_parser.get_data(easynvesting_pdf_text)

    assert (
      [
        ('C', 'FRACIONARIO', 'ENEV3F ON NM', '12', '16,61', '199,32'),
        ('C', 'FRACIONARIO', 'MGLU3F ON NM', '10', '20,08', '200,80')
      ],
      '03/08/2021',
      ('0,10', '0,00'),
      ('0,02',),
      0,
      '38173'
    ) == stocks_data

