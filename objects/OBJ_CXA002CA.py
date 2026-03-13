from services.FA_ManipulacaoDeArquivos import ler_json
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from datetime import date
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.ConfiguracoesBase import Base, engine, session

#from FA_Parametros import TCxaParametro

class Lancamentos:
    def __init__(self):
        self.tcxalancamento = TCxaLancamento()
        
class TCxaLancamento(Base):

    __tablename__ = 'TCXALANCAMENTO'

    gid = Column(BigInteger, nullable=False)
    empresa = Column(String(2), nullable=False)
    caixa = Column(String(2), nullable=False)
    data = Column(Date, nullable=False)
    numero = Column(Integer, primary_key=True, nullable=False)
    historico = Column(String(2), nullable=False)
    complemento = Column(String(50), nullable=False)
    valordh = Column(Numeric(18,2), default=0, nullable=False)
    valorch = Column(Numeric(18,2), default=0, nullable=False)
    valorchpre = Column(Numeric(18,2), default=0, nullable=False)
    iddeposito = Column(Integer, default=0)
    idbaixa = Column(Integer, default=0)
    idbaixach = Column(Integer, default=0)
    origem = Column(String(3), nullable=False)
    usuario = Column(String(15), nullable=False)
    idcheque = Column(Integer)
    idpagamento = Column(Integer)
    iddevolucaoch = Column(Integer)
    idquitacaoch = Column(Integer)
    idsangriasuprimento = Column(Integer)
    registradora = Column(String(2))
    idperiodo = Column(Integer)
    iddocumento = Column(Integer)
    idcreditofornecedor = Column(Integer)
    idsequencia = Column(Integer, nullable=False)
    idsequenciaorigem = Column(Integer)
    idvaletroco = Column(String(16))
    conciliado = Column(String(1))
    observacao = Column(String(10000))
    gid_tpagdocumento = Column(BigInteger)
    tipomovimento = Column(String(1))
    
    def __init__(self, lancamento='TCXALANCAMENTO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_CXA002CA.json')

        self.gid = self._buscar_proximo_numero_lancamento()
        self.empresa = dados[lancamento]['empresa']
        self.caixa = dados[lancamento]['caixa']
        self.data = dados[lancamento]['data']
        self.numero = self.gid
        self.historico = dados[lancamento]['historico']
        self.complemento = dados[lancamento]['complemento']
        self.valordh = dados[lancamento]['valordh']
        self.valorch = dados[lancamento]['valorch']
        self.valorchpre = dados[lancamento]['valorchpre']
        self.iddeposito = dados[lancamento]['iddeposito']
        self.idbaixa = dados[lancamento]['idbaixa']
        self.idbaixach = dados[lancamento]['idbaixach']
        self.origem = dados[lancamento]['origem']
        self.usuario = dados[lancamento]['usuario']
        self.idcheque = dados[lancamento]['idcheque']
        self.idpagamento = dados[lancamento]['idpagamento']
        self.iddevolucaoch = dados[lancamento]['iddevolucaoch']
        self.idquitacaoch = dados[lancamento]['idquitacaoch']
        self.idsangriasuprimento = dados[lancamento]['idsangriasuprimento']
        self.registradora = dados[lancamento]['registradora']
        self.idperiodo = dados[lancamento]['idperiodo']
        self.iddocumento = dados[lancamento]['iddocumento']
        self.idcreditofornecedor = dados[lancamento]['idcreditofornecedor']
        self.idsequencia = self.gid
        self.idsequenciaorigem = dados[lancamento]['idsequenciaorigem']
        self.idvaletroco = dados[lancamento]['idvaletroco']
        self.conciliado = dados[lancamento]['conciliado']
        self.observacao = dados[lancamento]['observacao']
        self.gid_tpagdocumento = dados[lancamento]['gid_tpagdocumento']
        self.tipomovimento = dados[lancamento]['tipomovimento']
    
    def _buscar_proximo_numero_lancamento(self):
        codigo = session.query(func.max(TCxaLancamento.gid)).scalar()
        
        if codigo:
            codigo += 1
        else:
            codigo = 1
            
        return codigo