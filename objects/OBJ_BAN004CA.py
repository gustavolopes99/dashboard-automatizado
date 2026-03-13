from services.FA_ManipulacaoDeArquivos import ler_json
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from datetime import date
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.ConfiguracoesBase import Base, engine, session

class Movimento:
    def __init__(self):
        self.tbanmovimento = TBanMovimento()
        
class TBanMovimento(Base):
    __tablename__ = 'TBANMOVIMENTO'

    gid = Column(BigInteger, primary_key=True, nullable=False)
    empresa = Column(String(2), nullable=False)
    conta = Column(String(2), nullable=False)
    data = Column(Date, nullable=False)
    numero = Column(Integer, nullable=False)
    operacao = Column(String(2), nullable=False)
    complemento = Column(String(50), nullable=False)
    valor = Column(Numeric(18,2), nullable=False)
    valordisponivel = Column(Numeric(18,2), default=0)
    vencimento = Column(Date)
    conciliado = Column(String(1), default='N', nullable=False)
    conciliacao = Column(Date)
    iddeposito = Column(Integer)
    idbaixach = Column(Integer)
    origem = Column(String(3), nullable=False)
    usuario = Column(String(15), nullable=False)
    idpagamento = Column(Integer)
    iddevolucaoch = Column(Integer)
    idbaixa = Column(Integer)
    idcreditofornecedor = Column(Integer)
    idquitacaoch = Column(Integer)
    idsequencia = Column(Integer)
    idcheque = Column(Integer)
    idmovimento = Column(Integer)
    identificador = Column(Integer)
    seriecheque = Column(String(6))
    clientedeposito = Column(String(5))
    iddesconto = Column(Integer)
    idboleto = Column(Integer)
    codcarteiraboleto = Column(String(2))
    observacao = Column(String(10000))
    tbancheque_gid = Column(BigInteger)
    trecestornodesconto_gid = Column(BigInteger)
    pix = Column(String(1), default='N')
    conciliacaoofx = Column(Date)
    ofx = Column(String(1), default='N')
    bxbanco = Column(SmallInteger)
    
    def __init__(self, movimento='TBANMOVIMENTO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_BAN004CA.json')

        self.gid = self._buscar_proximo_gid_movimento()
        self.empresa = dados[movimento]['empresa']
        self.conta = dados[movimento]['conta']
        self.data = dados[movimento]['data']
        self.numero = dados[movimento]['numero']
        self.operacao = dados[movimento]['operacao']
        self.complemento = dados[movimento]['complemento']
        self.valor = dados[movimento]['valor']
        self.valordisponivel = dados[movimento]['valordisponivel']
        self.vencimento = dados[movimento]['vencimento']
        self.conciliado = dados[movimento]['conciliado']
        self.conciliacao = dados[movimento]['conciliacao']
        self.iddeposito = dados[movimento]['iddeposito']
        self.idbaixach = dados[movimento]['idbaixach']
        self.origem = dados[movimento]['origem']
        self.usuario = dados[movimento]['usuario']
        self.idpagamento = dados[movimento]['idpagamento']
        self.iddevolucaoch = dados[movimento]['iddevolucaoch']
        self.idbaixa = dados[movimento]['idbaixa']
        self.idcreditofornecedor = dados[movimento]['idcreditofornecedor']
        self.idquitacaoch = dados[movimento]['idquitacaoch']
        self.idsequencia = self._buscar_proximo_idsequencia()
        self.idcheque = dados[movimento]['idcheque']
        self.idmovimento = dados[movimento]['idmovimento']
        self.identificador = dados[movimento]['identificador']
        self.seriecheque = dados[movimento]['seriecheque']
        self.clientedeposito = dados[movimento]['clientedeposito']
        self.iddesconto = dados[movimento]['iddesconto']
        self.idboleto = dados[movimento]['idboleto']
        self.codcarteiraboleto = dados[movimento]['codcarteiraboleto']
        self.observacao = dados[movimento]['observacao']
        self.tbancheque_gid = dados[movimento]['tbancheque_gid']
        self.trecestornodesconto_gid = dados[movimento]['trecestornodesconto_gid']
        self.pix = dados[movimento]['pix']
        self.conciliacaoofx = dados[movimento]['conciliacaoofx']
        self.ofx = dados[movimento]['ofx']
        self.bxbanco = dados[movimento]['bxbanco']

    def _buscar_proximo_gid_movimento(self):
        codigo = session.query(func.max(TBanMovimento.gid)).first()

        if codigo[0]: 
            codigo = codigo[0]+1
        else:
            codigo = 1

        return codigo

    def _buscar_proximo_idsequencia(self):
        codigo = session.query(func.max(TBanMovimento.idsequencia)).scalar()

        if codigo: 
            codigo = codigo+1
        else:
            codigo = 1

        return codigo