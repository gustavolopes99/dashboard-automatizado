from services.FA_ManipulacaoDeArquivos import ler_json
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from datetime import date
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.ConfiguracoesBase import Base, engine, session

class Agencia:
    def __init__(self, agencia='TBANAGENCIA'):
        self.tbanagencia = TBanAgencia(agencia)

class TBanAgencia(Base):
    
    __tablename__ = 'TBANAGENCIA'

    gid = Column(BigInteger, primary_key=True, nullable=False)
    banco = Column(String(3), primary_key=True, nullable=False)
    numero = Column(String(4), primary_key=True, nullable=False)
    digito = Column(String(2), nullable=False)
    nome = Column(String(30), nullable=False)
    endereco = Column(String(40))
    cidade = Column(String(4), nullable=False)
    telefone = Column(String(12))
    fax = Column(String(12))
    gerente = Column(String(20))
    usuario = Column(String(15), nullable=False)
    gid_banco = Column(BigInteger)
    cnpjagencia = Column(String(14))

    def __init__(self, agencia='TBANAGENCIA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_BAN001CA.json')
        #funcoes_gerais = FuncoesGerais()

        self.gid = self._buscar_proximo_gid_agencia()
        self.banco = dados[agencia]['banco']
        self.numero = self._buscar_proxima_agencia() if dados[agencia]['numero'] == '0000' else dados[agencia]['numero']
        self.digito = dados[agencia]['digito']
        self.nome = dados[agencia]['nome'] # + str(funcoes_gerais.iterador())
        self.endereco = dados[agencia]['endereco']
        self.cidade = dados[agencia]['cidade']
        self.telefone = dados[agencia]['telefone']
        self.fax = dados[agencia]['fax']
        self.gerente = dados[agencia]['gerente']
        self.usuario = dados[agencia]['usuario']
        self.gid_banco = dados[agencia]['gid_banco']
        self.cnpjagencia = dados[agencia]['cnpjagencia']

    def _buscar_proxima_agencia(self):
        code = ''
        with engine.connect() as con:
            code = con.execute(text('SELECT MAX(CAST(NUMERO as integer)) FROM TBANAGENCIA;')).fetchall()
            
        if code[0][0]:
            codigo = int(code[0][0])
            codigo += 1
        else:
            codigo = 1
         
        return str(codigo).zfill(4)

    def _buscar_proximo_gid_agencia(self):
        codigo = session.query(func.max(TBanAgencia.gid)).scalar()

        if codigo: 
            codigo = codigo + 1
        else:
            codigo = 1

        return codigo