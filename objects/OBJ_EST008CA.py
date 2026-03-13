import datetime
from services.FA_ManipulacaoDeArquivos import ler_json
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy import select, text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from services.ConfiguracoesBase import Base, session, engine
from datetime import date

class CondicaoPagamento:
    
    def __init__(self, condicao_pagamento="TESTCONDPAGVENDA_01"):
        self.testcondpagvenda = TEstCondPagVenda(condicao_pagamento)        

class TEstCondPagVenda(Base):
    
    __tablename__ = "TESTCONDPAGVENDA"
    
    empresa = Column(String(2), primary_key=True, nullable=False)
    codigo = Column(String(3), primary_key=True, nullable=False)
    tipo = Column(String(2), nullable=False)
    forma = Column(String(2), nullable=False)
    qtdparcela = Column(Integer, nullable=False)
    diasemana = Column(Integer)
    dodia1 = Column(Integer)
    aodia1 = Column(Integer)
    diavencimento1 = Column(Integer)
    dodia2 = Column(Integer)
    aodia2 = Column(Integer)
    diavencimento2 = Column(Integer)
    dodia3 = Column(Integer)
    aodia3 = Column(Integer)
    diavencimento3 = Column(Integer)
    acrescimo = Column(Numeric(6,4), nullable=False)
    administradora = Column(String(5))
    tipocontrato = Column(String(2))
    ativa = Column(String(1), nullable=False)
    usuario = Column(String(15), nullable=False)
    percmaxdesc = Column(Numeric(6,4))
    comentrada = Column(String(1))
    percminent = Column(Numeric(6,4))
    editavcto = Column(String(1), default='N', nullable=False)
    descricao = Column(String(40), nullable=False)
    prazoadicional = Column(Integer)
    utilizanovarejo = Column(String(1))
    utilizanoatacado = Column(String(1))
    ignorarajusteproduto = Column(String(1), default='N')
    controlavariacao = Column(String(1), default='N')
    diasvariacao1 = Column(Integer, default=0)
    diasvariacao2 = Column(Integer, default=0)
    taxaadm = Column(Numeric(6,4))
    diasrepasseadm = Column(SmallInteger)
    diaviradaadm = Column(SmallInteger)
    diarepasseadm = Column(SmallInteger)
    disponivelpda = Column(String(1))
    cartafrete = Column(String(1), default='N')
    editavctocheque = Column(String(1), nullable=False)
    permitetrococheque = Column(String(1), nullable=False)
    diretorioreqtef = Column(String(50))
    diretorioresptef = Column(String(50))
    debitocredito = Column(String(1))
    requisicao = Column(String(1), default='N')
    diasemana1 = Column(Integer)
    atediasemana1 = Column(Integer)
    diavencsemana1 = Column(Integer)
    diasemana2 = Column(Integer)
    atediasemana2 = Column(Integer)
    diavencsemana2 = Column(Integer)
    usacoeficiente = Column(String(1), default='N', nullable=False)
    ignorajurosentrada = Column(String(1), default='N', nullable=False)
    ajustecomissao = Column(Numeric(18,5))
    condpagto = Column(String(3))
    redetef = Column(Integer)
    idalteracao = Column(Integer, default=0, nullable=False)
    idenviopaf = Column(Integer, default=0, nullable=False)
    valorminimo = Column(Numeric(15,2), default=0)
    controlavariacaovalor = Column(String(1))
    percvariacaovalor = Column(Numeric(6,4))
    idenviomobile = Column(Integer, default=0)
    idbandeiraadministradora = Column(Integer)
    datahoraalteracao = Column(DateTime, default='NOW')
    minimoentradaautomatico = Column(String(1), default='N')
    enviaecoloja = Column(String(1), default='S')
    meiopagamento = Column(String(2), default=99, nullable=False)
    gidredesadquirentes = Column(BigInteger)
    tipocartao = Column(SmallInteger)
    tipofinanciamento = Column(SmallInteger)
    
    def __init__(self, condicao_pagamento):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_EST008CA.json')
        
        self.empresa = dados[condicao_pagamento]['empresa']
        self.codigo = self._buscar_proximo_codigo()
        self.tipo = dados[condicao_pagamento]['tipo']
        self.forma = dados[condicao_pagamento]['forma']
        self.qtdparcela = dados[condicao_pagamento]['qtdparcela']
        self.diasemana = dados[condicao_pagamento]['diasemana']
        self.dodia1 = dados[condicao_pagamento]['dodia1']
        self.aodia1 = dados[condicao_pagamento]['aodia1']
        self.diavencimento1 = dados[condicao_pagamento]['diavencimento1']
        self.dodia2 = dados[condicao_pagamento]['dodia2']
        self.aodia2 = dados[condicao_pagamento]['aodia2']
        self.diavencimento2 = dados[condicao_pagamento]['diavencimento2']
        self.dodia3 = dados[condicao_pagamento]['dodia3']
        self.aodia3 = dados[condicao_pagamento]['aodia3']
        self.diavencimento3 = dados[condicao_pagamento]['diavencimento3']
        self.acrescimo = dados[condicao_pagamento]['acrescimo']
        self.administradora = dados[condicao_pagamento]['administradora']
        self.tipocontrato = dados[condicao_pagamento]['tipocontrato']
        self.ativa = dados[condicao_pagamento]['ativa']
        self.usuario = dados[condicao_pagamento]['usuario']
        self.percmaxdesc = dados[condicao_pagamento]['percmaxdesc']
        self.comentrada = dados[condicao_pagamento]['comentrada']
        self.percminent = dados[condicao_pagamento]['percminent']
        self.editavcto = dados[condicao_pagamento]['editavcto']
        self.descricao = dados[condicao_pagamento]['descricao']
        self.prazoadicional = dados[condicao_pagamento]['prazoadicional']
        self.utilizanovarejo = dados[condicao_pagamento]['utilizanovarejo']
        self.utilizanoatacado = dados[condicao_pagamento]['utilizanoatacado']
        self.ignorarajusteproduto = dados[condicao_pagamento]['ignorarajusteproduto']
        self.controlavariacao = dados[condicao_pagamento]['controlavariacao']
        self.diasvariacao1 = dados[condicao_pagamento]['diasvariacao1']
        self.diasvariacao2 = dados[condicao_pagamento]['diasvariacao2']
        self.taxaadm = dados[condicao_pagamento]['taxaadm']
        self.diasrepasseadm = dados[condicao_pagamento]['diasrepasseadm']
        self.diaviradaadm = dados[condicao_pagamento]['diaviradaadm']
        self.diarepasseadm = dados[condicao_pagamento]['diarepasseadm']
        self.disponivelpda = dados[condicao_pagamento]['disponivelpda']
        self.cartafrete = dados[condicao_pagamento]['cartafrete']
        self.editavctocheque = dados[condicao_pagamento]['editavctocheque']
        self.permitetrococheque = dados[condicao_pagamento]['permitetrococheque']
        self.diretorioreqtef = dados[condicao_pagamento]['diretorioreqtef']
        self.diretorioresptef = dados[condicao_pagamento]['diretorioresptef']
        self.debitocredito = dados[condicao_pagamento]['debitocredito']
        self.requisicao = dados[condicao_pagamento]['requisicao']
        self.diasemana1 = dados[condicao_pagamento]['diasemana1']
        self.atediasemana1 = dados[condicao_pagamento]['atediasemana1']
        self.diavencsemana1 = dados[condicao_pagamento]['diavencsemana1']
        self.diasemana2 = dados[condicao_pagamento]['diasemana2']
        self.atediasemana2 = dados[condicao_pagamento]['atediasemana2']
        self.diavencsemana2 = dados[condicao_pagamento]['diavencsemana2']
        self.usacoeficiente = dados[condicao_pagamento]['usacoeficiente']
        self.ignorajurosentrada = dados[condicao_pagamento]['ignorajurosentrada']
        self.ajustecomissao = dados[condicao_pagamento]['ajustecomissao']
        self.condpagto = dados[condicao_pagamento]['condpagto']
        self.redetef = dados[condicao_pagamento]['redetef']
        self.idalteracao = dados[condicao_pagamento]['idalteracao']
        self.idenviopaf = dados[condicao_pagamento]['idenviopaf']
        self.valorminimo = dados[condicao_pagamento]['valorminimo']
        self.controlavariacaovalor = dados[condicao_pagamento]['controlavariacaovalor']
        self.percvariacaovalor = dados[condicao_pagamento]['percvariacaovalor']
        self.idenviomobile = dados[condicao_pagamento]['idenviomobile']
        self.idbandeiraadministradora = dados[condicao_pagamento]['idbandeiraadministradora']
        #self.datahoraalteracao = converter_dados.data_hora_atual(dados[condicao_pagamento]['datahoraalteracao'])
        self.minimoentradaautomatico = dados[condicao_pagamento]['minimoentradaautomatico']
        self.enviaecoloja = dados[condicao_pagamento]['enviaecoloja']
        self.meiopagamento = dados[condicao_pagamento]['meiopagamento']
        self.gidredesadquirentes = dados[condicao_pagamento]['gidredesadquirentes']
        self.tipocartao = dados[condicao_pagamento]['tipocartao']
        self.tipofinanciamento = dados[condicao_pagamento]['tipofinanciamento']

    def _buscar_proximo_codigo(self):
        code = ''
        with engine.connect() as con:
            code = con.execute(text('SELECT MAX(Codigo) AS Codigo FROM TEstCondPagVenda;')).fetchall()
            
        codigo = int(code[0][0])
        
        if codigo:
            codigo += 1
        else:
            codigo = 1
         
        return str(codigo).zfill(3)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    