import os
import sys
from pages.PO_CXA002CA import ComponentesCXA002CA
from objects.OBJ_CXA002CA import Lancamentos
from services.ConfiguracoesBase import session, engine, Base

class GerenciadorLancamentos:
    def __init__(self, context):
        self.context = context
        self.manipular_dados = ManipularDados()
        if hasattr(context, 'app'):
            self.manipular_tela = ManipularTela(self.context.app)
        else:
            self.manipular_tela = None
    
    def cadastro_lancamento_tela(self, valor):
        self.manipular_tela.cadastrar_lancamento(valor)

    def cadastro_lancamento_banco(self, historico, valordh, valorch):
        self.manipular_dados.insercao_lancamento_banco(historico, valordh, valorch)

class ManipularDados:

    def insercao_lancamento_banco(self, historico, valordh, valorch):
        dados = Lancamentos()
        dados.tcxalancamento.valordh = valordh
        dados.tcxalancamento.valorch = valorch
        dados.tcxalancamento.historico = historico
        session.add(dados.tcxalancamento)
        session.commit()

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