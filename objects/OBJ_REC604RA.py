from datetime import date
from services.ConfiguracoesBase import Base, engine, session
from sqlalchemy.sql import func, text
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (Column, String, Integer, Date, Numeric,
                        ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
import datetime
from services.FA_ManipulacaoDeArquivos import ler_json
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')

from OBJ_REC006CA import TRecParcela

class Baixa:
    def __init__(self):
        self.trecbaixa = TRecBaixa()
        self.trecformabaixa = TRecFormaBaixa()

        self.parcela = session.query(TRecParcela).order_by(TRecParcela.idtrecparcela.desc()).first() 
        self.trecbaixa.fk_empresa = self.parcela
        self.trecbaixa.fk_cliente = self.parcela
        self.trecbaixa.fk_tipo_documento = self.parcela
        self.trecbaixa.fk_documento = self.parcela
        self.trecbaixa.fk_parcela = self.parcela
        

class TRecBaixa(Base):
    __tablename__ = 'TRECBAIXA'

    empresa = Column(String(2), ForeignKey('TRECPARCELA.empresa'), primary_key=True, nullable=False)
    cliente = Column(String(5), ForeignKey('TRECPARCELA.cliente'), primary_key=True, nullable=False)
    tipo = Column(String(2), ForeignKey('TRECPARCELA.tipo'), primary_key=True, nullable=False)
    documento = Column(String(7), ForeignKey('TRECPARCELA.documento'), primary_key=True, nullable=False)
    parcela = Column(String(3), ForeignKey('TRECPARCELA.parcela'), primary_key=True, nullable=False)
    idbaixa = Column(Integer, primary_key=True, nullable=False)
    idsequencia = Column(Integer)
    datahorabaixa = Column(DateTime, nullable=False)
    datarecebimento = Column(Date, nullable=False)
    valor = Column(Numeric(18, 2), nullable=False)
    multa = Column(Numeric(18, 2), nullable=False)
    juros = Column(Numeric(18, 2), nullable=False)
    desconto = Column(Numeric(18, 2), nullable=False)
    multaoriginal = Column(Numeric(18, 2), nullable=False)
    jurosoriginal = Column(Numeric(18, 2), nullable=False)
    descontooriginal = Column(Numeric(18, 2), nullable=False)
    juroscaptalizado = Column(Numeric(18, 2), nullable=False)
    valorindice = Column(Numeric(10, 5), default=0)
    observacao = Column(String(40))
    empresadestino = Column(String(2))
    usuario = Column(String(20), nullable=False)
    obsbaixa = Column(String(100))
    usuarioliberacao = Column(String(15))
    jurosmultaacumulado = Column(Numeric(18, 2))
    origem = Column(String(3))
    datahoraalteracao = Column(DateTime, default='NOW')
    obs = Column(String(10000))

    fk_empresa = relationship('TRecParcela', foreign_keys='TRecBaixa.empresa')
    fk_cliente = relationship('TRecParcela', foreign_keys='TRecBaixa.cliente')
    fk_tipo_documento = relationship('TRecParcela', foreign_keys='TRecBaixa.tipo')
    fk_documento = relationship('TRecParcela', foreign_keys='TRecBaixa.documento')
    fk_parcela = relationship('TRecParcela', foreign_keys='TRecBaixa.parcela')

    def __init__(self, baixa='TRECBAIXA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC604RA.json')

        self.empresa = dados[baixa]['empresa']
        self.cliente = dados[baixa]['cliente']
        self.tipo = dados[baixa]['tipo']
        self.documento = dados[baixa]['documento']
        self.parcela = dados[baixa]['parcela']
        self.idbaixa = self._buscar_proximo_id_baixa()
        self.idsequencia = dados[baixa]['idsequencia']
        self.datahorabaixa = dados[baixa]['datahorabaixa']
        self.datarecebimento = dados[baixa]['datarecebimento']
        self.valor = dados[baixa]['valor']
        self.multa = dados[baixa]['multa']
        self.juros = dados[baixa]['juros']
        self.desconto = dados[baixa]['desconto']
        self.multaoriginal = dados[baixa]['multaoriginal']
        self.jurosoriginal = dados[baixa]['jurosoriginal']
        self.descontooriginal = dados[baixa]['descontooriginal']
        self.juroscaptalizado = dados[baixa]['juroscaptalizado']
        self.valorindice = dados[baixa]['valorindice']
        self.observacao = dados[baixa]['observacao']
        self.empresadestino = dados[baixa]['empresadestino']
        self.usuario = dados[baixa]['usuario']
        self.obsbaixa = dados[baixa]['obsbaixa']
        self.usuarioliberacao = dados[baixa]['usuarioliberacao']
        self.jurosmultaacumulado = dados[baixa]['jurosmultaacumulado']
        self.origem = dados[baixa]['origem']
        self.datahoraalteracao = dados[baixa]['datahoraalteracao']
        self.obs = dados[baixa]['obs']

    def _buscar_proximo_id_baixa(self):
        with engine.connect() as con:
            codigo = con.execute(text('SELECT MAX(CAST(IDBAIXA as integer)) FROM TRECBAIXA;')).fetchall()[0][0]

        if codigo:
            codigo += 1
        else:
            codigo = 1

        return codigo


class TRecFormaBaixa(Base):
    __tablename__ = 'TRECFORMABAIXA'

    gid = Column(BigInteger, primary_key=True, nullable=False)
    empresa = Column(String(2), nullable=False)
    idbaixa = Column(Integer, nullable=False)
    forma = Column(String(2), nullable=False)
    valor = Column(Numeric(18, 2), nullable=False)
    idcheque = Column(Integer)
    idconta = Column(String(2))
    idmovimento = Column(Integer)
    idcredito = Column(Integer)
    datamovimento = Column(Date)
    idsequencia = Column(Integer, nullable=False)
    datahoraalteracao = Column(DateTime, default='NOW')
    tbanmovimento_gid = Column(BigInteger)

    def __init__(self, formabaixa='TRECFORMABAIXA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC604RA.json')

        self.gid = self._buscar_proximo_gid_forma_baixa()
        self.empresa = dados[formabaixa]['empresa']
        self.idbaixa = dados[formabaixa]['idbaixa']
        self.forma = dados[formabaixa]['forma']
        self.valor = dados[formabaixa]['valor']
        self.idcheque = dados[formabaixa]['idcheque']
        self.idconta = dados[formabaixa]['idconta']
        self.idmovimento = dados[formabaixa]['idmovimento']
        self.idcredito = dados[formabaixa]['idcredito']
        self.datamovimento = dados[formabaixa]['datamovimento']
        self.idsequencia = dados[formabaixa]['idsequencia']
        self.datahoraalteracao = dados[formabaixa]['datahoraalteracao']
        self.tbanmovimento_gid = dados[formabaixa]['tbanmovimento_gid']

    def _buscar_proximo_gid_forma_baixa(self):
        with engine.connect() as con:
            codigo = con.execute(text('SELECT MAX(CAST(GID as integer)) FROM TRECFORMABAIXA;')).fetchall()[0][0]

        if codigo:
            codigo += 1
        else:
            codigo = 1

        return codigo


# class TRecAuditoria:
#     __tablename__ = "TRECAUDITORIA"

#     id = Column(Integer, nullable=False)
#     empresa = Column(String(2), nullable=False)
#     cliente = Column(String(5), nullable=False)
#     tipo = Column(String(2), nullable=False)
#     documento = Column(String(7), nullable=False)
#     parcela = Column(String(3), nullable=False)
#     idsequencia = Column(Integer)
#     data = Column(Date, default='Today')
#     hora = Column(Time, default='Now')
#     historico = Column(String(60))
#     valorbaixa = Column(Numeric(15, 2))
#     valorcancelamento = Column(Numeric(15, 2))
#     usuario = Column(String(20))
#     origemalteracao = Column(String(20))

#     def __init__(self, auditoria='TRECAUDITORIA_BAIXA'):
#         dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC604RA.json')
#         funcoes_gerais = FuncoesGerais()
#         converter_dados = ConverterDados()

#         self.id = self._buscar_proximo_id_auditoria()
#         self.empresa = dados[auditoria]['empresa']
#         self.cliente = dados[auditoria]['cliente']
#         self.tipo = dados[auditoria]['tipo']
#         self.documento = dados[auditoria]['documento']
#         self.parcela = dados[auditoria]['parcela']
#         self.idsequencia = dados[auditoria]['idsequencia']
#         self.data = converter_dados.data_atual(dados[auditoria]['data'])
#         self.hora = converter_dados.hora_atual(dados[auditoria]['hora'])
#         self.historico = dados[auditoria]['historico']
#         self.valorbaixa = dados[auditoria]['valorbaixa']
#         self.valorcancelamento = dados[auditoria]['valorcancelamento']
#         self.usuario = dados[auditoria]['usuario']
#         self.origemalteracao = dados[auditoria]['origemalteracao']

#     def _buscar_proximo_id_auditoria(self):
#         codigo = session.query(func.max(TRecAuditoria.id)).scalar()

#         codigo += 1 if codigo else 1

#         return codigo
