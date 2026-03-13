from objects.OBJ_EST008CA import CondicaoPagamento
from services.ConfiguracoesBase import session, engine, Base

class GerenciadorCondicao:

    def __init__(self, context):
        self.context = context
        self.manipular_dados = ManipularDados()
        
    def cadastro_condicao(self):
        self.manipular_dados.cadastrar_condicao()

class ManipularDados:

    def cadastrar_condicao(self):
        dados = CondicaoPagamento(condicao_pagamento='CARTAO_001')
        session.add(dados.testcondpagvenda) # condicao 002
        session.commit()