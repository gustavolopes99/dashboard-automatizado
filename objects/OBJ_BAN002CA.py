from services.FA_ManipulacaoDeArquivos import ler_json
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from datetime import date
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.ConfiguracoesBase import Base, engine, session

class Conta:
    def __init__(self, conta='TBANCONTA'):
        self.tbanconta = TBanConta(conta)
        
class TBanConta(Base):
    __tablename__ = 'TBANCONTA'
    
    gid = Column(BigInteger, nullable=False)
    empresa = Column(String(2), primary_key=True, nullable=False)
    codigo = Column(String(2), primary_key=True, nullable=False)
    banco = Column(String(3), ForeignKey('TBANAGENCIA.banco'), nullable=False)
    agencia = Column(String(4), ForeignKey('TBANAGENCIA.numero'), nullable=False)
    numero = Column(String(10), nullable=False)
    digito = Column(String(2), nullable=False)
    titular = Column(String(30), nullable=False)
    tipo = Column(String(1), nullable=False)
    limite = Column(Numeric(18,2), nullable=False)
    saldopendente = Column(Numeric(18,2), default=0, nullable=False)
    chequependente = Column(Numeric(18,2), default=0, nullable=False)
    saldoatual = Column(Numeric(18,2), default=0)
    usuario = Column(String(15), nullable=False)
    usarcc = Column(String(1), default='S')
    fluxocaixa = Column(String(1), default='S')
    usafavorecido = Column(String(1), default='S')
    saldoatualbanco = Column(Numeric(18,2), default=0)
    ativo = Column(String(1))
    tipopessoacedente = Column(String(1))
    cpfcnpjcedente = Column(String(14))
    bancocorrespondente = Column(String(3))
    agenciacorrespondente = Column(String(4))
    digitoagenciacorrespondente = Column(String(2))
    contacorrentecorrespondente = Column(String(10))
    digcontacorrentecorrespondente = Column(String(1))
    gid_agencia = Column(BigInteger, ForeignKey('TBANAGENCIA.gid'))
    contapadrao = Column(SmallInteger)
    
    fk_banco = relationship('TBanAgencia', foreign_keys='TBanConta.banco')
    fk_agencia = relationship('TBanAgencia', foreign_keys='TBanConta.agencia')
    fk_gid_agencia = relationship('TBanAgencia', foreign_keys='TBanConta.gid_agencia')
    
    def __init__(self, conta='TBANCONTA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_BAN002CA.json')
        
        self.gid = self._buscar_proximo_gid_conta()
        self.empresa = dados[conta]['empresa']
        self.codigo = self._buscar_proximo_codigo_conta()
        self.banco = dados[conta]['banco']
        self.agencia = dados[conta]['agencia']
        self.numero = dados[conta]['numero']
        self.digito = dados[conta]['digito']
        self.titular = dados[conta]['titular']
        self.tipo = dados[conta]['tipo']
        self.limite = dados[conta]['limite']
        self.saldopendente = dados[conta]['saldopendente']
        self.chequependente = dados[conta]['chequependente']
        self.saldoatual = dados[conta]['saldoatual']
        self.usuario = dados[conta]['usuario']
        self.usarcc = dados[conta]['usarcc']
        self.fluxocaixa = dados[conta]['fluxocaixa']
        self.usafavorecido = dados[conta]['usafavorecido']
        self.saldoatualbanco = dados[conta]['saldoatualbanco']
        self.ativo = dados[conta]['ativo']
        self.tipopessoacedente = dados[conta]['tipopessoacedente']
        self.cpfcnpjcedente = dados[conta]['cpfcnpjcedente']
        self.bancocorrespondente = dados[conta]['bancocorrespondente']
        self.agenciacorrespondente = dados[conta]['agenciacorrespondente']
        self.digitoagenciacorrespondente = dados[conta]['digitoagenciacorrespondente']
        self.contacorrentecorrespondente = dados[conta]['contacorrentecorrespondente']
        self.digcontacorrentecorrespondente = dados[conta]['digcontacorrentecorrespondente']
        self.gid_agencia = dados[conta]['gid_agencia']
        self.contapadrao = dados[conta]['contapadrao']

    def _buscar_proximo_codigo_conta(self):
        code = ''
        with engine.connect() as con:
            code = con.execute(text('SELECT MAX(CAST(CODIGO as integer)) FROM TBANCONTA;')).fetchall()
            
        if code[0][0]:
            codigo = int(code[0][0])
            codigo += 1
        else:
            codigo = 1
         
        return str(codigo).zfill(2)

    def _buscar_proximo_numero_conta(self):
        code = ''
        with engine.connect() as con:
            code = con.execute(text('SELECT MAX(CAST(NUMERO as integer)) FROM TBANCONTA;')).fetchall()
            
        if code[0][0]:
            codigo = int(code[0][0])
            codigo += 1
        else:
            codigo = 1
         
        return str(codigo)

    def _buscar_proximo_gid_conta(self):
        codigo = session.query(func.max(TBanConta.gid)).scalar()

        if codigo: 
            codigo = codigo + 1
        else:
            codigo = 1

        return codigo