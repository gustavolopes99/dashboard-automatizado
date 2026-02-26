from pages.PO_CXA002CA import ComponentesCXA002CA

class GerenciadorLancamentos:
    def __init__(self, context):
        self.context = context
        self.manipular_tela = ManipularTela(self.context.app)
    
    def cadastro_lancamento_tela(self, valor):
        self.manipular_tela.cadastrar_lancamento(valor)
    
class ManipularTela:
    def __init__(self, app):
        self.app = app
        self.cxa002ca = ComponentesCXA002CA(self.app)
    
    def cadastrar_lancamento(self, valor):
        tela_cadastro = self.cxa002ca.tela_lancamentos
        tela_cadastro.type_keys(f'28{{ENTER}}') # histórico
        tela_cadastro.type_keys(valor + '{ENTER}') # valor
        self.cxa002ca.bt_confirmar.click()
        self.cxa002ca.bt_sair.click()