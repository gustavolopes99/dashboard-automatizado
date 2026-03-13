import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from sqlalchemy import (Column, String, Integer)
from services.ConfiguracoesBase import Base
    
class TGerTipoBloqueioRemoto(Base):
    
    __tablename__ = 'TGERTIPOBLOQUEIOREMOTO'
    
    codigo = Column(Integer, primary_key=True, nullable=False)
    descricao = Column(String(40))
    percentual = Column(String(1), default='N')
    ativo = Column(String(1), default='S')