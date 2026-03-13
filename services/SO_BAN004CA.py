from pages.PO_BAN004CA import ComponentesBAN004CA
from objects.OBJ_BAN004CA import Movimento
from services.ConfiguracoesBase import session, engine, Base

class GerenciadorMovimentos:
    def __init__(self, context):
        self.context = context
        self.manipular_dados = ManipularDados()
        if hasattr(context, 'app'):
            self.manipular_tela = ManipularTela(self.context.app)
        else:
            self.manipular_tela = None
    
    def cadastrar_movimento_tela(self, valor):
        self.manipular_tela.cadastro_movimento(valor)
    
    def cadastrar_movimento_banco_conciliado(self, conta, valor, operacao):
        self.manipular_dados.cadastro_movimento_banco_conciliado(conta, valor, operacao)

    def cadastrar_movimento_banco_nao_conciliado(self, conta, valor, operacao):
        self.manipular_dados.cadastro_movimento_banco_nao_conciliado(conta, valor, operacao)
class ManipularDados:
    
    def cadastro_movimento_banco_conciliado(self, conta, valor, operacao):
        dados = Movimento()
        dados.tbanmovimento.conciliacao = 'NOW' # data de hoje
        dados.tbanmovimento.conciliado = 'S'
        dados.tbanmovimento.conta = conta
        dados.tbanmovimento.valor = valor
        dados.tbanmovimento.valordisponivel = valor
        dados.tbanmovimento.operacao = operacao
        session.add(dados.tbanmovimento)
        session.commit()

    def cadastro_movimento_banco_nao_conciliado(self, conta, valor, operacao):
        dados = Movimento()
        dados.tbanmovimento.conta = conta
        dados.tbanmovimento.valor = valor
        dados.tbanmovimento.valordisponivel = valor
        dados.tbanmovimento.operacao = operacao
        session.add(dados.tbanmovimento)
        session.commit()    

class ManipularTela:
    def __init__(self, app):
        self.app = app
        self.ban004ca = ComponentesBAN004CA(self.app)
    
    def cadastrar_movimento(self, valor):
        tela_cadastro = self.ban004ca.tela_movimentos
        tela_cadastro.type_keys(f'01{{ENTER}}') # conta
        tela_cadastro.type_keys(f'04{{ENTER}}') # operacao
        tela_cadastro.type_keys(f'TESTE MOV DASHBOARD{{ENTER}}') # complemento
        tela_cadastro.type_keys(valor + '{ENTER}') # valor
        self.ban004ca.bt_confirmar.click()
        self.ban004ca.bt_cancelar.click()
        self.ban004ca.bt_sair.click()
