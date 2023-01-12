def cblc_taxes():
  return ['0,50', '0,01']

def b3_taxes():
  return ['0,32']

def date():
  return '20/06/2021'

def broker():
  return 'Easynvesting'

def doc_no():
  return '123527'

class TestBaseParser:

  def test_sanitize_stock(self, base_parser, raw_stock):
    stocks = base_parser.sanitize_stock(raw_stock)
    
    assert stocks['operation'] == 'C'
    assert stocks['market'] == 'FRACIONARIO'
    assert stocks['ticker'] == 'B3SA3'
    assert stocks['quantity'] == 37
    assert stocks['unit_cost'] == 16.31
    assert stocks['total_cost_before_tax'] == 603.47

  def test_create_stock_with_taxes(self, base_parser, stocks):
    stocks = base_parser.create_stock_with_taxes(stocks, 5.0, b3_taxes(), cblc_taxes())

    assert stocks[0]['total_cost_after_tax'] == 608.53
    assert stocks[1]['total_cost_after_tax'] == 3455.78
    assert stocks[2]['total_cost_after_tax'] == 4829.45

  def test_create_stock_lines(self, base_parser, stocks_with_taxes):
    formated_data = base_parser.create_stock_lines(
      stocks_with_taxes,
      date(),
      broker(),
      doc_no()
    )

    assert formated_data == [
      [
        '20/06/2021',
        'B3SA3',
        'C',
        37,
        16.31,
        603.53,
        'Easynvesting',
        '123527'
      ],
      [
        '20/06/2021',
        'VILG11',
        'V',
        30,
        115.47,
        3460.78,
        'Easynvesting',
        '123527'
      ],
      [
        '20/06/2021',
        'CPLE6',
        'C',
        800,
        6.03,
        4824.45,
        'Easynvesting',
        '123527'
      ]
    ]
