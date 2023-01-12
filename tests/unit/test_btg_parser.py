class TestBtgParser:

  def test_get_data(self,btg_pdf_text, btg_parser): 
    stocks_data = btg_parser.get_data(btg_pdf_text)

    assert (
      [
        ('V', 'VISTA', 'BPAN4', '100', '6,05', '605,00'),
        ('V', 'VISTA', 'CASH3', '300', '1,21', '363,00'),
        ('V', 'VISTA', 'CASH3F', '60', '1,20', '72,00'),
        ('V', 'VISTA', 'MGLU3', '100', '3,07', '307,00'),
        ('V', 'VISTA', 'MGLU3F', '15', '3,07', '46,05'),
        ('V', 'VISTA', 'MLAS3F', '45', '3,54', '159,30'),
        ('V', 'VISTA', 'PIBB11', '12', '196,25', '2.355,00'),
        ('V', 'VISTA', 'SHUL4', '200', '4,81', '962,00'),
      ],
      '11/01/2023',
      ('1,21', '0,00'),
      ('0,26', ),
      4.5,
      '2954597'
    ) == stocks_data
