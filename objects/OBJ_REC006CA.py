from services.FA_ManipulacaoDeArquivos import ler_json
import re
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from services.ConfiguracoesBase import Base, engine, session
from datetime import timedelta, datetime, date
from objects.OBJ_REC000CA import TRecCliente
from objects.OBJ_REC007CA import TRecTipoDocumento


class Documento:
    def __init__(self, documentos='TRECDOCUMENTO_01', parcela='TRECPARCELA', valor=None, qtd_parc=None, emissao=None):
        self.trecdocumento = TRecDocumento(documentos)

        if valor is not None:
            self.trecdocumento.valor = valor
        if qtd_parc is not None:
            self.trecdocumento.qtdparcela = qtd_parc        
        if emissao is not None:
            self.trecdocumento.emissao = emissao

        self.cliente = session.query(TRecCliente).order_by(TRecCliente.gid.desc()).first() 
        self.trecdocumento.empresa = self.cliente.empresa
        self.trecdocumento.cliente = self.cliente.codigo

        qtd_parcelas = int(self.trecdocumento.qtdparcela)
        valor_total = float(self.trecdocumento.valor)

        valor_por_parcela = round(valor_total / qtd_parcelas, 2)

        self.trecparcelas = []

        parcela_temp = TRecParcela(parcela)

        id_seq_base = parcela_temp._buscar_proximo_idsequencia_parcela()
        id_trec_base = parcela_temp._buscar_proximo_idtrecparcela()

        for i in range(1, qtd_parcelas + 1):
                nova_parcela = TRecParcela(parcela)

                nova_parcela.empresa = self.trecdocumento.empresa
                nova_parcela.cliente = self.trecdocumento.cliente
                nova_parcela.tipo = self.trecdocumento.tipo
                nova_parcela.documento = self.trecdocumento.documento
                nova_parcela.vencimento = self.trecdocumento.emissao

                venc_texto = nova_parcela.vencimento

                if venc_texto == 'NOW' or not venc_texto:
                    data_base = date.today()
                elif isinstance(venc_texto, str):
                    data_base = datetime.strptime(venc_texto, '%Y-%m-%d').date()
                else:
                    data_base = venc_texto

                nova_parcela.vencimento = data_base + timedelta(days=30 * (i - 1))

                nova_parcela.parcela = str(i).zfill(3)

                nova_parcela.valor = valor_por_parcela
                nova_parcela.valorpendente = valor_por_parcela

                nova_parcela.idsequencia = id_seq_base + (i - 1)
                nova_parcela.idtrecparcela = id_trec_base + (i - 1)

                if i == qtd_parcelas:
                    soma_parcelas = valor_por_parcela * qtd_parcelas
                    diferenca = valor_total - soma_parcelas
                    if diferenca != 0:
                        nova_parcela.valor += diferenca
                        nova_parcela.valorpendente += diferenca

                self.trecparcelas.append(nova_parcela)

class TRecDocumento(Base):
    __tablename__ = 'TRECDOCUMENTO'
    
    empresa = Column(String(2), ForeignKey('TRECCLIENTE.empresa'), nullable=False)
    cliente = Column(String(5), ForeignKey('TRECCLIENTE.codigo'), nullable=False)
    tipo = Column(String(2), ForeignKey('TRECTIPODOCUMENTO.codigo'), nullable=False)
    documento = Column(String(7), primary_key=True, nullable=False)
    datadigitacao = Column(Date, default='NOW', nullable=False)
    emissao = Column(Date, nullable=False)
    valor = Column(Numeric(18,2), nullable=False)
    possuiindice = Column(String(1))
    indice = Column(String(2))
    valorindice = Column(Numeric(10,5), default=0)
    qtdparcela = Column(Integer, default=1, nullable=False)
    origem = Column(String(3), nullable=False)
    usuario = Column(String(15), nullable=False)
    observacao = Column(String(40))
    vendedor = Column(String(3))
    geracomissao = Column(String(1), default='S')
    lote = Column(String(50))
    iddocumento = Column(Integer)
    condicaopagamento = Column(String(3))
    complemento = Column(String(60))
    idbaixaorigem = Column(Integer)
    ajuste = Column(Numeric(18,2), default=0)
    documentoorigem = Column(String(20))
    idquitacaocheque = Column(Integer)
    percentualcomissao = Column(Numeric(15,2))
    tipovinculo = Column(SmallInteger)
    imoultajuste = Column(Integer)
    imotipoparcela = Column(String(1))
    datahoraalteracao = Column(DateTime, default='NOW')
    numerocontrato = Column(Integer)
    tipointegracaocartao = Column(Integer)

    fk_empresa = relationship('TRecCliente', foreign_keys='TRecDocumento.empresa')
    fk_cliente = relationship('TRecCliente', foreign_keys='TRecDocumento.cliente')
    fk_tipo_documento = relationship('TRecTipoDocumento', foreign_keys='TRecDocumento.tipo')
    
    def __init__(self, documentos='TRECDOCUMENTO_01'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC006CA.json')
        
        self.empresa = dados[documentos]['empresa']
        self.cliente = dados[documentos]['cliente']
        self.tipo = dados[documentos]['tipo']
        self.documento = str(self._buscar_proximo_iddocumento())
        self.datadigitacao = dados[documentos]['datadigitacao']
        self.emissao = dados[documentos]['emissao']
        self.valor = dados[documentos]['valor']
        self.possuiindice = dados[documentos]['possuiindice']
        self.indice = dados[documentos]['indice']
        self.valorindice = dados[documentos]['valorindice']
        self.qtdparcela = dados[documentos]['qtdparcela']
        self.origem = dados[documentos]['origem']
        self.usuario = dados[documentos]['usuario']
        self.observacao = dados[documentos]['observacao']
        self.vendedor = dados[documentos]['vendedor']
        self.geracomissao = dados[documentos]['geracomissao']
        self.lote = dados[documentos]['lote']
        self.iddocumento = self._buscar_proximo_iddocumento()
        self.condicaopagamento = dados[documentos]['condicaopagamento']
        self.complemento = dados[documentos]['complemento']
        self.idbaixaorigem = dados[documentos]['idbaixaorigem']
        self.ajuste = dados[documentos]['ajuste']
        self.documentoorigem = self.documento
        self.idquitacaocheque = dados[documentos]['idquitacaocheque']
        self.percentualcomissao = dados[documentos]['percentualcomissao']
        self.tipovinculo = dados[documentos]['tipovinculo']
        self.imoultajuste = dados[documentos]['imoultajuste']
        self.imotipoparcela = dados[documentos]['imotipoparcela']
        self.datahoraalteracao = dados[documentos]['datahoraalteracao']
        self.numerocontrato = dados[documentos]['numerocontrato']
        self.tipointegracaocartao = dados[documentos]['tipointegracaocartao']
        
    def _buscar_proximo_documento(self):                
        code = ''
        with engine.connect() as con:
            code = con.execute(text('SELECT DOCUMENTO FROM TRECDOCUMENTO')).scalar()
            
        code = re.findall(r'([\d]+)', str(code[0][0]))
            
        if code:
            codigo = int(code[0])
            codigo += 1
        else:
            codigo = 1
         
        return str(codigo)

    def _buscar_proximo_iddocumento(self):
        codigo = session.query(func.max(TRecDocumento.iddocumento)).scalar()

        if codigo:
            codigo += 1
        else:
            codigo = 1
            
        return codigo


class TRecParcela(Base):
    __tablename__ = 'TRECPARCELA'

    empresa = Column(String(2), ForeignKey('TRECDOCUMENTO.empresa'), primary_key=True, nullable=False)
    cliente = Column(String(5), ForeignKey('TRECDOCUMENTO.cliente'), primary_key=True, nullable=False)
    tipo = Column(String(2), ForeignKey('TRECDOCUMENTO.tipo'), primary_key=True, nullable=False)
    documento = Column(String(7), ForeignKey('TRECDOCUMENTO.documento'), primary_key=True, nullable=False)
    parcela = Column(String(3), primary_key=True, nullable=False)
    idsequencia = Column(Integer)
    vencimento = Column(Date, nullable=False)
    ultimorecebimento = Column(Date)
    databaixa = Column(Date)
    valor = Column(Numeric(18,2), nullable=False)
    valorpendente = Column(Numeric(18,2))
    jurosacumulado = Column(Numeric(18,2), default=0)
    portador = Column(String(2), nullable=False)
    situacao = Column(String(1), default='N')
    idboleto = Column(String(7))
    databoleto = Column(Date)
    idbaixaorigem = Column(Integer)
    nossonumero = Column(String(20))
    data_programada = Column(Date)
    idprogramacao = Column(Integer)
    tipoprog = Column(String(2))
    docrenegociacao = Column(String(7))
    idsequenciaspc = Column(Integer)
    idrenegociacao = Column(Integer)
    situacaoremessa = Column(SmallInteger)
    taxaadministradora = Column(Numeric(18,2))
    idquitacaocheque = Column(Integer)
    valorissqnretido = Column(Numeric(18,2))
    serasa = Column(String(1), default='N')
    imoparcelabase = Column(Numeric(18,2))
    imojurosparcela = Column(Numeric(18,2))
    imosaldodevedor = Column(Numeric(18,2))
    imopercjurosac = Column(Numeric(7,4))
    nnboleto = Column(String(30))
    irrfvalorretido = Column(Numeric(16,2))
    pisvalorretido = Column(Numeric(16,2))
    cofinsvalorretido = Column(Numeric(16,2))
    inssvalorretido = Column(Numeric(16,2))
    csllvalorretido = Column(Numeric(16,2))
    imovalorbolao = Column(Numeric(16,2))
    imovalororigem = Column(Numeric(16,2))
    imoajusteacumulado = Column(Numeric(16,2))
    datahoraalteracao = Column(DateTime, default='NOW')
    iddesconto = Column(Integer)
    idtrecparcela = Column(BigInteger, nullable=False)
    obs = Column(String(10000))

    fk_empresa = relationship('TRecDocumento', foreign_keys='TRecParcela.empresa')
    fk_cliente = relationship('TRecDocumento', foreign_keys='TRecParcela.cliente')
    fk_tipo = relationship('TRecDocumento', foreign_keys='TRecParcela.tipo')
    fk_documento = relationship('TRecDocumento', foreign_keys='TRecParcela.documento')


    def __init__(self, parcela='TRECPARCELA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC006CA.json')

        self.empresa = dados[parcela]['empresa']
        self.cliente = dados[parcela]['cliente']
        self.tipo = dados[parcela]['tipo']
        self.documento = dados[parcela]['documento']
        self.parcela = dados[parcela]['parcela']
        self.idsequencia = self._buscar_proximo_idsequencia_parcela()
        self.vencimento = dados[parcela]['vencimento']
        self.ultimorecebimento = dados[parcela]['ultimorecebimento']
        self.databaixa = dados[parcela]['databaixa']
        self.valor = dados[parcela]['valor']
        self.valorpendente = dados[parcela]['valorpendente']
        self.jurosacumulado = dados[parcela]['jurosacumulado']
        self.portador = dados[parcela]['portador']
        self.situacao = dados[parcela]['situacao']
        self.idboleto = dados[parcela]['idboleto']
        self.databoleto = dados[parcela]['databoleto']
        self.idbaixaorigem = dados[parcela]['idbaixaorigem']
        self.nossonumero = dados[parcela]['nossonumero']
        self.data_programada = dados[parcela]['data_programada']
        self.idprogramacao = dados[parcela]['idprogramacao']
        self.tipoprog = dados[parcela]['tipoprog']
        self.docrenegociacao = dados[parcela]['docrenegociacao']
        self.idsequenciaspc = dados[parcela]['idsequenciaspc']
        self.idrenegociacao = dados[parcela]['idrenegociacao']
        self.situacaoremessa = dados[parcela]['situacaoremessa']
        self.taxaadministradora = dados[parcela]['taxaadministradora']
        self.idquitacaocheque = dados[parcela]['idquitacaocheque']
        self.valorissqnretido = dados[parcela]['valorissqnretido']
        self.serasa = dados[parcela]['serasa']
        self.imoparcelabase = dados[parcela]['imoparcelabase']
        self.imojurosparcela = dados[parcela]['imojurosparcela']
        self.imosaldodevedor = dados[parcela]['imosaldodevedor']
        self.imopercjurosac = dados[parcela]['imopercjurosac']
        self.nnboleto = dados[parcela]['nnboleto']
        self.irrfvalorretido = dados[parcela]['irrfvalorretido']
        self.pisvalorretido = dados[parcela]['pisvalorretido']
        self.cofinsvalorretido = dados[parcela]['cofinsvalorretido']
        self.inssvalorretido = dados[parcela]['inssvalorretido']
        self.csllvalorretido = dados[parcela]['csllvalorretido']
        self.imovalorbolao = dados[parcela]['imovalorbolao']
        self.imovalororigem = dados[parcela]['imovalororigem']
        self.imoajusteacumulado = dados[parcela]['imoajusteacumulado']
        self.datahoraalteracao = dados[parcela]['datahoraalteracao']
        self.iddesconto = dados[parcela]['iddesconto']
        self.idtrecparcela = self._buscar_proximo_idtrecparcela()
        self.obs = dados[parcela]['obs']

    def _buscar_proximo_idsequencia_parcela(self):
        codigo = session.query(func.max(TRecParcela.idsequencia)).scalar()
        
        if codigo:
            codigo += 1
        else:
            codigo = 1
            
        return codigo

    def _buscar_proximo_idtrecparcela(self):
        codigo = session.query(func.max(TRecParcela.idtrecparcela)).scalar()

        if codigo:
            codigo += 1
        else:
            codigo = 1
            
        return codigo