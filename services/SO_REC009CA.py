from objects.OBJ_REC009CA import TipoCliente
from services.ConfiguracoesBase import session, engine, Base

class GerenciadorTipoClientes:

    def __init__(self, context):
        self.context = context
        self.manipular_dados = ManipularDados()
    
    def cadastro_tipo_cliente(self):
        self.manipular_dados.cadastrar_tipocliente()

class ManipularDados:

    def cadastrar_tipocliente(self):
        dados = TipoCliente()
        session.add(dados.trectipocliente)
        session.commit()