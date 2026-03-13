from objects.OBJ_REC000CA import Cliente
from services.ConfiguracoesBase import session, engine, Base
from objects.OBJ_GER002CA import Cidade

class GerenciadorClientes:

    def __init__(self, context):
        self.context = context
        self.manipular_dados = ManipularDados()
    
    def cadastro_cliente_pj(self):
        self.manipular_dados.cadastrar_cliente_pj()

class ManipularDados:

    def cadastrar_cliente_pj(self):
        dados = Cliente(cliente='CLIENTE_PJ')
        session.add(dados.treccliente)
        session.add(dados.trecclientegeral)
        session.add(dados.trecpjuridica)
        session.commit()
