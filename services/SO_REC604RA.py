from objects.OBJ_REC604RA import Baixa
from services.ConfiguracoesBase import session, engine, Base

class GerenciadorTipoClientes:

    def __init__(self, context):
        self.context = context
        self.manipular_dados = ManipularDados()
    
    def registro_baixa(self):
        self.manipular_dados.registrar_baixa()

class ManipularDados:

    def registrar_baixa(self):
        dados = Baixa()