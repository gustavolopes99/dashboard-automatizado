from pages.PO_DSH001PA import ComponentesDashboard
import time
from pywinauto.mouse import click
from pywinauto.keyboard import send_keys
from pywinauto import Application
import pyperclip
import pyautogui

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
    
    def acesso_detalhes_caixabanco(self):
        self.manipular_tela.clicar_total_caixabanco()
    
    def validar_detalhes_cxaban(self, total_caixa, nosso_saldo_banco, totalgeral):
        self.manipular_tela.validar_detalhes_total_cxaban(total_caixa, nosso_saldo_banco, totalgeral)
    
    def validar_tabela_cxabanco(self, tabela_bancos_esperados):
        self.manipular_tela.validar_tabela_cxaban(tabela_bancos_esperados)

class ManipularTela:    
    def __init__(self, app):
        self.app = app
        self.dsh001pa = ComponentesDashboard(self.app)
        self.dados_capturados = None

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

    def clicar_total_caixabanco(self):
        pyautogui.moveTo(1659, 466, duration=0.5)
        pyautogui.click() # Clica em 'Total:' no quadro Caixa/Banco
        time.sleep(3)
        self.dados_capturados = self.dsh001pa.acessar_detalhes_caixa_banco()

    def validar_detalhes_total_cxaban(self, total_caixa, nossosaldobanco, totalgeral):
        dados = self.dsh001pa.acessar_detalhes_caixa_banco()
        print(f'\nDados capturados {dados}\n')

        assert dados["resumos"]["total_caixa"] == total_caixa, f"Erro no Total Caixa: {dados['resumos']['total_caixa']}"
        assert dados["resumos"]["nosso_saldo_banco"] == nossosaldobanco, f"Erro no Nosso Saldo Banco: {dados['resumos']['nosso_saldo_banco']}"
        assert dados["resumos"]["total_geral"] == totalgeral, f"Erro no Total Geral: {dados['resumos']['total_geral']}"
    
    def validar_tabela_cxaban(self, tabela_bancos_esperados):
        grid_da_tela = self.dados_capturados["grid"]

        for linha_esperada in tabela_bancos_esperados:
            nome_banco = linha_esperada["descricao"]
            saldo_banco = linha_esperada["saldo"]

            print(f"Buscando: {nome_banco} com saldo de {saldo_banco}...")

            registro_encontrado = any(nome_banco in linha_tela and saldo_banco in linha_tela for linha_tela in grid_da_tela)

            assert registro_encontrado, f"❌ FAILED: Não encontrei '{nome_banco}' com o saldo '{saldo_banco}' na tabela da tela."
            print(f"✅ {nome_banco} validado!")