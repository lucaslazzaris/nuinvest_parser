import os
import pytest
import types
from werkzeug.datastructures import FileStorage
from app import create_app
from parser.base_parser import BaseParser
from parser.clear_parser import ClearParser
from parser.easynvesting_parser import EasynvestingParser

@pytest.fixture
def client():
  app = create_app()

  with app.test_client() as client:
      yield client

@pytest.fixture
def clear_parser():
  return ClearParser(None)

@pytest.fixture
def fitz_file_clear():
  fitz_page = types.SimpleNamespace()
  fitz_page.get_text = lambda: 'Clear'
  return [fitz_page]

@pytest.fixture
def fitz_file_easynvesting():
  fitz_page = types.SimpleNamespace()
  fitz_page.get_text = lambda: 'Easynvesting'
  return [fitz_page]

@pytest.fixture
def easynvesting_file():
  file_path = os.path.join('tests/assets/Invoice_384268.pdf')
    
  pdf_file = FileStorage(
    stream= open(file_path, "rb"),
    filename='Invoice_384268.pdf',
    content_type='application/pdf',
  )

  return pdf_file

@pytest.fixture
def empty_file():
  file_path = os.path.join('tests/assets/empty_file.txt')
    
  pdf_file = FileStorage(
    stream= open(file_path, "rb"),
    filename='empty_file.txt',
    content_type='text/plain',
  )

  return pdf_file

@pytest.fixture
def raw_stock():
  return [
    'C',
    'FRACIONARIO',
    'B3SA3F ON EDJ NM',
    '37',
    '16,31',
    '603,47'
  ]

@pytest.fixture
def base_parser():
  return BaseParser(None)

@pytest.fixture
def stocks():
  return [
    {
      'operation': 'C',
      'market': 'FRACIONARIO',
      'ticker': 'B3SA3',
      'quantity': 37,
      'unit_cost': 16.31,
      'total_cost_before_tax': 603.47
    },
    {
      'operation': 'V',
      'market': 'FRACIONARIO',
      'ticker': 'VILG11',
      'quantity': 30,
      'unit_cost': 115.47,
      'total_cost_before_tax': 3461.10
    },
    {
      'operation': 'C',
      'market': 'FRACIONARIO',
      'ticker': 'CPLE6',
      'quantity': 800,
      'unit_cost': 6.03,
      'total_cost_before_tax': 4824.00
    }
  ]

@pytest.fixture
def stocks_with_taxes(stocks):
  stocks_with_taxes = stocks.copy()
  stocks_with_taxes[0]['total_cost_after_tax'] = 603.53
  stocks_with_taxes[1]['total_cost_after_tax'] = 3460.78
  stocks_with_taxes[2]['total_cost_after_tax'] = 4824.45
  return stocks_with_taxes

@pytest.fixture
def easyvesing_parser():
  return EasynvestingParser(None)


@pytest.fixture
def easynvesting_pdf_text():
  return 'Mercado\nMercado\nC/V\nC/V\nTipo de Mercado\nTipo de Mercado\n' \
          'Especifica????o do T??tulo\nEspecifica????o do T??tulo\nObserva????o\n' \
          'Observa????o\nQuantidade\nQuantidade\nPre??o/Ajuste\nPre??o/Ajuste\n' \
          'Valor/Ajuste\nValor/Ajuste D/C\nD/C\nBOVESPA\nC\nFRACIONARIO\n' \
          'ENEV3F ON NM\n12\n16,61\n199,32\nD\nBOVESPA\nC\nFRACIONARIO\n' \
          'MGLU3F ON NM\n10\n20,08\n200,80\nD\nResumo dos Neg??cios\n' \
          'Resumo dos Neg??cios\nDeb??ntures\n0,00\nVendas ?? vista\n0,00\n' \
          'Compras ?? vista\n400,12\nOp????es - Compras\n0,00\nOp????es - Vendas\n' \
          '0,00\nOpera????es a Termo\n0,00\nValor das Opera????es com T??tulos' \
          ' P??blicos (V. Nom.)\n0,00\nValor das Opera????es\nValor das' \
          ' Opera????es\n400,12\n400,12\nEspecifica????es Diversas\n' \
          'Especifica????es Diversas\nIRRF Day Trade: Base R$ 0,00 Proje????o:' \
          ' R$ 0,00\nObserva????es (*)\nObserva????es (*)\n2 - Corretora ou ' \
          ' pessoa vinculada atuou na contra parte\n# - Neg??cio direto\n8 - ' \
          'Liquida????o Institucional\nD - Day-Trade\nF - Cobertura\nB - ' \
          'Deb??ntures\nC - Clubes e Fundos de A????es\nA - Posi????o Futuro\nH -' \
          ' Home Broker\nX - Box\nP - Carteira Pr??pria\nY - Desmanche de Box' \
          '\nL - Precat??rio\nT - Liquida????o pelo Bruto\nI - POP\nResumo' \
          ' Financeiro\nResumo Financeiro\nClearing (CBLC)\nClearing (CBLC)' \
          '\nValor L??quido das Opera????es\n-400,12\nTaxa de Liquida????o\n' \
          '-0,10\nTaxa de Registro\n0,00\nTotal Clearing (CBLC)\nTotal' \
          ' Clearing (CBLC)\n-400,22\n-400,22\nBolsa\nBolsa\nTaxa de Termo /' \
          ' Op????es\n0,00\nTaxa A.N.A.\n0,00\nEmolumentos\n-0,02\nTotal Bolsa' \
          '\nTotal Bolsa\n-0,02\n-0,02\nCorretagem/Despesas\nCorretagem/' \
          'Despesas\nCorretagem\n0,00\nISS (S??O PAULO)\n0,00\nI.R.R.F. s/' \
          ' opera????es. Base 0,00\n0,00\nOutras\n0,00\nTotal Corretagem/' \
          'Despesas\nTotal Corretagem/Despesas\n0,00\n0,00\nL??quido para \n' \
          'L??quido para 05/08/2021\n05/08/2021\n-400,24\n-400,24\nObserva????o:' \
          ' As opera????es a termo n??o s??o computadas no l??quido da fatura.\n' \
          'Easynvest - T??tulo Corretora de Valores SA\nEasynvest - T??tulo' \
          ' Corretora de Valores SA\nCNPJ: 62.169.875/0001-79 | ' \
          'www.easynvest.com.br\nAv. Dr. Cardoso de Melo, 1608 - 14?? Andar | ' \
          'Vila Ol??mpia\n04548-005. | S??o Paulo. | SP | BR\nTel: (11) 3841-' \
          '4515 | Fax: (11) 3841-4516 | easynvest@easynvest.com.br\nFolha\n1' \
          ' / 1\nN??mero da nota\n38173\nData Preg??o\n03/08/2021\nNome do' \
          ' Cliente\nLUCAS CERCAL LAZZARIS\nCPF\n071.465.969-07\nC??digo do' \
          ' Cliente\n7851860\nEndere??o\nRUA 303, 222 APTO 402\nCidade\n' \
          'ITAPEMA\nUF\nSC\nCEP\n88220-000\nOuvidoria Easynvest - T??tulo C' \
          'orretora de Valores SA | ouvidoria@easynvest.com.br | 0800-7277784\n'


@pytest.fixture
def clear_pdf_text():
  return 'Neg??cios realizados\nQ Negocia????o\nC/V Tipo mercado\n' \
          'Prazo Especifica????o do t??tulo\nObs. (*) Quantidade\n' \
          'Pre??o / Ajuste\nValor Opera????o / Ajuste\nD/C\n1-BOVESPA\n' \
          'V FRACIONARIO\nBANCO PAN          PN N1\n7\n20,67\n144,69\nC' \
          '\n1-BOVESPA\nV FRACIONARIO\nCOSAN          ON NM\n#\n8\n24,29' \
          '\n194,32\nC\n1-BOVESPA\nV FRACIONARIO\nENEVA          ON NM\n16' \
          '\n17,24\n275,84\nC\n1-BOVESPA\nV FRACIONARIO' \
          '\nGRUPO SBF          ON NM\n11\n34,82\n383,02\nC\n1-BOVESPA\n' \
          'V FRACIONARIO\nTELEF BRASIL          ON\n1\n42,21\n42,21\nC' \
          '\n1-BOVESPA\nV FRACIONARIO\nTELEF BRASIL          ON\n#\n2\n42,21' \
          '\n84,42\nC\n1-BOVESPA\nV FRACIONARIO\nVIAVAREJO          ON NM\n35' \
          '\n12,46\n436,10\nC\n1-BOVESPA\nV VISTA' \
          '\nFII RBRALPHA          RBRF11          CI\n#\n1\n80,27\n80,27\nC' \
          '\n1-BOVESPA\nV VISTA\nFII RBRHGRAD          RBRR11          CI ER' \
          '\n1\n98,98\n98,98\nC\nNOTA DE NEGOCIA????O\nNr. nota\n14120770' \
          '\nFolha\n1\nData preg??o\n09/08/2021\nCLEAR CORRETORA - GRUPO XP\n' \
          'Av. Presidente Juscelino Kubitschek - Torre Sul, 1909 - 29?? ANDAR' \
          ' VILA OLIMPIA\n4543-907\nSAO PAULO - SP\nTel. 4003-6245   Fax:' \
          ' (55 ) -\nInternet: www.clear.com.br SAC: 0800-774-0404' \
          '\ne-mail: atendimento@clear.com.br\nC.N.P.J: 02.332.886/0011-78\n' \
          'Carta Patente:\nOuvidoria: Tel. 0800.774.0404\ne-mail ouvidoria:' \
          ' ouvidoria@clear.com.br\nCliente\n0273166\nLUCAS CERCAL LAZZARIS' \
          '\nRUA 303, 222 - APTO 402 MEIA PRAIA\nTel. (048) 99655-7422' \
          '\n88220-000 ITAPEMA - SC\nParticipante destino do repasse\n-' \
          '\nCliente\n0\nValor\n260\nBanco\n00001\nAg??ncia\n8892143\n' \
          'Conta corrente\nAcionista\nAdministrador\n071.465.969-07\n' \
          'C.P.F./C.N.P.J/C.V.M./C.O.B.\nC??digo cliente\n308-5   0273166' \
          '\nAssessor\n0\nCustodiante\nC.I\nN\nComplemento nome\nP. Vinc\nN' \
          '\n0,00\n1.739,85\n0,00\n0,00\n0,00\n0,00\n0,00\n1.739,85\n' \
          'Resumo dos Neg??cios\nDeb??ntures\nVendas ?? vista\nCompras ?? vista\n' \
          'Op????es - compras\nOp????es - vendas\nOpera????es ?? termo\nValor das' \
          ' oper. c/ t??tulos p??bl. (v. nom.)\nValor das opera????es \n' \
          'Especifica????es diversas\nA coluna Q indica liquida????o no Agente' \
          ' do Qualificado.\n(*) Observa????es\nA - Posi????o futuro\n' \
          'T - Liquida????o pelo Bruto\n2 - Corretora ou pessoa vinculada atuou' \
          ' na contra parte.\nC - Clubes e fundos de A????es\nI - POP\n# ' \
          '- Neg??cio direto\nP - Carteira Pr??pria\n8 - Liquida????o ' \
          'Institucional\nH - Home Broker\nD - Day Trade\nX - Box\nF' \
          ' - Cobertura\nY - Desmanche de Box\nB - Deb??ntures\nL - Precat??rio' \
          '\n1.739,42\nTotal CBLC\nC\n1.739,85\nValor l??quido das opera????es' \
          '\nC\n0,43\nTaxa de liquida????o\nD\n0,00\nTaxa de Registro\nD\n0,08' \
          '\nTotal Bovespa / Soma\nD\n0,00\nTaxa de termo/op????es\nD\n0,00' \
          '\nTaxa A.N.A.\nD\n0,08\nEmolumentos\nD\n \n0,00\nTotal Custos /' \
          ' Despesas\nD\n \n0,00\nTaxa Operacional\nD\n0,00\nExecu????o\n0,00' \
          '\nTaxa de Cust??dia\n0,00\nImpostos\n0,08\nI.R.R.F. s/ opera????es,' \
          ' base R$1.739,85\n0,00\nOutros\nD\n1.739,34\nL??quido para' \
          ' 11/08/2021\nC\nResumo Financeiro\nClearing\nBolsa\n' \
          'Custos Operacionais\nObserva????o: (1) As opera????es a termo n??o s??o' \
          ' computadas no l??quido da fatura.\nCapitais e regi??es' \
          ' metropolitanas: 4003-6245 Demais localidades: 0800-887-9107 SAC:' \
          ' 0800-774-0404 Ouvidoria: 0800-200-5550\n'
