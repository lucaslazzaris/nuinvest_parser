class TestClearParser:

  def test_get_data(self,clear_pdf_text, clear_parser): 
    stocks_data = clear_parser.get_data(clear_pdf_text)

    assert (
      [
        ('V', 'FRACIONARIO', 'BANCO PAN          PN N1', '7', '20,67', '144,69'),
        ('V', 'FRACIONARIO', 'COSAN          ON NM', '8', '24,29', '194,32'),
        ('V', 'FRACIONARIO', 'ENEVA          ON NM', '16', '17,24', '275,84'),
        ('V', 'FRACIONARIO', 'GRUPO SBF          ON NM', '11', '34,82', '383,02'),
        ('V', 'FRACIONARIO', 'TELEF BRASIL          ON', '1', '42,21', '42,21'),
        ('V', 'FRACIONARIO', 'TELEF BRASIL          ON', '2', '42,21', '84,42'),
        ('V', 'FRACIONARIO', 'VIAVAREJO          ON NM', '35', '12,46', '436,10'),
        ('V', 'VISTA', 'FII RBRALPHA          RBRF11          CI', '1', '80,27', '80,27'),
        ('V', 'VISTA', 'FII RBRHGRAD          RBRR11          CI ER', '1', '98,98', '98,98')
      ],
      '09/08/2021',
      ('0,43', '0,00'),
      ('0,08', ),
      '14120770'
    ) == stocks_data
    