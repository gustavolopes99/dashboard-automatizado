from pages.PO_CXA000CA import ComponentesCXA000CA

class GerenciadorCadastroCaixa:
    def __init__(self, context):
        self.context = context
        self.manipular_dados = ManipularDados()

    def teste_elementos(self):
        self.manipular_dados.testar_elementos()

class ManipularDados:
    def testar_elementos(self):
        self.cxa000ca = ComponentesCXA000CA(self.context.app)
        self.cxa000ca.eb_descricao.type_keys('TESTE CADASTRO{ENTER}', with_spaces=True)        
        self.cxa000ca.bt_confirmar.click()        
        self.cxa000ca.bt_editar        
        self.cxa000ca.eb_caixa.click_input()
        self.cxa000ca.eb_caixa.type_keys('02{ENTER}')        
        self.cxa000ca.eb_descricao.click_input()
        self.cxa000ca.eb_descricao.type_keys('{HOME}+{END}TESTE CADASTRO OK{ENTER}', with_spaces=True)        
        self.cxa000ca.ch_ativo.uncheck()        
        self.cxa000ca.bt_confirmar.click()        
        self.cxa000ca.bt_excluir        
        self.cxa000ca.eb_caixa.click_input()
        self.cxa000ca.eb_caixa.type_keys('02{ENTER}')        
        self.cxa000ca.bt_confirmar.click()