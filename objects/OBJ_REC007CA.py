import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.FA_ManipulacaoDeArquivos import ler_json
from sqlalchemy import (
    Column, String, Integer, SmallInteger
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from services.ConfiguracoesBase import Base, session, engine


class TiposDeDocumento:
    def __init__(self):
        self.trectipodocumento = TRecTipoDocumento()


class TRecTipoDocumento(Base):

    __tablename__ = 'TRECTIPODOCUMENTO'

    codigo = Column(String(2), primary_key=True, nullable=True)
    descricao = Column(String(20), nullable=True)
    abreviatura = Column(String(3), nullable=True)
    usuario = Column(String(15), nullable=True)
    codigoagrup = Column(String(4))
    codigocc = Column(String(14))
    cartao = Column(String(1))

    def __init__(self, tipo_documento='TIPO_DE_DOCUMENTO_000'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC007CA.json')

        self.codigo = self._buscar_proximo_codigo_tipo_documento()
        self.descricao = dados[tipo_documento]['TRECTIPODOCUMENTO']['descricao']
        self.abreviatura = dados[tipo_documento]['TRECTIPODOCUMENTO']['abreviatura']
        self.usuario = dados[tipo_documento]['TRECTIPODOCUMENTO']['usuario']
        self.codigoagrup = dados[tipo_documento]['TRECTIPODOCUMENTO']['codigoagrup']
        self.codigocc = dados[tipo_documento]['TRECTIPODOCUMENTO']['codigocc']
        self.cartao = dados[tipo_documento]['TRECTIPODOCUMENTO']['cartao']

    def _buscar_proximo_codigo_tipo_documento(self):
        codigo = session.query(func.max(TRecTipoDocumento.codigo)).scalar()

        if codigo:
            codigo = int(codigo)+1
        else:
            codigo = 1

        return str(codigo).zfill(2)
