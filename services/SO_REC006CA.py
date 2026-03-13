from objects.OBJ_REC006CA import Documento
from services.ConfiguracoesBase import session, engine, Base

class GerenciadorDocumento:

    def __init__(self, context):
        self.context = context
        self.manipular_dados = ManipularDados()
    
    def cadastro_documento(self, valor, qtdparc, dataemissao):
        self.manipular_dados.cadastrar_documento(valor, qtdparc, dataemissao)

class ManipularDados:

    def cadastrar_documento(self, valor, qtdparc, dataemissao):
        dados = Documento(valor=valor, qtd_parc=qtdparc, emissao=dataemissao)
        session.add(dados.trecdocumento)
        for parcelas in dados.trecparcelas:
            session.add(parcelas)
        session.commit()