from pages.PO_DSH001PA import ComponentesDashboard
import time
from pywinauto.mouse import click
from pywinauto.keyboard import send_keys
from pywinauto import Application
import pyperclip

class GerenciadorDashboard:
    def __init__(self, context):
        self.context = context
        self.manipular_tela = ManipularTela(self.context.app)

    def validar_saldo(self, valor_saldo):
        self.manipular_tela.validar_saldo_banco(valor_saldo)
    
    def acessar_dashboard_tela(self):
        self.manipular_tela.clicar_botao_dre()
    
    def maximizar_tela(self):
        self.manipular_tela.maximizar_tela()
    
    def validar_detalhes_cxaban(self):
        self.manipular_tela.validar_detalhes_total_cxaban()

class ManipularTela:    
    def __init__(self, app):
        self.app = app
        self.dsh001pa = ComponentesDashboard(self.app)

    def clicar_botao_dre(self):
        tela = self.dsh001pa.tela_dre
        tela.set_focus()
        click(button='left', coords=(395, 800))
        tela.type_keys('%d')
    
    def maximizar_tela(self):
        tela = self.dsh001pa.tela_dashboard
        tela.set_focus()
        tela.maximize()

    def validar_saldo_banco(self, valor_esperado):
        dados_card = self.dsh001pa.obter_dados_caixa_banco()
        print(f"Dados capturados: {dados_card}")

        valor_capturado = dados_card.get("total")        
        
        assert valor_capturado == valor_esperado, f"❌ FAILED: Esperava R$ {valor_esperado}, mas o Total está R$ {valor_capturado}."
        print(f"✅ PASSED: Valor Total de {valor_esperado} confirmado!")

    def validar_apenas_caixa(self, valor_esperado):
        dados_card = self.dsh001pa.obter_dados_caixa_banco()
        assert dados_card.get("caixa") == valor_esperado
    
    def validar_detalhes_total_cxaban(self):
        self.dsh001pa.acessar_detalhes_caixa_banco()