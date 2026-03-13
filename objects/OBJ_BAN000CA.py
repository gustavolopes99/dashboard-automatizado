from services.FA_ManipulacaoDeArquivos import ler_json
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from datetime import date
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.ConfiguracoesBase import Base, engine, session

class Banco:
    def __init__(self):
        self.tbanbanco = TBanBanco()

class TBanBanco(Base):
    __tablename__ = 'TBANBANCO'

    gid = Column(BigInteger, nullable=False)
    numero = Column(String(3), primary_key=True, nullable=False)
    digito = Column(String(1), nullable=False)
    nome = Column(String(40), nullable=False)
    taxanegcheque = Column(Numeric(6,2), default=0)
    definicaocheque = Column(String(2))
    usuario = Column(String(15), nullable=False)
    idalteracao = Column(Integer, default=0, nullable=False)
    idenviopaf = Column(Integer, default=0, nullable=False)
    datahoraalteracao = Column(DateTime, default='NOW')

    def __init__(self, banco='TBANBANCO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_BAN000CA.json')

        self.gid = self._buscar_proximo_gid_banco()
        self.numero = self._buscar_proximo_numero_banco()
        self.digito = dados[banco]['digito']
        self.nome = dados[banco]['nome']
        self.taxanegcheque = dados[banco]['taxanegcheque']
        self.definicaocheque = dados[banco]['definicaocheque']
        self.usuario = dados[banco]['usuario']
        self.idalteracao = dados[banco]['idalteracao']
        self.idenviopaf = dados[banco]['idenviopaf']
        self.datahoraalteracao = dados[banco]['datahoraalteracao']

    def _buscar_proximo_gid_banco(self):
        codigo = session.query(func.max(TBanBanco.gid)).scalar()

        if codigo: 
            codigo = codigo + 1
        else:
            codigo = 1

        return codigo
        
    def _buscar_proximo_numero_banco(self):
        codigo = session.query(func.max(TBanBanco.numero)).scalar()

        if codigo: 
            codigo = int(codigo) + 1
        else:
            codigo = 1

        return str(codigo)