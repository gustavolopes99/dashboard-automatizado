import datetime
from services.FA_ManipulacaoDeArquivos import ler_json
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from services.ConfiguracoesBase import Base, engine, session
from datetime import date
from services.FA_Parametros import TPagParametro, TCxaParametro

class BaixaPagamento:
    def __init__(self):
        self.tpagbaixa = TPagBaixa()
        self.tpagformabaixa = TPagFormaBaixa()

class TPagBaixa(Base):
    __tablename__ = 'TPAGBAIXA'

    empresa = Column(String(2), nullable=False)
    fornecedor = Column(String(5), nullable=False)
    tipo = Column(String(2), nullable=False)
    documento = Column(String(9), nullable=False)
    parcela = Column(String(3), nullable=False)
    datahorabaixa = Column(DateTime)
    valor = Column(Numeric(18,2), nullable=False)
    juros = Column(Numeric(18,2), nullable=False)
    multa = Column(Numeric(18,2), nullable=False)
    desconto = Column(Numeric(18,2), nullable=False)
    jurosoriginal = Column(Numeric(18,2), nullable=False)
    multaoriginal = Column(Numeric(18,2), nullable=False)
    descontooriginal = Column(Numeric(18,2), nullable=False)
    usuario = Column(String(15))
    idpagamento = Column(Integer, primary_key=True, nullable=False)
    hora = Column(Time, default='NOW')
    data = Column(Date, default='TODAY')
    datapagamento = Column(Date, nullable=False)
    obsbaixa = Column(String(100))
    empresadestino = Column(String(2))
    valorpermuta = Column(Numeric(18,2), default=0)
    obs = Column(String(10000))

    def __init__(self, baixa='TPAGBAIXA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PAG601RA.json')

        self.empresa = dados[baixa]['empresa']
        self.fornecedor = dados[baixa]['fornecedor']
        self.tipo = dados[baixa]['tipo']
        self.documento = dados[baixa]['documento']
        self.parcela = dados[baixa]['parcela']
        self.datahorabaixa = dados[baixa]['datahorabaixa']
        self.valor = dados[baixa]['valor']
        self.juros = dados[baixa]['juros']
        self.multa = dados[baixa]['multa']
        self.desconto = dados[baixa]['desconto']
        self.jurosoriginal = dados[baixa]['jurosoriginal']
        self.multaoriginal = dados[baixa]['multaoriginal']
        self.descontooriginal = dados[baixa]['descontooriginal']
        self.usuario = dados[baixa]['usuario']
        self.idpagamento = self._buscar_novo_idpagamento()
        self.hora = dados[baixa]['hora']
        self.data = dados[baixa]['data']
        self.datapagamento = dados[baixa]['datapagamento']
        self.obsbaixa = dados[baixa]['obsbaixa']
        self.empresadestino = dados[baixa]['empresadestino']
        self.valorpermuta = dados[baixa]['valorpermuta']
        self.obs = dados[baixa]['obs']

    def _buscar_novo_idpagamento(self):
        codigo = session.query(func.max(TPagParametro.idpagamento)).scalar()

        if codigo: 
            codigo = codigo + 1
        else:
            codigo = 1

        return codigo

class TPagFormaBaixa(Base):

    __tablename__ = 'TPAGFORMABAIXA'

    empresa = Column(String(2), nullable=False)
    idpagamento = Column(Integer, primary_key=True, nullable=False)
    fornecedor = Column(String(5))
    data = Column(Date, default='NOW')
    hora = Column(Time, default='NOW')
    valordh = Column(Numeric(18,2))
    valorch = Column(Numeric(18,2))
    chqvalor = Column(Numeric(18,2))
    debvalor = Column(Numeric(18,2))
    usuario = Column(String(15), nullable=False)
    trocodinheiro = Column(Numeric(18,2))
    trococheque = Column(Numeric(18,2))
    credito = Column(Numeric(18,2))
    clientepermuta = Column(String(5))
    trococredito = Column(Numeric(18,2))

    def __init__(self, cancelamento_baixa='TPAGFORMABAIXA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\\MA_PAG601RA.json')

        self.empresa = dados[cancelamento_baixa]['empresa']
        self.idpagamento = self._buscar_proximo_idpagamento()
        self.fornecedor = dados[cancelamento_baixa]['fornecedor']
        self.data = dados[cancelamento_baixa]['data']
        self.hora = dados[cancelamento_baixa]['hora']
        self.valordh = dados[cancelamento_baixa]['valordh']
        self.valorch = dados[cancelamento_baixa]['valorch']
        self.chqvalor = dados[cancelamento_baixa]['chqvalor']
        self.debvalor = dados[cancelamento_baixa]['debvalor']
        self.usuario = dados[cancelamento_baixa]['usuario']
        self.trocodinheiro = dados[cancelamento_baixa]['trocodinheiro']
        self.trococheque = dados[cancelamento_baixa]['trococheque']
        self.credito = dados[cancelamento_baixa]['credito']
        self.clientepermuta = dados[cancelamento_baixa]['clientepermuta']
        self.trococredito = dados[cancelamento_baixa]['trococredito']

    def _buscar_proximo_idpagamento(self):
        codigo = session.query(func.max(TPagParametro.idpagamento)).first()

        if codigo[0]: 
            codigo = codigo[0]+1
        else:
            codigo = 1

        return codigo
