import datetime
from services.FA_ManipulacaoDeArquivos import ler_json
import re
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from services.ConfiguracoesBase import Base, engine, session
from datetime import date

class Caixa:
    def __init__(self):
        self.tcxacaixa = TCxaCaixa()

class TCxaCaixa(Base):
    __tablename__ = 'TCXACAIXA'

    empresa = Column(String(2), primary_key=True, nullable=False)
    numero = Column(String(2), primary_key=True, nullable=False)
    descricao = Column(String(30), nullable=False)
    saldoatualdh = Column(Numeric(18,2), default=0, nullable=False)
    saldoatualch = Column(Numeric(18,2), default=0, nullable=False)
    datafechada = Column(Date)
    usuario = Column(String(15), nullable=False)
    ativo = Column(String(1))

    def __init__(self, caixa='TCXACAIXA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_CXA000CA.json')

        self.empresa = dados[caixa]['empresa']
        self.numero = self._buscar_proximo_numero_caixa()
        self.descricao = dados[caixa]['descricao']
        self.saldoatualdh = dados[caixa]['saldoatualdh']
        self.saldoatualch = dados[caixa]['saldoatualch']
        self.datafechada = dados[caixa]['datafechada']
        self.usuario = dados[caixa]['usuario']
        self.ativo = dados[caixa]['ativo']

    def _buscar_proximo_numero_caixa(self):
        code = ''
        with engine.connect() as con:
            code = con.execute(text('SELECT MAX(CAST(NUMERO as integer)) FROM TCXACAIXA;')).fetchall()
        
        if code[0][0]:
            codigo = int(code[0][0])
            codigo += 1
        else:
            codigo = 1
         
        return str(codigo).zfill(2)