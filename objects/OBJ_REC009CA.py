import datetime
from services.FA_ManipulacaoDeArquivos import ler_json
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from services.ConfiguracoesBase import Base, engine, session
from datetime import date

class TipoCliente:
    def __init__(self):
        self.trectipocliente = TRecTipoCliente()

class TRecTipoCliente(Base):
    __tablename__ = 'TRECTIPOCLIENTE'

    gid = Column(BigInteger, primary_key=True, nullable=False)
    descr_tipo = Column(String(20))
    replicado = Column(SmallInteger, default=0, nullable=False)
    ativo = Column(SmallInteger, default=1)
    # cod_tipo = Column(String)

    def __init__(self, tipo_cliente='TRECTIPOCLIENTE'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC009CA.json')

        self.gid = self._buscar_proximo_codigo_tipo_cliente()
        self.descr_tipo = dados[tipo_cliente]['descr_tipo']
        self.replicado = dados[tipo_cliente]['replicado']
        self.ativo = dados[tipo_cliente]['ativo']
        # self.cod_tipo = dados[tipo_cliente]['cod_tipo']

    def _buscar_proximo_codigo_tipo_cliente(self):
        codigo = session.query(func.max(TRecTipoCliente.gid)).scalar()
                
        if codigo:
            codigo = codigo + 1
        else:
            codigo = 1
        return codigo