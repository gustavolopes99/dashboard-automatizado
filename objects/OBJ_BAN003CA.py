from services.FA_ManipulacaoDeArquivos import ler_json
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from datetime import date
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.ConfiguracoesBase import Base, engine, session


class Operacao:
    def __init__(self, operacao='TBANOPERACAO'):
        self.tbanoperacao = TBanOperacao(operacao)

    
class TBanOperacao(Base):
    __tablename__ = 'TBANOPERACAO'

    codigo = Column(String(2), primary_key=True, nullable=False)
    descricao = Column(String(20), nullable=False)
    tipo = Column(String(1), nullable=False)
    possuicomplemento = Column(String(1), default='S')
    possuiconciliacao = Column(String(1), default='S')
    possuivencimento = Column(String(1), default='N')
    usuario = Column(String(15), nullable=False)
    codigoagrup = Column(String(4))
    codigocc = Column(String(14))
    operusacc = Column(String(1), default='N')
    gid = Column(BigInteger)
    ativo = Column(SmallInteger, default=1)

    def __init__(self, operacao='TBANOPERACAO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_BAN003CA.json')

        self.codigo = self._buscar_proximo_codigo_operacao()
        self.descricao = dados[operacao]['descricao']
        self.tipo = dados[operacao]['tipo']
        self.possuicomplemento = dados[operacao]['possuicomplemento']
        self.possuiconciliacao = dados[operacao]['possuiconciliacao']
        self.possuivencimento = dados[operacao]['possuivencimento']
        self.usuario = dados[operacao]['usuario']
        self.codigoagrup = dados[operacao]['codigoagrup']
        self.codigocc = dados[operacao]['codigocc']
        self.operusacc = dados[operacao]['operusacc']
        self.gid = self._buscar_proximo_gid_operacao()
        self.ativo = dados[operacao]['ativo']

    def _buscar_proximo_codigo_operacao(self):
        codigo = session.query(func.max(TBanOperacao.codigo)).scalar()

        if codigo: 
            codigo = int(codigo) + 1
        else:
            codigo = 1

        return str(codigo).zfill(2)

    def _buscar_proximo_gid_operacao(self):
        codigo = session.query(func.max(TBanOperacao.gid)).scalar()

        if codigo: 
            codigo = codigo + 1
        else:
            codigo = 1

        return codigo