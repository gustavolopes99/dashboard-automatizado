import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.FA_ManipulacaoDeArquivos import ler_json
from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, SmallInteger, not_, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from services.ConfiguracoesBase import Base, Session, engine, session

class Cidade:
    
    def __init__(self, cidade='CIDADE_EXTERIOR_001'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_GER002CA.json')
        
        self.codigo = self._buscar_proximo_codigo_disponivel_cidade()
        self.tgercidade = TGerCidade(cidade, self.codigo)
        self.tgercidadeissqn = TGerCidadeIssqn(cidade, self.codigo)
        self.tgercidadeissqn.fk_tgercidade = self.tgercidade
        
    def _buscar_proximo_codigo_disponivel_cidade(self):
        for codigo_disponivel in range(1,9999):
            codigo_disponivel = str(codigo_disponivel).zfill(4)
            resultado = session.query(TGerCidade).filter(TGerCidade.codigo == codigo_disponivel).scalar()
            if resultado is None:
                break
        return codigo_disponivel


class TGerCidade(Base):
    
    __tablename__ = 'TGERCIDADE'
    
    codigo = Column(String(4),primary_key=True, nullable=False)
    nome = Column(String(30), nullable=False)
    ceppadrao = Column(String(10))
    ddd = Column(String(2))
    estado = Column(String(2), nullable=False)
    usuario = Column(String(15))
    codigonacional = Column(String(8))
    issqn = Column(Numeric(5,2))
    tipocidade = Column(String(1), default='m')
    idpais = Column(Integer)
    codigoibge = Column(Integer)
    ajusteprecopda = Column(Numeric(6,4))
    idalteracao = Column(Integer, default=0, nullable=False)
    idenviopaf = Column(Integer, default=0, nullable=False)
    datahoraalteracao = Column(DateTime, default='now')
    
    fk_tgercidadeissqn = relationship("TGerCidadeIssqn", back_populates="fk_tgercidade")
	
    def __init__(self, cidade, codigo):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_GER002CA.json')
        self.codigo = codigo
        self.nome = dados[cidade]['TGERCIDADE']['nome']
        self.ceppadrao = dados[cidade]['TGERCIDADE']['ceppadrao']
        self.ddd = dados[cidade]['TGERCIDADE']['ddd']
        self.estado = dados[cidade]['TGERCIDADE']['estado']
        self.usuario = dados[cidade]['TGERCIDADE']['usuario']
        self.codigonacional = dados[cidade]['TGERCIDADE']['codigonacional']
        self.issqn = dados[cidade]['TGERCIDADE']['issqn']
        self.tipocidade = dados[cidade]['TGERCIDADE']['tipocidade']
        self.idpais = dados[cidade]['TGERCIDADE']['idpais']
        self.codigoibge = dados[cidade]['TGERCIDADE']['codigoibge']
        self.ajusteprecopda = dados[cidade]['TGERCIDADE']['ajusteprecopda']
        self.idalteracao = dados[cidade]['TGERCIDADE']['idalteracao']
        self.idenviopaf = dados[cidade]['TGERCIDADE']['idenviopaf']
        
class TGerCidadeIssqn(Base):
    
    __tablename__ = 'TGERCIDADEISSQN'
    
    empresa = Column(String(2), nullable=False)
    cidade = Column(String(10), ForeignKey('TGERCIDADE.codigo'), primary_key=True, nullable=False)
    issqn = Column(Numeric(15,6), nullable=False)
    minimoretencao = Column(Numeric(18,2), nullable=False)
    
    fk_tgercidade = relationship("TGerCidade", back_populates="fk_tgercidadeissqn")
    
    def __init__(self, cidade, codigo):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_GER002CA.json')
        self.empresa = dados[cidade]['TGERCIDADEISSQN']['empresa']
        self.cidade = codigo
        self.issqn = dados[cidade]['TGERCIDADEISSQN']['issqn']
        self.minimoretencao = dados[cidade]['TGERCIDADEISSQN']['minimoretencao']