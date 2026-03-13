from objects.OBJ_PAG000CA import Fornecedor
from services.ConfiguracoesBase import session, engine, Base

class GerenciadorFornecedor:

    def __init__(self, context):
        self.context = context
        self.manipular_dados = ManipularDados()
    
    def cadastro_fornecedor(self):        
        self.manipular_dados.cadastrar_fornecedor()

class ManipularDados:

    def cadastrar_fornecedor(self):
        dados = Fornecedor()
        session.add(dados.tpagfornecedor)
        session.commit()