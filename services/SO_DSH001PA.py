from pages.PO_DSH001PA import ComponentesDashboard
import time
import pyautogui
import sys
sys.path.append('..\\..\\ecoTestCompleteBDD\\ProjetoEco\\PackagesPython')
from decimal import Decimal
class GerenciadorDashboard:
    def __init__(self, context):
        self.context = context
        self.manipular_tela = ManipularTela(self.context.app)
        self.manipular_dados = ManipularDados(self.context.app)
    
    def maximizar_tela(self):
        self.manipular_tela.maximizar_tela()
    
    def acesso_detalhes_caixabanco(self):
        self.manipular_tela.clicar_total_caixabanco()
    
    def acesso_detalhes_receber(self):
        self.manipular_tela.clicar_total_receber()

    def acesso_detalhes_pagar(self):
        self.manipular_tela.clicar_total_pagar()
    
    def acesso_detalhes_cartao(self):
        self.manipular_tela.clicar_total_cartao()

    def validar_totalcxaban(self, valor_total):
        self.manipular_dados.obter_totais_visaogeral()
        self.manipular_dados.validar_totalbancxa(valor_total)
    
    def validar_detalhes_cxaban(self, total_caixa, nosso_saldo_banco, totalgeral):
        self.manipular_dados.obter_detalhes_total_cxaban()
        self.manipular_dados.validar_detalhes_total_cxaban(total_caixa, nosso_saldo_banco, totalgeral)
    
    def validar_tabela_cxabanco(self, tabela_bancos_esperados):
        self.manipular_dados.validar_tabela_cxaban(tabela_bancos_esperados)
    
    def validar_tabela_areceber(self):
        self.manipular_dados.obter_detalhes_total_receber()
        self.manipular_dados.validar_tabela_receber()
    
    def validar_totalcontasreceber(self, valor_total):
        self.manipular_dados.obter_totais_visaogeral()
        self.manipular_dados.validar_totalreceber(valor_total)
    
    def validar_totalcontasreceber(self, valor_total):
        self.manipular_dados.obter_totais_visaogeral()
    
    def verificar_grafico_financeiro(self, vencidos, venc_hoje, a_vencer):
        self.manipular_dados.obter_totais_visaogeral()
        self.manipular_dados.verifica_grafico_financeiro(vencidos, venc_hoje, a_vencer)

class ManipularDados:
    def __init__(self, app):
        self.app = app
        self.dsh001pa = ComponentesDashboard(app)

    def obter_totais_visaogeral(self):
        xpaths = {
            "totalcaixabanco": "/html/body/div/div[2]/div[4]/div/a[2]", # Xpath do Total: R$ 1.922,30
            "totalcontasreceber": "/html/body/div/div[2]/div[1]/div/a[2]", # Xpath do Total: R$ 6.750,25
            "totalcontaspagar": "/html/body/div/div[2]/div[2]/div/a[2]", # Xpath do Total: R$ 0,00
            "totalcartao": "/html/body/div/div[2]/div[3]/div/a[2]" # Xpath to Total: R$ 0,00
        }
        self.dsh001pa.coletar_dados_html_retorno('visaogeral.html') # Gravação do html
        self.valores = self.dsh001pa.obter_valor_elemento(xpaths)
        valor_bruto_totalcxaban = self.valores["totalcaixabanco"]
        valor_bruto_totalcontasreceber = self.valores["totalcontasreceber"]
        valor_bruto_totalcontaspagar = self.valores["totalcontaspagar"]
        valor_bruto_totalcartao = self.valores["totalcartao"]
        self.valor_totalcxaban = valor_bruto_totalcxaban.replace("Total: R$ ", "").strip()
        self.valor_totalcontasreceber = valor_bruto_totalcontasreceber.replace("Total: R$ ", "").strip()
        self.valor_totalcontaspagar = valor_bruto_totalcontaspagar.replace("Total: R$ ", "").strip()
        self.valor_totalcartao = valor_bruto_totalcartao.replace("Total: R$ ", "").strip()

    def validar_totalbancxa(self, valor_total):
        assert valor_total == self.valor_totalcxaban, f'O valor total de Banco / Caixa esperado é {valor_total}, o valor obtido foi {self.valor_totalcxaban}'
    
    def obter_detalhes_total_cxaban(self):
        xpaths = {
            "total_caixa": "/html/body/div/div[2]/div/div/div[1]/div[1]/div[2]",
            "total_banco": "/html/body/div/div[2]/div/div/div[1]/div[2]/div[2]",
            "total_geral": "/html/body/div/div[2]/div/div/div[1]/div[3]/div[2]"
                }
        self.dsh001pa.coletar_dados_html_retorno('detalhes_cxaban.html')
        self.totais_detalhes_cxaban = self.dsh001pa.obter_valor_elemento(xpaths)
    
    def obter_detalhes_total_receber(self):
        xpaths = {
            "total_capital": "/html/body/div/div[2]/div/div/div[1]/div[1]/div[2]",
            "total_juros": "/html/body/div/div[2]/div/div/div[1]/div[2]/div[2]",
            "total_multas": "/html/body/div/div[2]/div/div/div[1]/div[3]/div[2]",
            "valor_total": "/html/body/div/div[2]/div/div/div[1]/div[4]/div[2]"
                }
        self.dsh001pa.coletar_dados_html_retorno('detalhes_receber.html')
        self.totais_detalhes_receber = self.dsh001pa.obter_valor_elemento(xpaths)
        
    def obter_graficos_contaspagar(self):
        pass
    def obter_graficos_cartao(self):
        pass
    def obter_graficos_caixabanco(self):
        pass
    
    def validar_detalhes_total_cxaban(self, total_caixa_esp, nossosaldobanco_esp, totalgeral_esp):        
        assert self.totais_detalhes_cxaban["total_caixa"] == total_caixa_esp, f"Total Caixa esperado {total_caixa_esp}"
        assert self.totais_detalhes_cxaban["total_banco"] == nossosaldobanco_esp, f"Nosso saldo hoje - Banco esperado {nossosaldobanco_esp}"
        assert self.totais_detalhes_cxaban["total_geral"] == totalgeral_esp, f"Total"
    
    def validar_tabela_cxaban(self, tabela_bancos_esperados):
        gd_tela = self.dsh001pa.obter_linha_grid_cxaban()

            # Dados da FEATURE
        for linha_esperada in tabela_bancos_esperados:
            descricao = linha_esperada["descricao"].strip()
            nosso_saldoesp = linha_esperada["nosso_saldo"].strip()
            saldo_bancoesp = linha_esperada["saldo_banco"].strip()
            saldo_geralesp = linha_esperada["saldo_geral"].strip()
            valordh_esp = linha_esperada["saldo_dinheiro"].strip()
            valorch_esp = linha_esperada["saldo_cheque"].strip()
            saldo_caixaesp = linha_esperada["saldo_caixa"].strip()

            assert descricao in gd_tela, f"A conta '{descricao}' não foi encontrada!"

            gd_valor = gd_tela[descricao]
            
            # Dados do GRID
            nosso_saldo = gd_valor[4]
            saldo_banco = gd_valor[5]
            saldo_geral = gd_valor[6]
            dinheiro = gd_valor[7]
            cheque = gd_valor[8]
            caixa = gd_valor[9]

            assert nosso_saldoesp == nosso_saldo, f"{descricao} 'Nosso saldo' esperado {nosso_saldoesp} Informado {nosso_saldo}"
            assert saldo_bancoesp == saldo_banco, f"{descricao} 'Saldo do banco' esperado {saldo_bancoesp} Informado {saldo_banco}"
            assert saldo_geralesp == saldo_geral, f"{descricao} 'Saldo geral' esperado {saldo_geralesp} Informado {saldo_geral}"
            assert valordh_esp == dinheiro, f"{descricao} 'Valor dinheiro' esperado {valordh_esp} Informado {dinheiro}"
            assert valorch_esp == cheque, f"{descricao} 'Valor cheque'esperado {valorch_esp} Informado {cheque}"
            assert saldo_caixaesp == caixa, f"{descricao} 'Saldo caixa' esperado {saldo_caixaesp} Informado {caixa}"
    
    def validar_totalreceber(self, valor_total):
        assert valor_total == self.valor_totalcontasreceber, f'O valor total de Contas a receber esperado é {valor_total}, o valor obtido foi {self.valor_totalcontasreceber}'
    
    def validar_tabela_receber(self):
        gd_tela = self.dsh001pa.obter_linha_grid_receber()

        soma_capital = str(gd_tela['soma_capital']).replace('.', ',')
        soma_juros = str(gd_tela['soma_juros']).replace('.', ',')
        soma_multa = str(gd_tela['soma_multa']).replace('.', ',')
        soma_geral = str(gd_tela['soma_geral']).replace('.', ',')

        total_capital = self.totais_detalhes_receber['total_capital'].replace('R$', '').replace('.', '').strip()
        total_juros = self.totais_detalhes_receber['total_juros'].replace('R$', '').replace('.', '').strip()
        total_multas = self.totais_detalhes_receber['total_multas'].replace('R$', '').replace('.', '').strip()
        valor_total = self.totais_detalhes_receber['valor_total'].replace('R$', '').replace('.', '').strip()

        assert total_capital == soma_capital, "'Valor Capital' não é o mesmo valor da somatória do grid. "
        assert total_juros == soma_juros, "'Valor Juros' não é o mesmo valor da somatória do grid. "
        assert total_multas == soma_multa, "'Valor Multa' não é o mesmo valor da somatória do grid. "
        assert valor_total == soma_geral, "'Valor Total' não é o mesmo valor da somatória do grid. "


    def verifica_grafico_financeiro(self, vencidos, venc_hoje, a_vencer):
        dados = self.dsh001pa.obter_valores_grafico_financeiro()
        assert vencidos == dados[0], f"O valor de 'Vencidos' esperado é {vencidos}, o valor obtido foi {dados[0]}"
        assert venc_hoje == dados[1], f"O valor de 'Venc. hoje' esperado é {venc_hoje}, o valor obtido foi {dados[1]}"
        assert a_vencer == dados[2], f"O valor 'A Vencer' esperado é {a_vencer}, o valor obtido foi {dados[2]}"

    def validar_totalpagar(self, valor_total):
        pass

    def validar_totalcartao(self, valor_total):
        pass

class ManipularTela:
    def __init__(self, app):
        self.app = app
        self.dsh001pa = ComponentesDashboard(self.app)
    
    def maximizar_tela(self):
        tela = self.dsh001pa.tela_dashboard
        tela.set_focus()
        tela.maximize()

    def clicar_total_caixabanco(self):
        pyautogui.moveTo(1659, 466, duration=0.5)
        pyautogui.click() # Clica em 'Total:' no quadro Caixa/Banco
        time.sleep(3)

    def clicar_total_receber(self):
        pyautogui.moveTo(245, 466, duration=0.5)
        pyautogui.click() # Clica em 'Total:' no quadro Contas a Receber
        time.sleep(3)
    
    def clicar_total_pagar(self):
        pyautogui.moveTo(716, 466, duration=0.5)
        pyautogui.click() # Clica em 'Total:' no quadro Contas a Pagar
        time.sleep(3)
    
    def clicar_total_cartao(self):
        pyautogui.moveTo(1198, 466, duration=0.5)
        pyautogui.click() # Clica em 'Total:' no quadro Cartão
        time.sleep(3)