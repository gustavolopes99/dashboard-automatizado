import time
from pywinauto.application import Application
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from decimal import Decimal

class ComponentesDashboard:
    def __init__(self, app):
        self.app = app
    
    @property
    def janela_principal(self):
        return self.app.top_window()
        
    @property
    def tela_dashboard(self):
        return self.janela_principal.child_window(title="DashBoard", found_index=0)
    
    def coletar_dados_html_retorno(self, nomearquivo):
        dsh001pa = self.app.window(title_re=".*DashBoard.*") # Ajuste o titulo da sua janela
        dsh001pa.right_click_input()
        time.sleep(0.5)
        
        dsh001pa.type_keys("{DOWN 10}{ENTER}") # Desce o cursor até 'Exibir código-fonte'
        time.sleep(5) # Espera o Bloco de Notas abrir
        
        notepad = Application(backend="win32").connect(class_name="Notepad")
        window_notepad = notepad.window(class_name="Notepad")
        html_capturado = window_notepad.Edit.window_text() # Leitura do conteúdo do HTML
        window_notepad.close()
        print('HTML lido')

        self.caminho_arquivo = os.path.abspath(nomearquivo)
        with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(html_capturado)
    
    def obter_valor_elemento(self, elementos):
        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument("--headless")
        driver = webdriver.Chrome(options=opcoes)

        driver.get(f"file:///{self.caminho_arquivo}")

        valores_extraidos = {}

        for valor, xpath in elementos.items():
            try:
                valor_elemento = driver.find_element(By.XPATH, xpath).text.strip()
                
                valores_extraidos[valor] = valor_elemento

            except Exception as e:
                print(f"falha {e}")
        
        driver.quit()

        return valores_extraidos
    
    def obter_linha_grid_cxaban(self):
        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument("--headless")
        driver = webdriver.Chrome(options=opcoes)

        driver.get(f"file:///{self.caminho_arquivo}")
        xpath_linhas = f'//*[@id="tbgwebchart"]/tbody/tr'

        linhas_da_tabela = driver.find_elements(By.XPATH, xpath_linhas)

        dados_extraidos = {}

        for linha in linhas_da_tabela:
            colunas = linha.find_elements(By.XPATH, "./td | ./th")
        
            if len(colunas) > 0:
                valor = colunas[2].get_attribute("textContent").strip()

                valores_da_linha = []

                for col in colunas[1:]:
                    texto_coluna = col.get_attribute("textContent").strip() or "-"
                    valores_da_linha.append(texto_coluna)
                
                dados_extraidos[valor] = valores_da_linha
        driver.quit()

        return dados_extraidos
    

    
    def obter_valores_grafico_financeiro(self):
        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument("--headless")
        driver = webdriver.Chrome(options=opcoes)

        driver.get(f"file:///{self.caminho_arquivo}")

        valores_grafico = []
        try:
            script_js = """
                        var instancias = Chart.instances;
                        for (var key in instancias) {
                            if (instancias[key].chart.canvas.id === 'greceber') {
                                return instancias[key].data.datasets[0].data;
                            }
                        }
                        return null;
                        """
            valores = driver.execute_script(script_js)

            if valores:
                valores_grafico = [str(Decimal(str(v)).quantize(Decimal('0.00'))).replace('.', ',') for v in valores]
        except Exception as e:
            print(f"Falha ao obter gráfico {e}")
        finally:
            driver.quit()
        return valores_grafico
    
    def obter_linha_grid_receber(self):
        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument("--headless")
        driver = webdriver.Chrome(options=opcoes)

        driver.get(f"file:///{self.caminho_arquivo}")
        xpath_linhas = f'//*[@id="tbgwebchart"]/tbody/tr'

        linhas_da_tabela = driver.find_elements(By.XPATH, xpath_linhas)

        total_capital = Decimal('0.00')
        total_juros = Decimal('0.00')
        total_multa = Decimal('0.00')
        total_geral = Decimal('0.00')

        for linha in linhas_da_tabela:
            colunas = linha.find_elements(By.XPATH, "./td")

            if len(colunas) > 0:
                texto_capital = colunas[8].get_attribute("textContent").strip()
                texto_juros = colunas[9].get_attribute("textContent").strip()
                texto_multa = colunas[10].get_attribute("textContent").strip()
                texto_geral = colunas[11].get_attribute("textContent").strip()

                valor_cap = Decimal(texto_capital.replace('.', '').replace(',', '.'))
                valor_jur = Decimal(texto_juros.replace('.', '').replace(',', '.'))
                valor_mul = Decimal(texto_multa.replace('.', '').replace(',', '.'))
                valor_ger = Decimal(texto_geral.replace('.', '').replace(',', '.'))

                total_capital += valor_cap
                total_juros += valor_jur
                total_multa += valor_mul
                total_geral += valor_ger
        
        driver.quit()

        return {
            "soma_capital": total_capital,
            "soma_juros": total_juros,
            "soma_multa": total_multa,
            "soma_geral": total_geral
        }
                