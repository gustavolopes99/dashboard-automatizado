import sys
import os
sys.path.append(r'C:\fontes\sistemaEco\Certificacao\ecoTestCompleteBDD\ProjetoEco\Scripts_Banco')
from configparser import ConfigParser
import shutil
import inserirUsuarioPadrao
from services.ConfiguracoesBase import engine


def resetarBase():
    '''Executar somente para resetar a base quando utilizado o TESCOMPLETE IDE'''
    caminho_diretorio_banco = 'C:\\ecosis\\dados'
    caminho_diretorio_ini = 'C:\\ecosis\\windows'
    caminho_banco_novo = 'C:\\fontes\\sistemaEco\\BancoDados'
    caminho_scripts = 'C:\\fontes\\sistemaEco\\Certificacao\\ecoTestCompleteBDD\\ProjetoEco\\Scripts_Banco\\'

    os.system("taskkill /F /IM eco.exe >nul 2>&1")
    engine.dispose()

    # Exclui e copia ini novo
    arquivos_diretorio = os.listdir(caminho_diretorio_ini)
    for arquivo in arquivos_diretorio:
        if arquivo == 'eco.ini':
            os.remove(f'{caminho_diretorio_ini}\\eco.ini')
            shutil.copy(f'{caminho_scripts}\\eco.ini',
                        f'{caminho_diretorio_ini}\\eco.ini')
            break

    # Inclui o usuário TESTCOMPLETE na tag usuario do eco.ini
    config = ConfigParser()
    config.read(f'{caminho_diretorio_ini}\\eco.ini')
    parametro_existe = config.get('preferencias', 'usuario')

    config.set('preferencias', 'usuario', 'TESTCOMPLETE')
    with open(f'{caminho_diretorio_ini}\\eco.ini', 'w') as eco_ini:
        config.write(eco_ini)

    # Exclui e copia base nova, e inclui o usuario padrão utilizado TESTCOMPLETE
    arquivos_diretorio = os.listdir(caminho_diretorio_banco)
    for arquivo in arquivos_diretorio:
        if arquivo.upper() == 'ECODADOS.ECO':
            os.remove(f'{caminho_diretorio_banco}\\ECODADOS.ECO')
            shutil.copy(f'C:\\fontes\\sistemaEco\\BancoDados\\ECODADOS.ECO',
                        f'{caminho_diretorio_banco}\\ECODADOS.ECO')

            # Roda o EcoUpdate.
            # Manter na pasta ecosis\windows o executável da versão desejada com nome EcoUpdate
            os.system(r'C:\ecosis\windows\EcoUpdate.exe /autoupdate')
            inserirUsuarioPadrao.inserir_usuario(
                f'{caminho_scripts}\\liberar_modulos_usuario.sql')
            break