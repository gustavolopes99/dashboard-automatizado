import os
import json
import shutil
import tempfile
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')

def ler_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo_json:
            dados = json.load(arquivo_json)
        return dados
    except BaseException as e:
        print(e)  
    
def gravar_arquivo_json(caminho_arquivo, dados):
    # Abre arquivo como temporário e carrega os dados do json aberto
    with open(caminho_arquivo, 'r', encoding='utf-8') as arq, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
        dados_json = json.load(arq)
        
        # Verifica se as chaves ja estão no arquivo, se estiver sobrescreve os dados da chave
        if list(dados.keys())[0] not in dados_json.keys():
            dados_json.update(dados)
        else:
            del dados_json[list(dados.keys())[0]]
            dados_json.update(dados)
        
        # Grava
        json.dump(dados_json, out, ensure_ascii=False, indent=4, separators=(',',':'))
        
    # se tudo deu certo, renomeia o arquivo temporário, substituindo o antigo
    shutil.move(out.name, caminho_arquivo)
    
def pesquisa_caminho_completo_arquivo(file):
    path = 'C:\\fontes\\'
    # path = 'C:\\gitlab-runner\\builds'
    for (root, dirs, files) in os.walk(path, topdown=True):
        if file in files:
            return root
