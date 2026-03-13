from behave import given, when, then
from pywinauto.application import Application
import time
from datetime import date
from pages.FA_Acesso import AcessoEco
from services.SO_DSH001PA import GerenciadorDashboard
from services.SO_BAN004CA import GerenciadorMovimentos
from services.SO_CXA002CA import GerenciadorLancamentos
from services.SO_REC000CA import GerenciadorClientes
from services.SO_EST008CA import GerenciadorCondicao
from services.SO_PAG000CA import GerenciadorFornecedor
from services.SO_REC006CA import GerenciadorDocumento
from services.CadastroConta import CadastroConta
from services.AplicacaoAutonomias import AplicacaoAutonomias
from services.ResetaBase import resetarBase
from decimal import Decimal

@given('zerar o banco de dados')
def step_impl(context):
    context.reset = resetarBase()

@given('cadastrar a conta')
def step_impl(context):
    context.conta = CadastroConta()
    
@given('autonomias liberadas')
def step_impl(context):
    context.autonomia = AplicacaoAutonomias()

@when('abrir o sistema eco e realize login')
def step_impl(context):
    context.app = Application(backend="win32").start(r"C:\ecosis\windows\eco.exe")
    time.sleep(10)
    servico = AcessoEco(context.app)
    servico.login_eco()
    
@when('acesse a tela {tela}')
def step_impl(context, tela):
    time.sleep(1)
    servico = AcessoEco(context.app)
    servico.acesso_tela(tela)

@then('o valor total do Caixa / Banco deve ser R$ {valor_esperado}')
def step_impl(context, valor_esperado):
    gerenciador = GerenciadorDashboard(context)
    gerenciador.validar_totalcxaban(valor_esperado)

@when('cadastre um lançamento no valor de R$ {valor}')
def step_impl(context, valor):
    gerenciador = GerenciadorLancamentos(context)
    gerenciador.cadastro_lancamento_tela(valor)

@when('eu clico no card Caixa / Banco')
def step_impl(context):
    context.gerenciador = GerenciadorDashboard(context)
    context.gerenciador.acesso_detalhes_caixabanco()

@then('valide os resumos superiores da tela de detalhes de caixa e banco:')
def step_impl(context):
    linha = context.table[0] 
    caixa_esp = linha['total_caixa']
    banco_esp = linha['total_banco']
    geral_esp = linha['total_geral']
    gerenciador: GerenciadorDashboard = context.gerenciador
    gerenciador.validar_detalhes_cxaban(caixa_esp, banco_esp, geral_esp)

@then('valide os seguintes saldos aparecem no grid:')
def step_impl(context):
    gerenciador: GerenciadorDashboard = context.gerenciador
    gerenciador.validar_tabela_cxabanco(context.table)

@given('que os seguintes lançamentos de caixa são injetados no banco de dados:')
def step_impl(context):
    context.lancamento = GerenciadorLancamentos(context)
    
    for linha in context.table:
        historico = linha['historico']
        valordh = float(linha['valordh'].replace(',', '.'))
        valorch = float(linha['valorch'].replace(',', '.'))
        
        context.lancamento.cadastro_lancamento_banco(historico, valordh, valorch)

@given('que os seguintes movimentos bancários são injetados no banco de dados:')
def step_impl(context):
    context.movimento = GerenciadorMovimentos(context)
    
    for linha in context.table:
        conta = linha['conta']
        valor = float(linha['valor'])
        operacao = linha['operacao']
        conciliado = linha['conciliado']
    
        if conciliado == 'S':
            context.movimento.cadastrar_movimento_banco_conciliado(conta, valor, operacao)
        else:
            context.movimento.cadastrar_movimento_banco_nao_conciliado(conta, valor, operacao)

@given('cliente cadastrado')
def step_impl(context):
    gerenciador = GerenciadorClientes(context)
    gerenciador.cadastro_cliente_pj()

@given('documento cadastrado')
def step_impl(context):
    gerenciador = GerenciadorDocumento(context)
    gerenciador.cadastro_documento()

@given('que os seguintes documentos a receber são injetados no banco de dados:')
def step_impl(context):
    context.documento = GerenciadorDocumento(context)
    for linha in context.table:
        valor = Decimal(linha['valor'].replace(',', '.'))
        qtdparc = linha['qtd_parc']
        if linha['emissao'] == 'hoje':
            dataemissao = date.today()
        elif linha['emissao'] == 'anopassado':
            hoje = date.today()
            dataemissao = hoje.replace(year=hoje.year - 1)
        elif linha['emissao'] == 'mesquevem':
            hoje = date.today()
            dataemissao = hoje.replace(month=hoje.month - 1)        
        context.documento.cadastro_documento(valor, qtdparc, dataemissao)

@then('o valor total do Contas a receber deve ser R$ {valor_esperado}')
def step_impl(context, valor_esperado):
    gerenciador = GerenciadorDashboard(context)
    gerenciador.validar_totalcontasreceber(valor_esperado)

@then('valide os graficos a receber:')
def step_impl(context):
    context.gerenciador = GerenciadorDashboard(context)
    for linha in context.table:
        vencidos = linha['vencidos']
        venc_hoje = linha['venc_hoje']
        a_vencer = linha['a_vencer']
        context.gerenciador.verificar_grafico_financeiro(vencidos, venc_hoje, a_vencer)

@when('eu clico no card Contas a receber')
def step_impl(context):
    context.gerenciador = GerenciadorDashboard(context)
    context.gerenciador.acesso_detalhes_receber()

@when('eu clico no card Contas a pagar')
def step_impl(context):
    context.gerenciador = GerenciadorDashboard(context)
    context.gerenciador.acesso_detalhes_pagar()

@when('eu clico no card Cartão')
def step_impl(context):
    context.gerenciador = GerenciadorDashboard(context)
    context.gerenciador.acesso_detalhes_cartao()

@then('os totalizadores superiores devem corresponder a soma das colunas da tabela')
def step_impl(context):
    gerenciador: GerenciadorDashboard = context.gerenciador
    gerenciador.validar_tabela_areceber()

@then('o valor total geral deve corresponder a soma do Capital, Juros e Multas')
def step_impl(context):
    pass