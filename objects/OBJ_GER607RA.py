from services.FA_ManipulacaoDeArquivos import ler_json
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from datetime import date
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.ConfiguracoesBase import Base, engine, session
#from OBJ_GER624RA import TGerTipoBloqueioRemoto

class Autonomia:
    def __init__(self, autonomia, usuario='TESTCOMPLETE', valor=''):
        self.tgerbloqueiousuario = TGerBloqueioUsuario(autonomia, usuario)
        
        if int(autonomia) == 2:
            if valor:
                self.tgerbloqueiousuario.vdamaxdesconto = valor
        
        # Em relações one-to-may, caso realizado um insert em apenas uma das tabelas, 
        #   não pode referenciar a outra tabela na fk.
        #self.tgertipobloqueioremoto = TGerTipoBloqueioRemoto()
        #self.tgerbloqueiousuario.fk_motivo = self.tgertipobloqueioremoto
    
class TGerBloqueioUsuario(Base):
    
    __tablename__ = 'TGERBLOQUEIOUSUARIO'
    
    empresa = Column(String(2), primary_key=True, nullable=False)
    usuario = Column(String(15), primary_key=True, nullable=False)
    motivo = Column(Integer, ForeignKey('TGERTIPOBLOQUEIOREMOTO.codigo'), primary_key=True, nullable=False)
    docmaxdesconto = Column(Numeric(15,2), default=0)
    docmaxjuro = Column(Numeric(15,2), default=0)
    docmaxmulta = Column(Numeric(15,2), default=0)
    vdamaxdesconto = Column(Numeric(15,2), default=0)
    docmaxjurocap = Column(Numeric(15,2), default=0)
    temautonomia = Column(String(1), default='n')
    permaxlimitecredito = Column(Numeric(15,2))
    percedicaopreco = Column(Numeric(12,6))
    percdescatacado = Column(Numeric(15,3))
    percmaxdescquitacaocheque = Column(Numeric(15,3))
    
    fk_motivo = relationship("TGerTipoBloqueioRemoto", foreign_keys='TGerBloqueioUsuario.motivo')
    
    def __init__(self, autonomia, usuario):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_GER607RA.json')
        
        self.empresa = dados[autonomia]['TGERBLOQUEIOUSUARIO']['empresa']
        self.usuario = usuario
        self.motivo = dados[autonomia]['TGERBLOQUEIOUSUARIO']['motivo']
        self.docmaxdesconto = dados[autonomia]['TGERBLOQUEIOUSUARIO']['docmaxdesconto']
        self.docmaxjuro = dados[autonomia]['TGERBLOQUEIOUSUARIO']['docmaxjuro']
        self.docmaxmulta = dados[autonomia]['TGERBLOQUEIOUSUARIO']['docmaxmulta']
        self.vdamaxdesconto = dados[autonomia]['TGERBLOQUEIOUSUARIO']['vdamaxdesconto']
        self.docmaxjurocap = dados[autonomia]['TGERBLOQUEIOUSUARIO']['docmaxjurocap']
        self.temautonomia = dados[autonomia]['TGERBLOQUEIOUSUARIO']['temautonomia']
        self.permaxlimitecredito = dados[autonomia]['TGERBLOQUEIOUSUARIO']['permaxlimitecredito']
        self.percedicaopreco = dados[autonomia]['TGERBLOQUEIOUSUARIO']['percedicaopreco']
        self.percdescatacado = dados[autonomia]['TGERBLOQUEIOUSUARIO']['percdescatacado']
        self.percmaxdescquitacaocheque = dados[autonomia]['TGERBLOQUEIOUSUARIO']['percmaxdescquitacaocheque']