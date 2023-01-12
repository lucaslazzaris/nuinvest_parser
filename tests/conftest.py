import os
import pytest
import types
from werkzeug.datastructures import FileStorage
from app import create_app
from parser.base_parser import BaseParser
from parser.clear_parser import ClearParser
from parser.easynvesting_parser import EasynvestingParser
from parser.btg_parser import BtgParser

@pytest.fixture
def client():
  app = create_app()

  with app.test_client() as client:
      yield client

@pytest.fixture
def clear_parser():
  return ClearParser(None)

@pytest.fixture
def btg_parser():
  return BtgParser(None)

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
          'Especificação do Título\nEspecificação do Título\nObservação\n' \
          'Observação\nQuantidade\nQuantidade\nPreço/Ajuste\nPreço/Ajuste\n' \
          'Valor/Ajuste\nValor/Ajuste D/C\nD/C\nBOVESPA\nC\nFRACIONARIO\n' \
          'ENEV3F ON NM\n12\n16,61\n199,32\nD\nBOVESPA\nC\nFRACIONARIO\n' \
          'MGLU3F ON NM\n10\n20,08\n200,80\nD\nResumo dos Negócios\n' \
          'Resumo dos Negócios\nDebêntures\n0,00\nVendas à vista\n0,00\n' \
          'Compras à vista\n400,12\nOpções - Compras\n0,00\nOpções - Vendas\n' \
          '0,00\nOperações a Termo\n0,00\nValor das Operações com Títulos' \
          ' Públicos (V. Nom.)\n0,00\nValor das Operações\nValor das' \
          ' Operações\n400,12\n400,12\nEspecificações Diversas\n' \
          'Especificações Diversas\nIRRF Day Trade: Base R$ 0,00 Projeção:' \
          ' R$ 0,00\nObservações (*)\nObservações (*)\n2 - Corretora ou ' \
          ' pessoa vinculada atuou na contra parte\n# - Negócio direto\n8 - ' \
          'Liquidação Institucional\nD - Day-Trade\nF - Cobertura\nB - ' \
          'Debêntures\nC - Clubes e Fundos de Ações\nA - Posição Futuro\nH -' \
          ' Home Broker\nX - Box\nP - Carteira Própria\nY - Desmanche de Box' \
          '\nL - Precatório\nT - Liquidação pelo Bruto\nI - POP\nResumo' \
          ' Financeiro\nResumo Financeiro\nClearing (CBLC)\nClearing (CBLC)' \
          '\nValor Líquido das Operações\n-400,12\nTaxa de Liquidação\n' \
          '-0,10\nTaxa de Registro\n0,00\nTotal Clearing (CBLC)\nTotal' \
          ' Clearing (CBLC)\n-400,22\n-400,22\nBolsa\nBolsa\nTaxa de Termo /' \
          ' Opções\n0,00\nTaxa A.N.A.\n0,00\nEmolumentos\n-0,02\nTotal Bolsa' \
          '\nTotal Bolsa\n-0,02\n-0,02\nCorretagem/Despesas\nCorretagem/' \
          'Despesas\nCorretagem\n0,00\nISS (SÃO PAULO)\n0,00\nI.R.R.F. s/' \
          ' operações. Base 0,00\n0,00\nOutras\n0,00\nTotal Corretagem/' \
          'Despesas\nTotal Corretagem/Despesas\n0,00\n0,00\nLíquido para \n' \
          'Líquido para 05/08/2021\n05/08/2021\n-400,24\n-400,24\nObservação:' \
          ' As operações a termo não são computadas no líquido da fatura.\n' \
          'Easynvest - Título Corretora de Valores SA\nEasynvest - Título' \
          ' Corretora de Valores SA\nCNPJ: 62.169.875/0001-79 | ' \
          'www.easynvest.com.br\nAv. Dr. Cardoso de Melo, 1608 - 14º Andar | ' \
          'Vila Olímpia\n04548-005. | São Paulo. | SP | BR\nTel: (11) 3841-' \
          '4515 | Fax: (11) 3841-4516 | easynvest@easynvest.com.br\nFolha\n1' \
          ' / 1\nNúmero da nota\n38173\nData Pregão\n03/08/2021\nNome do' \
          ' Cliente\nLUCAS CERCAL LAZZARIS\nCPF\n071.465.969-07\nCódigo do' \
          ' Cliente\n7851860\nEndereço\nRUA 303, 222 APTO 402\nCidade\n' \
          'ITAPEMA\nUF\nSC\nCEP\n88220-000\nOuvidoria Easynvest - Título C' \
          'orretora de Valores SA | ouvidoria@easynvest.com.br | 0800-7277784\n'


@pytest.fixture
def clear_pdf_text():
  return 'Negócios realizados\nQ Negociação\nC/V Tipo mercado\n' \
          'Prazo Especificação do título\nObs. (*) Quantidade\n' \
          'Preço / Ajuste\nValor Operação / Ajuste\nD/C\n1-BOVESPA\n' \
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
          '\n1\n98,98\n98,98\nC\nNOTA DE NEGOCIAÇÃO\nNr. nota\n14120770' \
          '\nFolha\n1\nData pregão\n09/08/2021\nCLEAR CORRETORA - GRUPO XP\n' \
          'Av. Presidente Juscelino Kubitschek - Torre Sul, 1909 - 29º ANDAR' \
          ' VILA OLIMPIA\n4543-907\nSAO PAULO - SP\nTel. 4003-6245   Fax:' \
          ' (55 ) -\nInternet: www.clear.com.br SAC: 0800-774-0404' \
          '\ne-mail: atendimento@clear.com.br\nC.N.P.J: 02.332.886/0011-78\n' \
          'Carta Patente:\nOuvidoria: Tel. 0800.774.0404\ne-mail ouvidoria:' \
          ' ouvidoria@clear.com.br\nCliente\n0273166\nLUCAS CERCAL LAZZARIS' \
          '\nRUA 303, 222 - APTO 402 MEIA PRAIA\nTel. (048) 99655-7422' \
          '\n88220-000 ITAPEMA - SC\nParticipante destino do repasse\n-' \
          '\nCliente\n0\nValor\n260\nBanco\n00001\nAgência\n8892143\n' \
          'Conta corrente\nAcionista\nAdministrador\n071.465.969-07\n' \
          'C.P.F./C.N.P.J/C.V.M./C.O.B.\nCódigo cliente\n308-5   0273166' \
          '\nAssessor\n0\nCustodiante\nC.I\nN\nComplemento nome\nP. Vinc\nN' \
          '\n0,00\n1.739,85\n0,00\n0,00\n0,00\n0,00\n0,00\n1.739,85\n' \
          'Resumo dos Negócios\nDebêntures\nVendas à vista\nCompras à vista\n' \
          'Opções - compras\nOpções - vendas\nOperações à termo\nValor das' \
          ' oper. c/ títulos públ. (v. nom.)\nValor das operações \n' \
          'Especificações diversas\nA coluna Q indica liquidação no Agente' \
          ' do Qualificado.\n(*) Observações\nA - Posição futuro\n' \
          'T - Liquidação pelo Bruto\n2 - Corretora ou pessoa vinculada atuou' \
          ' na contra parte.\nC - Clubes e fundos de Ações\nI - POP\n# ' \
          '- Negócio direto\nP - Carteira Própria\n8 - Liquidação ' \
          'Institucional\nH - Home Broker\nD - Day Trade\nX - Box\nF' \
          ' - Cobertura\nY - Desmanche de Box\nB - Debêntures\nL - Precatório' \
          '\n1.739,42\nTotal CBLC\nC\n1.739,85\nValor líquido das operações' \
          '\nC\n0,43\nTaxa de liquidação\nD\n0,00\nTaxa de Registro\nD\n0,08' \
          '\nTotal Bovespa / Soma\nD\n0,00\nTaxa de termo/opções\nD\n0,00' \
          '\nTaxa A.N.A.\nD\n0,08\nEmolumentos\nD\n \n0,00\nTotal Custos /' \
          ' Despesas\nD\n \n0,00\nTaxa Operacional\nD\n0,00\nExecução\n0,00' \
          '\nTaxa de Custódia\n0,00\nImpostos\n0,08\nI.R.R.F. s/ operações,' \
          ' base R$1.739,85\n0,00\nOutros\nD\n1.739,34\nLíquido para' \
          ' 11/08/2021\nC\nResumo Financeiro\nClearing\nBolsa\n' \
          'Custos Operacionais\nObservação: (1) As operações a termo não são' \
          ' computadas no líquido da fatura.\nCapitais e regiões' \
          ' metropolitanas: 4003-6245 Demais localidades: 0800-887-9107 SAC:' \
          ' 0800-774-0404 Ouvidoria: 0800-200-5550\n'

@pytest.fixture
def btg_pdf_text():
  return 'NOTA DE CORRETAGEM\n2954597\n Nr. nota\n1\n Folha\n11/01/2023\n ' \
          'Data pregão\nCarta Patente:\nAvenida Brigadeiro Faria Lima, ' \
          '3477 - 14º Andar ITAIM BIBI\nTel: (011) 3046 - 2100 / 3443 - 2100 ' \
          '- Fax (011) 3046 - 2001\nC.N.P.J: 43.815.158/0001-22\n04538-133\n' \
          'SÃO PAULO - SP\nBTG Pactual CTVM S.A.\nInternet: www.btgpactual.com' \
          '\nSAC: 0800-722-2827  Ouvidoria: Tel. 0800-722-0048\ne-mail: ' \
          'atendimento@btgpactualdigital.com\ne-mail ouvidoria: ' \
          'ouvidoria@btgpactualdigital.com\n Cliente\n004293984\n' \
          'C.P.F./C.N.P.J/C.V.M./C.O.B.\n071.465.969-07\n' \
          'LUCAS CERCAL LAZZARIS\nDOS CAMBUATAS, 584 - APTO 301 88053525' \
          ' FLORIANOPOLIS\nSANTA CATARINA\nTel. (48) 996557422\n ' \
          'Código cliente\n85-0 004293984\n Assessor\n Participante ' \
          'destino do repasse\n1026\n Cliente\n-\n Valor\n0\n Custodiante\n ' \
          'C.I\nN\n Banco\n Acionista\n Administrador\n Complemento nome' \
          '\n P.Vinc\nN\n Agência\n Conta Corrente\nNegócios realizados\n' \
          'Q Negociação\nC/V\nTipo Mercado\nPrazo\nEspecificação do título\n' \
          'Obs. (*)\nQuantidade\nPreço / Ajuste\nValor Operação / Ajuste\n' \
          'D/C\n1-BOVESPA\nV\nVISTA\nBPAN4\nPN\n100\n6,05\n605,00\nC' \
          '\n1-BOVESPA\nV\nVISTA\nCASH3\nON\n300\n1,21\n363,00\nC\n1-BOVESPA' \
          '\nV\nVISTA\nCASH3F\nON\n60\n1,20\n72,00\nC\n1-BOVESPA\nV\nVISTA\n' \
          'MGLU3\nON\n100\n3,07\n307,00\nC\n1-BOVESPA\nV\nVISTA\nMGLU3F\nON\n' \
          '15\n3,07\n46,05\nC\n1-BOVESPA\nV\nVISTA\nMLAS3F\nON\n45\n3,54\n' \
          '159,30\nC\n1-BOVESPA\nV\nVISTA\nPIBB11\n12\n196,25\n2.355,00\nC' \
          '\n1-BOVESPA\nV\nVISTA\nSHUL4\n200\n4,81\n962,00\nC\n' \
          'Resumo dos Negócios\nResumo Financeiro\nDebêntures\nClearing\n' \
          '0,00\n4.869,35\nVendas à vista\nCompras à vista\n0,00\n0,00\n' \
          'Opções - compras\nOpções - vendas\n0,00\n0,00\nOperações à termo\n' \
          'Valor das oper. c/ títulos públ. (v. nom.)\n0,00\n4.869,35\n' \
          'Valor das operações\nEspecificações diversas\nA coluna Q indica ' \
          'liquidação no Agente do Qualificado.\n4.869,35\nValor líquido das ' \
          'operações\nC\n1,21\nTaxa de liquidação\nD\n0,00\nTaxa de Registro' \
          '\n4.868,14\nTotal CBLC\nC\nBolsa\n0,00\nTaxa de termo/opções\n0,00' \
          '\nTaxa A.N.A.\n0,26\nEmolumentos\nD\n0,26\nTotal Bovespa / Soma\n' \
          'D\nCorretagem / Despesas\n36,00\nClearing\nD\n0,00\nExecução\n0,00' \
          '\nExecução casa\n3,83\nD\n0,23\n0,00\nI.R.R.F. s/ operações, base ' \
          'R$\n4.869,35\nOutras Bovespa\nTotal corretagem / Despesas\n39,83' \
          '\nD\nLíquido para 13/01/2023\nC\n4.828,05\n(*) Observações\nC - ' \
          'Clubes e fundos de\nI - POP\n2 - Corretora ou pessoa vinculada' \
          'atuou\nA - Posição futuro\nT - Liquidação pelo\nP - Carteira ' \
          'Própria\n# - Negócio direto\nH - Home Broker\n8 - Liquidação ' \
          'Institucional\nX - Box\nD - Day Trade\nY - Desmanche de Box\n' \
          'F - Cobertura\nL - Precatório\nB - Debêntures\nObservações:\n' \
          '(1) As operações a termo não são computadas no líquido da fatura.' \
          '\n(2) IR fonte à alíquota de 0,005% somente serão debitados em ' \
          'sua conta corrente, a\npartir do momento em que o IRRF for ' \
          'superior à R$ 1,00, no respectivo mês calendário.\n(3) Valor ' \
          'mínimo de IR fonte à alíquota de 0,005% não se aplica para FII e ' \
          'ETF.\n(4) IR fonte Day Trade de 1% não é descontado no líquido' \
          'da nota. O débito será feito\ndiretamente na conta do cliente.\n' \
          '(5) ISS*  contempla o ISS do município PIS / COFINS.\nISS* ' \
          '(SÃO PAULO - SP)\nCapitais e regiões metropolitanas: (011) ' \
          '4007-2511   Demais localidades: 0800-001-2511 SAC: 0800-772-2827  ' \
          ' Ouvidoria: 0800-722-0048\nwww.btgpactual.com\n'