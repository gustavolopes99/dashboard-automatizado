import pyperclip
import time
import pyautogui
import re

class ComponentesDashboard:
    def __init__(self, app):
        self.app = app
    
    @property
    def janela_principal(self):
        return self.app.top_window()
    
    @property
    def tela_dre(self):
        return self.app.top_window()
    
    @property
    def botao_dre(self):
        return self.tela_dre.child_window(title="DRE")
        
    @property
    def tela_dashboard(self):
        return self.janela_principal.child_window(title="DashBoard", found_index=0)
    
    def extrair_texto_bruto(self):
        tela = self.tela_dashboard
        tela.set_focus()
        time.sleep(1)

        pyperclip.copy('')

        largura_tela, altura_tela = pyautogui.size()
        pyautogui.click(x=largura_tela/2, y=altura_tela/2)
        time.sleep(0.5)

        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        
        return pyperclip.paste()
    
    def obter_dados_caixa_banco(self):
        texto_bruto = self.extrair_texto_bruto()

        linhas = texto_bruto.splitlines() # Separar o texto gigante em uma lista
        
        linhas = [linha.strip() for linha in linhas if linha.strip() != ""] # Limpar espaços em branco e remover linhas vazias
        
        dados_mapeados = {
            "caixa": None,
            "banco": None,
            "total": None
        }

        try: 
            index_card = linhas.index("Caixa / Banco") # Encontra em qual linha (índice) está o título do Card
            
            dados_mapeados["caixa"] = linhas[index_card + 1]
            dados_mapeados["banco"] = linhas[index_card + 3]
            # Procura a linha que começa com "Total:" logo após o título do card
            for i in range(index_card, index_card + 5):
                if linhas[i].startswith("Total:"):
                    padrao_dinheiro = r'\d{1,3}(?:\.\d{3})*,\d{2}'
                    resultado = re.search(padrao_dinheiro, linhas[i])

                    if resultado:
                        valor_corrigido = resultado.group(0)
                        dados_mapeados["total"] = valor_corrigido
                    else:
                        dados_mapeados["total"] = '0,00'
                    break

        except ValueError:
            print("Erro: O card 'Caixa / Banco' não foi encontrado no texto copiado.")
            
        return dados_mapeados
    
    def acessar_detalhes_caixa_banco(self):
        texto_detalhado = self.extrair_texto_bruto()
        linhas = texto_detalhado.splitlines()
        linhas = [linha.strip() for linha in linhas if linha.strip() != ""]

        dados_detalhados = {
            "resumos": {},
            "grid": []
        }

        try:
            idx_caixa = linhas.index("Total Caixa")
            dados_detalhados["resumos"]["total_caixa"] = linhas[idx_caixa + 1]
            idx_banco = linhas.index("Nosso saldo hoje - Banco") # Nâo conciliado
            dados_detalhados["resumos"]["total_caixa"] = linhas[idx_banco + 1]
            idx_total = linhas.index("Total", idx_banco) # Procura palavra "Total" depois do saldo do banco
            dados_detalhados["resumos"]["total_geral"] = linhas[idx_total + 1]
            idx_inicio_tabela = linhas.index("Saldo caixa ▲▼") + 1

            idx_fim_tabela = 0
            for i, linha in enumerate(linhas):
                if linha.startswith("Mostrando de"):
                    idx_fim_tabela = i
                    break

            if idx_fim_tabela > 0:
                dados_detalhados["grid"] = linhas[idx_inicio_tabela:idx_fim_tabela]

        except ValueError as e:
            print(f"Erro ao encontrar os elementos na tela detalhada: {e}")
        return dados_detalhados