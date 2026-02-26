from pages.PO_BAN004CA import ComponentesBAN004CA
import time

class GerenciadorMovimentos:
    def __init__(self, context):
        self.context = context
        self.manipular_tela = ManipularTela(self.context.app)
    
    def cadastro_movimento_tela(self, valor):
        self.manipular_tela.cadastrar_movimento(valor)
    
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
