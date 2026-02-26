from behave import given, when, then
from pywinauto.application import Application
from pywinauto import mouse
import time
from pages.FA_Acesso import AcessoEco
from services.SO_DSH001PA import GerenciadorDashboard
from services.SO_BAN004CA import GerenciadorMovimentos
from services.SO_CXA002CA import GerenciadorLancamentos

@given('que o sistema Eco está aberto e logado')
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

@when('clique no botão DRE')
def step_impl(context):
    time.sleep(1)
    gerenciador = GerenciadorDashboard(context)
    gerenciador.acessar_dashboard_tela()
    time.sleep(1)
    gerenciador.maximizar_tela()

@then('o valor total do Caixa / Banco deve ser R$ {valor_esperado}')
def step_impl(context, valor_esperado):
    gerenciador = GerenciadorDashboard(context)
    gerenciador.validar_saldo(valor_esperado)

@when('cadastre um movimento no valor de R$ {valor}')
def step_impl(context, valor):
    gerenciador = GerenciadorMovimentos(context)
    gerenciador.cadastro_movimento_tela(valor)

@when('cadastre um lançamento no valor de R$ {valor}')
def step_impl(context, valor):
    gerenciador = GerenciadorLancamentos(context)
    gerenciador.cadastro_lancamento_tela(valor)

@then('valide os detalhes do total de caixa/banco')
def step_impl(context):
    gerenciador = GerenciadorDashboard(context)
    gerenciador.validar_detalhes_cxaban()