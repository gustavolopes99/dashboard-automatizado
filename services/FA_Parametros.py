from datetime import date
from ConfiguracoesBase import Base, engine, session
from sqlalchemy.sql import func, text
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (Column, String, Integer, Date, Numeric, LargeBinary,
                        ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
import datetime
from FA_ManipulacaoDeArquivos import ler_json
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')


class EcobrancaParametroAdicionais(Base):
    __tablename__ = 'ECOBRANCAPARAMETROADICIONAIS'

    nome = Column(String(80), primary_key=True, nullable=False)
    valor = Column(String(80), primary_key=True, nullable=False)
    tipo = Column(String(80), primary_key=True, nullable=False)
    items = Column(Integer)
    empresa = Column(String(2), primary_key=True, nullable=False)
    portador = Column(String(2), primary_key=True, nullable=False)
    nomecarteira = Column(String(200), primary_key=True, nullable=False)

    def __init__(self, parametro='ECOBRANCAPARAMETROADICIONAIS'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.nome = dados[parametro]['nome']
        self.valor = dados[parametro]['valor']
        self.tipo = dados[parametro]['tipo']
        self.items = dados[parametro]['items']
        self.empresa = dados[parametro]['empresa']
        self.portador = dados[parametro]['portador']
        self.nomecarteira = dados[parametro]['nomecarteira']


class TBanParametro(Base):
    __tablename__ = 'TBANPARAMETRO'

    empresa = Column(String(2), primary_key=True, nullable=True)
    databanco = Column(Date, nullable=True)
    opchempresa = Column(String(2))
    opdepempresa = Column(String(2))
    opdepcliente = Column(String(2))
    opliqboleto = Column(String(2))
    opnegcheque = Column(String(2))
    optaxanegcheque = Column(String(2))
    usachequecontinuo = Column(String(1), default='N')
    opdebitoconta = Column(String(2))
    opdevcheque = Column(String(2))
    opliqcartao = Column(String(2))
    opcreditoconta = Column(String(2))

    def __init__(self, parametro='TBANPARAMETRO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.databanco = dados[parametro]['databanco']
        self.opchempresa = dados[parametro]['opchempresa']
        self.opdepempresa = dados[parametro]['opdepempresa']
        self.opdepcliente = dados[parametro]['opdepcliente']
        self.opliqboleto = dados[parametro]['opliqboleto']
        self.opnegcheque = dados[parametro]['opnegcheque']
        self.optaxanegcheque = dados[parametro]['optaxanegcheque']
        self.usachequecontinuo = dados[parametro]['usachequecontinuo']
        self.opdebitoconta = dados[parametro]['opdebitoconta']
        self.opdevcheque = dados[parametro]['opdevcheque']
        self.opliqcartao = dados[parametro]['opliqcartao']
        self.opcreditoconta = dados[parametro]['opcreditoconta']


class TCobParametro(Base):
    __tablename__ = 'TCOBPARAMETRO'

    empresa = Column(String(2), primary_key=True, nullable=False)
    portador = Column(String(2), primary_key=True, nullable=False)
    cedente = Column(String(50))
    cnpjcedente = Column(String(14))
    codigoconta = Column(String(2), nullable=False)
    carteira = Column(String(3))
    variacaocarteira = Column(String(3))
    tipocarteira = Column(String(1))
    tiposervico = Column(String(2))
    especie = Column(String(2))
    aceite = Column(String(1))
    convenio = Column(String(16))
    contrato = Column(String(15))
    enviaremessa = Column(String(1))
    receberetorno = Column(String(1))
    caminhoremessa = Column(String(100))
    caminhoretorno = Column(String(100))
    sequenciaremessa = Column(Integer, default=0)
    sequenciaretorno = Column(Integer, default=0)
    sequencianossonumero = Column(Integer, default=0)
    diaslimiteenvio = Column(SmallInteger)
    padraolayout = Column(SmallInteger)
    baixadevolucao = Column(SmallInteger)
    diasbaixadevolucao = Column(SmallInteger)
    tipoboleto = Column(SmallInteger)
    layoutboleto = Column(String(50))
    modoteste = Column(String(1))
    anoatual = Column(SmallInteger)
    postoagencia = Column(SmallInteger)
    responsavelimpressao = Column(SmallInteger)
    codigoclientebanco = Column(String(7))
    protestar = Column(String(1))
    codigoempresa = Column(String(20))
    sequenciaarquivo = Column(Integer, default=0)
    idcedenteunicred = Column(String(8))
    agenciaunicred = Column(String(6))
    contaunicred = Column(String(10))
    nomeunidunicred = Column(String(40))
    dataremessa = Column(Date)
    sequenciadiaria = Column(Integer)

    def __init__(self, parametro='TCOBPARAMETRO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.portador = dados[parametro]['portador']
        self.cedente = dados[parametro]['cedente']
        self.cnpjcedente = dados[parametro]['cnpjcedente']
        self.codigoconta = dados[parametro]['codigoconta']
        self.carteira = dados[parametro]['carteira']
        self.variacaocarteira = dados[parametro]['variacaocarteira']
        self.tipocarteira = dados[parametro]['tipocarteira']
        self.tiposervico = dados[parametro]['tiposervico']
        self.especie = dados[parametro]['especie']
        self.aceite = dados[parametro]['aceite']
        self.convenio = dados[parametro]['convenio']
        self.contrato = dados[parametro]['contrato']
        self.enviaremessa = dados[parametro]['enviaremessa']
        self.receberetorno = dados[parametro]['receberetorno']
        self.caminhoremessa = dados[parametro]['caminhoremessa']
        self.caminhoretorno = dados[parametro]['caminhoretorno']
        self.sequenciaremessa = dados[parametro]['sequenciaremessa']
        self.sequenciaretorno = dados[parametro]['sequenciaretorno']
        self.sequencianossonumero = dados[parametro]['sequencianossonumero']
        self.diaslimiteenvio = dados[parametro]['diaslimiteenvio']
        self.padraolayout = dados[parametro]['padraolayout']
        self.baixadevolucao = dados[parametro]['baixadevolucao']
        self.diasbaixadevolucao = dados[parametro]['diasbaixadevolucao']
        self.tipoboleto = dados[parametro]['tipoboleto']
        self.layoutboleto = dados[parametro]['layoutboleto']
        self.modoteste = dados[parametro]['modoteste']
        self.anoatual = dados[parametro]['anoatual']
        self.postoagencia = dados[parametro]['postoagencia']
        self.responsavelimpressao = dados[parametro]['responsavelimpressao']
        self.codigoclientebanco = dados[parametro]['codigoclientebanco']
        self.protestar = dados[parametro]['protestar']
        self.codigoempresa = dados[parametro]['codigoempresa']
        self.sequenciaarquivo = dados[parametro]['sequenciaarquivo']
        self.idcedenteunicred = dados[parametro]['idcedenteunicred']
        self.agenciaunicred = dados[parametro]['agenciaunicred']
        self.contaunicred = dados[parametro]['contaunicred']
        self.nomeunidunicred = dados[parametro]['nomeunidunicred']
        self.dataremessa = dados[parametro]['dataremessa']
        self.sequenciadiaria = dados[parametro]['sequenciadiaria']


class TCobParametroCobreBem(Base):
    __tablename__ = 'TCOBPARAMETROCOBREBEM'

    empresa = Column(String(2), primary_key=True, nullable=False)
    portador = Column(String(2), primary_key=True, nullable=False)
    codigoconta = Column(String(2), nullable=False)
    codigocarteira = Column(String(25))
    codigoagencia = Column(String(10))
    numerocontacorrente = Column(String(20))
    config1 = Column(String(50))
    config2 = Column(String(50))
    config3 = Column(String(50))
    inicionossonumero = Column(String(25), default=0)
    fimnossonumero = Column(String(25))
    proximonossonumero = Column(String(25))
    arquivolicenca = Column(String(100))
    protestar = Column(String(1))
    diasprotesto = Column(SmallInteger)
    prazodevolucao = Column(SmallInteger)
    aceite = Column(String(1))
    tipodocumento = Column(String(50))
    enviaremessa = Column(String(1))
    caminhoremessa = Column(String(100))
    layoutremessa = Column(String(25))
    receberetorno = Column(String(1))
    caminhoretorno = Column(String(100))
    layoutretorno = Column(String(25))
    sequenciaremessa = Column(Integer, default=0)
    sequenciaretorno = Column(Integer, default=0)
    caminhoimagensboleto = Column(String(100))
    emissorboleto = Column(SmallInteger)
    formatoboleto = Column(SmallInteger)
    modeloboleto = Column(String(50))
    caminholayoutfrenteboleto = Column(String(100))
    cedente = Column(String(50))
    cnpjcedente = Column(String(14))
    sequenciaarquivo = Column(Integer, default=0)
    dataremessa = Column(Date)
    sequenciadiaria = Column(Integer, default=0)
    anoatual = Column(SmallInteger)
    caminholayoutversoboleto = Column(String(100))
    servidorsmtp = Column(String(50))
    portasmtp = Column(String(5))
    usuariosmtp = Column(String(50))
    senhasmtp = Column(String(20))
    impressorapadrao = Column(String(100))
    margemsuperior = Column(SmallInteger)
    bcb = Column(String(1))
    localpagamentoboleto = Column(String(100))
    modotrabalho = Column(String(1))
    tipojuros = Column(String(1), default='P')
    tipomulta = Column(String(1), default='P')
    tipodesconto = Column(String(1), default='P')
    percentualjurosdia = Column(Numeric(18, 2), default=0)
    valorjurosdia = Column(Numeric(18, 2), default=0)
    percentualmulta = Column(Numeric(18, 2), default=0)
    valormulta = Column(Numeric(18, 2), default=0)
    percentualdesconto = Column(Numeric(18, 2), default=0)
    valordesconto = Column(Numeric(18, 2), default=0)
    imprimejuros = Column(String(1), default='N')
    imprimemulta = Column(String(1), default='N')
    imprimedesconto = Column(String(1), default='N')
    mensagemdeprotesto = Column(String(250))

    def __init__(self, parametro='TCOBPARAMETROCOBREBEM'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.portador = dados[parametro]['portador']
        self.codigoconta = dados[parametro]['codigoconta']
        self.codigocarteira = dados[parametro]['codigocarteira']
        self.codigoagencia = dados[parametro]['codigoagencia']
        self.numerocontacorrente = dados[parametro]['numerocontacorrente']
        self.config1 = dados[parametro]['config1']
        self.config2 = dados[parametro]['config2']
        self.config3 = dados[parametro]['config3']
        self.inicionossonumero = dados[parametro]['inicionossonumero']
        self.fimnossonumero = dados[parametro]['fimnossonumero']
        self.proximonossonumero = dados[parametro]['proximonossonumero']
        self.arquivolicenca = dados[parametro]['arquivolicenca']
        self.protestar = dados[parametro]['protestar']
        self.diasprotesto = dados[parametro]['diasprotesto']
        self.prazodevolucao = dados[parametro]['prazodevolucao']
        self.aceite = dados[parametro]['aceite']
        self.tipodocumento = dados[parametro]['tipodocumento']
        self.enviaremessa = dados[parametro]['enviaremessa']
        self.caminhoremessa = dados[parametro]['caminhoremessa']
        self.layoutremessa = dados[parametro]['layoutremessa']
        self.receberetorno = dados[parametro]['receberetorno']
        self.caminhoretorno = dados[parametro]['caminhoretorno']
        self.layoutretorno = dados[parametro]['layoutretorno']
        self.sequenciaremessa = dados[parametro]['sequenciaremessa']
        self.sequenciaretorno = dados[parametro]['sequenciaretorno']
        self.caminhoimagensboleto = dados[parametro]['caminhoimagensboleto']
        self.emissorboleto = dados[parametro]['emissorboleto']
        self.formatoboleto = dados[parametro]['formatoboleto']
        self.modeloboleto = dados[parametro]['modeloboleto']
        self.caminholayoutfrenteboleto = dados[parametro]['caminholayoutfrenteboleto']
        self.cedente = dados[parametro]['cedente']
        self.cnpjcedente = dados[parametro]['cnpjcedente']
        self.sequenciaarquivo = dados[parametro]['sequenciaarquivo']
        self.dataremessa = dados[parametro]['dataremessa']
        self.sequenciadiaria = dados[parametro]['sequenciadiaria']
        self.anoatual = dados[parametro]['anoatual']
        self.caminholayoutversoboleto = dados[parametro]['caminholayoutversoboleto']
        self.servidorsmtp = dados[parametro]['servidorsmtp']
        self.portasmtp = dados[parametro]['portasmtp']
        self.usuariosmtp = dados[parametro]['usuariosmtp']
        self.senhasmtp = dados[parametro]['senhasmtp']
        self.impressorapadrao = dados[parametro]['impressorapadrao']
        self.margemsuperior = dados[parametro]['margemsuperior']
        self.bcb = dados[parametro]['bcb']
        self.localpagamentoboleto = dados[parametro]['localpagamentoboleto']
        self.modotrabalho = dados[parametro]['modotrabalho']
        self.tipojuros = dados[parametro]['tipojuros']
        self.tipomulta = dados[parametro]['tipomulta']
        self.tipodesconto = dados[parametro]['tipodesconto']
        self.percentualjurosdia = dados[parametro]['percentualjurosdia']
        self.valorjurosdia = dados[parametro]['valorjurosdia']
        self.percentualmulta = dados[parametro]['percentualmulta']
        self.valormulta = dados[parametro]['valormulta']
        self.percentualdesconto = dados[parametro]['percentualdesconto']
        self.valordesconto = dados[parametro]['valordesconto']
        self.imprimejuros = dados[parametro]['imprimejuros']
        self.imprimemulta = dados[parametro]['imprimemulta']
        self.imprimedesconto = dados[parametro]['imprimedesconto']
        self.mensagemdeprotesto = dados[parametro]['mensagemdeprotesto']


class TCobParametroEcobranca(Base):
    __tablename__ = 'TCOBPARAMETROECOBRANCA'

    empresa = Column(String(2), primary_key=True, nullable=False)
    portador = Column(String(2), primary_key=True, nullable=False)
    nomecarteira = Column(String(200), primary_key=True, nullable=False)
    codigoagenciaitems = Column(Integer)
    codigomulta = Column(String(80))
    codigomultaitems = Column(Integer)
    tipomulta = Column(String(1), default='P')
    percentualmulta = Column(Numeric(18, 2))
    codigojuros = Column(String(80))
    codigojurositems = Column(Integer)
    tipojuros = Column(String(1), default='P')
    percentualjuros = Column(Numeric(18, 2))
    codigodesconto = Column(String(80))
    codigodescontoitems = Column(Integer)
    tipodesconto = Column(String(1), default='P')
    percentualdesconto = Column(Numeric(18, 2))
    codigomoeda = Column(String(80))
    codigomoedaitems = Column(Integer)
    codigoaceite = Column(String(80))
    codigoaceiteitms = Column(Integer)
    codigobaixadevolucao = Column(String(80))
    codigobaixadevolucaoitems = Column(Integer)
    codigosprotesto = Column(String(80))
    codigosprotestoitems = Column(Integer)
    tipodocumentocobranca = Column(String(80))
    tipodocumentocobrancaitems = Column(Integer)
    diasprotesto = Column(String(10))
    diasbaixabevolucao = Column(String(10))
    remsequencialote = Column(Integer)
    remsequenciaremessa = Column(Integer)
    diretorioarquivoremessa = Column(String(250))
    layoutarquivoremessaitems = Column(Integer)
    layoutarquivoremessa = Column(String(200))
    codigomovimentoremessa = Column(String(80))
    codigomovimentoremessaitms = Column(Integer)
    exibepropaganda = Column(String(1), default='S')
    tipopropaganda = Column(String(40))
    tipopropagandaitems = Column(Integer)
    propaganda = Column(String(300))
    exibelogotipocedente = Column(String(1), default='S')
    logotipocedente = Column(String(300))
    exibesac = Column(String(1), default='S')
    diretorioimagens = Column(String(300))
    diretoriogeracaoboleto = Column(String(300))
    tipomodeloboletoutilizado = Column(String(200))
    tipomodeloboletoutilizadoitems = Column(Integer)
    numeroboletosporpagina = Column(Integer)
    numeroboletosporpaginaitmes = Column(Integer)
    altrecibopagador = Column(Integer)
    altreciboentrega = Column(Integer)
    exibecodbancorecibo = Column(String(1), default='S')
    exibeespelholinhadigitavel = Column(String(1), default='S')
    dirmodbolpersonalizado = Column(String(300))
    modeloboletopersonalizado = Column(String(200))
    layoutarquivoretorno = Column(String(80))
    layoutarquivoretornoitems = Column(Integer)
    modosimpressao = Column(String(200))
    modosimpressaoitms = Column(Integer)
    nomeimpressora = Column(String(200))
    nomeimpressoraitems = Column(Integer)
    programaleitorpdf = Column(String(200))
    diretorioarquivoretorno = Column(String(200))
    enviaremessa = Column(String(1))
    receberetorno = Column(String(1))
    codigoconta = Column(String(2))
    modotrabalho = Column(String(1))
    emissorboleto = Column(String(1))
    arquivolicenca = Column(String(250))
    localpagamento = Column(String(250))
    modosaida = Column(String(80))
    modosaidaitems = Column(Integer)
    formatosaida = Column(String(80))
    formatosaidaitems = Column(Integer)
    dataremessa = Column(Date)
    sequenciadiaria = Column(Integer)
    fbpersonalizado = Column(String(80))
    fbpersonalizadoitems = Column(Integer)
    hostsmtp = Column(String(45))
    portasmtp = Column(Integer)
    possuiautenticacao = Column(String(1))
    utilizassl = Column(String(1))
    usuariosmtp = Column(String(45))
    assunto = Column(String(200))
    mensagem = Column(String(200))
    prefixonomenclatura = Column(String(45))
    tiponomenclatura = Column(String(45))
    tiponomenclaturaitens = Column(Integer)
    geramensagemmulta = Column(String(1), default='''N''')
    geramensagemprotesto = Column(String(1), default='''N''')
    geramensagemdesconto = Column(String(1), default='N')
    geramensagemjuros = Column(String(1), default='N')
    operacao = Column(String(2))
    codcarteira = Column(String(4))
    codcarteiradescontada = Column(String(4))
    diaminimovenboleto = Column(Integer, default=3)
    tiponunboleto = Column(Integer, default=0, nullable=False)
    #codigotransmissao = Column(String(20))
    #codigotransmissaoitems = Column(Integer)
    instrucao = Column(String(500))
    exibecodigocli = Column(String(1), default='N')
    exibeparcelasboletosagrupados = Column(String(1), default='N')
    lancarabatimento = Column(String(1))

    def __init__(self, parametro='TCOBPARAMETROECOBRANCA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.portador = dados[parametro]['portador']
        self.nomecarteira = dados[parametro]['nomecarteira']
        self.codigoagenciaitems = dados[parametro]['codigoagenciaitems']
        self.codigomulta = dados[parametro]['codigomulta']
        self.codigomultaitems = dados[parametro]['codigomultaitems']
        self.tipomulta = dados[parametro]['tipomulta']
        self.percentualmulta = dados[parametro]['percentualmulta']
        self.codigojuros = dados[parametro]['codigojuros']
        self.codigojurositems = dados[parametro]['codigojurositems']
        self.tipojuros = dados[parametro]['tipojuros']
        self.percentualjuros = dados[parametro]['percentualjuros']
        self.codigodesconto = dados[parametro]['codigodesconto']
        self.codigodescontoitems = dados[parametro]['codigodescontoitems']
        self.tipodesconto = dados[parametro]['tipodesconto']
        self.percentualdesconto = dados[parametro]['percentualdesconto']
        self.codigomoeda = dados[parametro]['codigomoeda']
        self.codigomoedaitems = dados[parametro]['codigomoedaitems']
        self.codigoaceite = dados[parametro]['codigoaceite']
        self.codigoaceiteitms = dados[parametro]['codigoaceiteitms']
        self.codigobaixadevolucao = dados[parametro]['codigobaixadevolucao']
        self.codigobaixadevolucaoitems = dados[parametro]['codigobaixadevolucaoitems']
        self.codigosprotesto = dados[parametro]['codigosprotesto']
        self.codigosprotestoitems = dados[parametro]['codigosprotestoitems']
        self.tipodocumentocobranca = dados[parametro]['tipodocumentocobranca']
        self.tipodocumentocobrancaitems = dados[parametro]['tipodocumentocobrancaitems']
        self.diasprotesto = dados[parametro]['diasprotesto']
        self.diasbaixabevolucao = dados[parametro]['diasbaixabevolucao']
        self.remsequencialote = dados[parametro]['remsequencialote']
        self.remsequenciaremessa = dados[parametro]['remsequenciaremessa']
        self.diretorioarquivoremessa = dados[parametro]['diretorioarquivoremessa']
        self.layoutarquivoremessaitems = dados[parametro]['layoutarquivoremessaitems']
        self.layoutarquivoremessa = dados[parametro]['layoutarquivoremessa']
        self.codigomovimentoremessa = dados[parametro]['codigomovimentoremessa']
        self.codigomovimentoremessaitms = dados[parametro]['codigomovimentoremessaitms']
        self.exibepropaganda = dados[parametro]['exibepropaganda']
        self.tipopropaganda = dados[parametro]['tipopropaganda']
        self.tipopropagandaitems = dados[parametro]['tipopropagandaitems']
        self.propaganda = dados[parametro]['propaganda']
        self.exibelogotipocedente = dados[parametro]['exibelogotipocedente']
        self.logotipocedente = dados[parametro]['logotipocedente']
        self.exibesac = dados[parametro]['exibesac']
        self.diretorioimagens = dados[parametro]['diretorioimagens']
        self.diretoriogeracaoboleto = dados[parametro]['diretoriogeracaoboleto']
        self.tipomodeloboletoutilizado = dados[parametro]['tipomodeloboletoutilizado']
        self.tipomodeloboletoutilizadoitems = dados[parametro]['tipomodeloboletoutilizadoitems']
        self.numeroboletosporpagina = dados[parametro]['numeroboletosporpagina']
        self.numeroboletosporpaginaitmes = dados[parametro]['numeroboletosporpaginaitmes']
        self.altrecibopagador = dados[parametro]['altrecibopagador']
        self.altreciboentrega = dados[parametro]['altreciboentrega']
        self.exibecodbancorecibo = dados[parametro]['exibecodbancorecibo']
        self.exibeespelholinhadigitavel = dados[parametro]['exibeespelholinhadigitavel']
        self.dirmodbolpersonalizado = dados[parametro]['dirmodbolpersonalizado']
        self.modeloboletopersonalizado = dados[parametro]['modeloboletopersonalizado']
        self.layoutarquivoretorno = dados[parametro]['layoutarquivoretorno']
        self.layoutarquivoretornoitems = dados[parametro]['layoutarquivoretornoitems']
        self.modosimpressao = dados[parametro]['modosimpressao']
        self.modosimpressaoitms = dados[parametro]['modosimpressaoitms']
        self.nomeimpressora = dados[parametro]['nomeimpressora']
        self.nomeimpressoraitems = dados[parametro]['nomeimpressoraitems']
        self.programaleitorpdf = dados[parametro]['programaleitorpdf']
        self.diretorioarquivoretorno = dados[parametro]['diretorioarquivoretorno']
        self.enviaremessa = dados[parametro]['enviaremessa']
        self.receberetorno = dados[parametro]['receberetorno']
        self.codigoconta = dados[parametro]['codigoconta']
        self.modotrabalho = dados[parametro]['modotrabalho']
        self.emissorboleto = dados[parametro]['emissorboleto']
        self.arquivolicenca = dados[parametro]['arquivolicenca']
        self.localpagamento = dados[parametro]['localpagamento']
        self.modosaida = dados[parametro]['modosaida']
        self.modosaidaitems = dados[parametro]['modosaidaitems']
        self.formatosaida = dados[parametro]['formatosaida']
        self.formatosaidaitems = dados[parametro]['formatosaidaitems']
        self.dataremessa = dados[parametro]['dataremessa']
        self.sequenciadiaria = dados[parametro]['sequenciadiaria']
        self.fbpersonalizado = dados[parametro]['fbpersonalizado']
        self.fbpersonalizadoitems = dados[parametro]['fbpersonalizadoitems']
        self.hostsmtp = dados[parametro]['hostsmtp']
        self.portasmtp = dados[parametro]['portasmtp']
        self.possuiautenticacao = dados[parametro]['possuiautenticacao']
        self.utilizassl = dados[parametro]['utilizassl']
        self.usuariosmtp = dados[parametro]['usuariosmtp']
        self.assunto = dados[parametro]['assunto']
        self.mensagem = dados[parametro]['mensagem']
        self.prefixonomenclatura = dados[parametro]['prefixonomenclatura']
        self.tiponomenclatura = dados[parametro]['tiponomenclatura']
        self.tiponomenclaturaitens = dados[parametro]['tiponomenclaturaitens']
        self.geramensagemmulta = dados[parametro]['geramensagemmulta']
        self.geramensagemprotesto = dados[parametro]['geramensagemprotesto']
        self.geramensagemdesconto = dados[parametro]['geramensagemdesconto']
        self.geramensagemjuros = dados[parametro]['geramensagemjuros']
        self.operacao = dados[parametro]['operacao']
        self.codcarteira = dados[parametro]['codcarteira']
        self.codcarteiradescontada = dados[parametro]['codcarteiradescontada']
        self.diaminimovenboleto = dados[parametro]['diaminimovenboleto']
        self.tiponunboleto = dados[parametro]['tiponunboleto']
        #self.codigotransmissao = dados[parametro]['codigotransmissao']
        #self.codigotransmissaoitems = dados[parametro]['codigotransmissaoitems']
        self.instrucao = dados[parametro]['instrucao']
        self.exibecodigocli = dados[parametro]['exibecodigocli']
        self.exibeparcelasboletosagrupados = dados[parametro]['exibeparcelasboletosagrupados']
        self.lancarabatimento = dados[parametro]['lancarabatimento']


class TCxaParametro(Base):

    __tablename__ = 'TCXAPARAMETRO'

    empresa = Column(String(2), primary_key=True, nullable=False)
    datacaixa = Column(Date, nullable=False)
    caixapadrao = Column(String(2), nullable=False)
    caixarecdocumento = Column(String(2))
    caixaentradareg = Column(String(2))
    caixanegcheque = Column(String(2))
    historicodepositobanco = Column(String(2))
    historicorecdoc = Column(String(2))
    historicoentradareg = Column(String(2))
    historicotrococheque = Column(String(2))
    historiconegcheque = Column(String(2))
    historicotaxanegcheque = Column(String(2))
    historicopagdoc = Column(String(2))
    iddeposito = Column(Integer, default=0)
    historicosobracaixa = Column(String(2))
    historicofaltacaixa = Column(String(2))
    historicosangria = Column(String(2))
    historicosuprimento = Column(String(2))
    historicobaixacheque = Column(String(2))
    idpagamento = Column(Integer)
    historicorecebtrococheque = Column(String(2))
    histquitchcredito = Column(String(2))
    histquitchdebito = Column(String(2))
    histdevolucaoch = Column(String(2))
    histtransfcheque = Column(String(2))
    histchequespre = Column(String(2))
    histcontasreceber = Column(String(2))
    histcontaspagar = Column(String(2))
    caixacontrapartidactarec = Column(String(2))
    geracontrapartidactarec = Column(String(1), default='N')
    historicopagcredito = Column(String(2))
    geracontrapartidacheque = Column(String(1), default='N')
    caixacontrapartidacheque = Column(String(2))
    geracontrapartidactapag = Column(String(1), default='N')
    caixacontrapartidactapag = Column(String(2))
    histjuroquitacaocheque = Column(String(2))
    histdescontoquitacaocheque = Column(String(2))
    histcreditofornecedor = Column(String(2))
    historicopagcreditoposto = Column(String(2))
    historicosaidacp = Column(String(2))
    historicoentradacp = Column(String(2))

    def __init__(self, parametro='TCXAPARAMETRO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.datacaixa = dados[parametro]['datacaixa']
        self.caixapadrao = dados[parametro]['caixapadrao']
        self.caixarecdocumento = dados[parametro]['caixarecdocumento']
        self.caixaentradareg = dados[parametro]['caixaentradareg']
        self.caixanegcheque = dados[parametro]['caixanegcheque']
        self.historicodepositobanco = dados[parametro]['historicodepositobanco']
        self.historicorecdoc = dados[parametro]['historicorecdoc']
        self.historicoentradareg = dados[parametro]['historicoentradareg']
        self.historicotrococheque = dados[parametro]['historicotrococheque']
        self.historiconegcheque = dados[parametro]['historiconegcheque']
        self.historicotaxanegcheque = dados[parametro]['historicotaxanegcheque']
        self.historicopagdoc = dados[parametro]['historicopagdoc']
        self.iddeposito = dados[parametro]['iddeposito']
        self.historicosobracaixa = dados[parametro]['historicosobracaixa']
        self.historicofaltacaixa = dados[parametro]['historicofaltacaixa']
        self.historicosangria = dados[parametro]['historicosangria']
        self.historicosuprimento = dados[parametro]['historicosuprimento']
        self.historicobaixacheque = dados[parametro]['historicobaixacheque']
        self.idpagamento = dados[parametro]['idpagamento']
        self.historicorecebtrococheque = dados[parametro]['historicorecebtrococheque']
        self.histquitchcredito = dados[parametro]['histquitchcredito']
        self.histquitchdebito = dados[parametro]['histquitchdebito']
        self.histdevolucaoch = dados[parametro]['histdevolucaoch']
        self.histtransfcheque = dados[parametro]['histtransfcheque']
        self.histchequespre = dados[parametro]['histchequespre']
        self.histcontasreceber = dados[parametro]['histcontasreceber']
        self.histcontaspagar = dados[parametro]['histcontaspagar']
        self.caixacontrapartidactarec = dados[parametro]['caixacontrapartidactarec']
        self.geracontrapartidactarec = dados[parametro]['geracontrapartidactarec']
        self.historicopagcredito = dados[parametro]['historicopagcredito']
        self.geracontrapartidacheque = dados[parametro]['geracontrapartidacheque']
        self.caixacontrapartidacheque = dados[parametro]['caixacontrapartidacheque']
        self.geracontrapartidactapag = dados[parametro]['geracontrapartidactapag']
        self.caixacontrapartidactapag = dados[parametro]['caixacontrapartidactapag']
        self.histjuroquitacaocheque = dados[parametro]['histjuroquitacaocheque']
        self.histdescontoquitacaocheque = dados[parametro]['histdescontoquitacaocheque']
        self.histcreditofornecedor = dados[parametro]['histcreditofornecedor']
        self.historicopagcreditoposto = dados[parametro]['historicopagcreditoposto']
        self.historicosaidacp = dados[parametro]['historicosaidacp']
        self.historicoentradacp = dados[parametro]['historicoentradacp']


class TEstParametro(Base):
    __tablename__ = 'TESTPARAMETRO'

    empresa = Column(String(2), primary_key=True, nullable=False)
    tipodocpadrao = Column(String(2))
    custocodificado = Column(String(10), default='0123456789', nullable=False)
    produto = Column(Integer, default=0)
    ajusteid = Column(Integer)
    inventarioid = Column(Integer, default=0)
    estoquenegativo = Column(String(1), default='N')
    usaalmox = Column(String(1), default='N')
    almoxpadrao = Column(String(2))
    idtransfalmox = Column(Integer)
    alteracusto = Column(String(1), default='S')
    idrevisao = Column(Integer, default=0)
    editaprecodevolucao = Column(String(1), default='N')
    setortrocadeoleo = Column(String(3))
    pis = Column(String(2))
    cofins = Column(String(2))
    identrega = Column(Integer)
    idcarga = Column(Integer)
    servirrfaliq = Column(Numeric(6, 2))
    servirrfvlrmin = Column(Numeric(16, 2))
    servpisaliq = Column(Numeric(6, 2))
    servpisvlrmin = Column(Numeric(16, 2))
    servcofinsaliq = Column(Numeric(6, 2))
    servcofinsvlrmin = Column(Numeric(16, 2))
    servinssaliq = Column(Numeric(6, 2))
    servinssvlrmin = Column(Numeric(16, 2))
    servcsllaliq = Column(Numeric(6, 2))
    servcsllvlrmin = Column(Numeric(16, 2))
    idalteracao = Column(Integer, default=0)
    idenviopaf = Column(Integer, default=0)
    codigoidnfentrada = Column(Integer)
    datahoraalteracao = Column(DateTime, default='NOW')
    idkeysistema = Column(String(50))
    ambientenfse = Column(SmallInteger, default=2)
    indsincronoassincrono = Column(Integer, default=1)
    tipocertificadonfse = Column(String(2), default='A1')
    certificadonfse = Column(String(200))
    senhacertificadonfse = Column(String(100))
    reciboprovisorioservico = Column(String(200))
    notafiscaleletronicaservico = Column(String(200))
    comprovanteretencaoservico = Column(String(200))
    cancelarnfse = Column(String(1), default='S')
    usuarionfse = Column(String(100))
    senhanfse = Column(String(100))
    idtoken = Column(String(100))
    chavedigital = Column(String(100))
    numeroemissor = Column(String(50))
    versaoxml = Column(String(20), default='1')
    usanfemonitornfse = Column(String(1), default='S')
    idlotenfse = Column(BigInteger)
    usadfemonitornfse = Column(String(1), default='N')
    cancelarnfsest = Column(String(1), default='S')
    indarredondamentovaloriss = Column(SmallInteger, default=1)
    reducaoirrf = Column(String(1))
    reducaoinss = Column(String(1))
    reducaocsll = Column(String(1))

    def __init__(self, parametro='TESTPARAMETRO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.tipodocpadrao = dados[parametro]['tipodocpadrao']
        self.custocodificado = dados[parametro]['custocodificado']
        self.produto = dados[parametro]['produto']
        self.ajusteid = dados[parametro]['ajusteid']
        self.inventarioid = dados[parametro]['inventarioid']
        self.estoquenegativo = dados[parametro]['estoquenegativo']
        self.usaalmox = dados[parametro]['usaalmox']
        self.almoxpadrao = dados[parametro]['almoxpadrao']
        self.idtransfalmox = dados[parametro]['idtransfalmox']
        self.alteracusto = dados[parametro]['alteracusto']
        self.idrevisao = dados[parametro]['idrevisao']
        self.editaprecodevolucao = dados[parametro]['editaprecodevolucao']
        self.setortrocadeoleo = dados[parametro]['setortrocadeoleo']
        self.pis = dados[parametro]['pis']
        self.cofins = dados[parametro]['cofins']
        self.identrega = dados[parametro]['identrega']
        self.idcarga = dados[parametro]['idcarga']
        self.servirrfaliq = dados[parametro]['servirrfaliq']
        self.servirrfvlrmin = dados[parametro]['servirrfvlrmin']
        self.servpisaliq = dados[parametro]['servpisaliq']
        self.servpisvlrmin = dados[parametro]['servpisvlrmin']
        self.servcofinsaliq = dados[parametro]['servcofinsaliq']
        self.servcofinsvlrmin = dados[parametro]['servcofinsvlrmin']
        self.servinssaliq = dados[parametro]['servinssaliq']
        self.servinssvlrmin = dados[parametro]['servinssvlrmin']
        self.servcsllaliq = dados[parametro]['servcsllaliq']
        self.servcsllvlrmin = dados[parametro]['servcsllvlrmin']
        self.idalteracao = dados[parametro]['idalteracao']
        self.idenviopaf = dados[parametro]['idenviopaf']
        self.codigoidnfentrada = dados[parametro]['codigoidnfentrada']
        self.datahoraalteracao = dados[parametro]['datahoraalteracao']
        self.idkeysistema = dados[parametro]['idkeysistema']
        self.ambientenfse = dados[parametro]['ambientenfse']
        self.indsincronoassincrono = dados[parametro]['indsincronoassincrono']
        self.tipocertificadonfse = dados[parametro]['tipocertificadonfse']
        self.certificadonfse = dados[parametro]['certificadonfse']
        self.senhacertificadonfse = dados[parametro]['senhacertificadonfse']
        self.reciboprovisorioservico = dados[parametro]['reciboprovisorioservico']
        self.notafiscaleletronicaservico = dados[parametro]['notafiscaleletronicaservico']
        self.comprovanteretencaoservico = dados[parametro]['comprovanteretencaoservico']
        self.cancelarnfse = dados[parametro]['cancelarnfse']
        self.usuarionfse = dados[parametro]['usuarionfse']
        self.senhanfse = dados[parametro]['senhanfse']
        self.idtoken = dados[parametro]['idtoken']
        self.chavedigital = dados[parametro]['chavedigital']
        self.numeroemissor = dados[parametro]['numeroemissor']
        self.versaoxml = dados[parametro]['versaoxml']
        self.usanfemonitornfse = dados[parametro]['usanfemonitornfse']
        self.idlotenfse = dados[parametro]['idlotenfse']
        self.usadfemonitornfse = dados[parametro]['usadfemonitornfse']
        self.cancelarnfsest = dados[parametro]['cancelarnfsest']
        self.indarredondamentovaloriss = dados[parametro]['indarredondamentovaloriss']
        self.reducaoirrf = dados[parametro]['reducaoirrf']
        self.reducaoinss = dados[parametro]['reducaoinss']
        self.reducaocsll = dados[parametro]['reducaocsll']


class TGerCcParametro(Base):
    __tablename__ = 'TGERCCPARAMETRO'

    empresa = Column(String(2), primary_key=True, nullable=False)
    mascara = Column(String(20))
    graulancto = Column(Integer)
    usacc = Column(String(1), default='S', nullable=False)
    seq = Column(Integer)
    usacontarevisao = Column(String(1), default='N')
    contarevisao = Column(String(14))

    def __init__(self, parametro='TGERCCPARAMETRO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.mascara = dados[parametro]['mascara']
        self.graulancto = dados[parametro]['graulancto']
        self.usacc = dados[parametro]['usacc']
        self.seq = dados[parametro]['seq']
        self.usacontarevisao = dados[parametro]['usacontarevisao']
        self.contarevisao = dados[parametro]['contarevisao']


class TGerParametroCrystal(Base):
    __tablename__ = 'TGERPARAMETROCRYSTAL'

    codigo = Column(Integer, primary_key=True, nullable=False)
    relatorio = Column(Integer, primary_key=True, nullable=False)
    parametro = Column(String(100), nullable=False)
    descricao = Column(String(100), nullable=False)
    pesquisa = Column(String(100))

    def __init__(self, parametro='TGERPARAMETROCRYSTAL'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.codigo = dados[parametro]['codigo']
        self.relatorio = dados[parametro]['relatorio']
        self.parametro = dados[parametro]['parametro']
        self.descricao = dados[parametro]['descricao']
        self.pesquisa = dados[parametro]['pesquisa']


class TGerParametroImpressora(Base):
    __tablename__ = 'TGERPARAMETROIMPRESSORA'

    gid = Column(SmallInteger, primary_key=True, nullable=False)
    descricao = Column(String(100))
    id_relatorio = Column(Integer, nullable=False)
    parametro = Column(String(100), nullable=False)
    valor = Column(String(100))
    ip = Column(String(16))
    estacao = Column(String(100))
    usuario = Column(String(100))

    def __init__(self, parametro='TGERPARAMETROIMPRESSORA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.gid = dados[parametro]['gid']
        self.descricao = dados[parametro]['descricao']
        self.id_relatorio = dados[parametro]['id_relatorio']
        self.parametro = dados[parametro]['parametro']
        self.valor = dados[parametro]['valor']
        self.ip = dados[parametro]['ip']
        self.estacao = dados[parametro]['estacao']
        self.usuario = dados[parametro]['usuario']


class TImoParametro(Base):
    __tablename__ = 'TIMOPARAMETRO'
    
    empresa = Column(String(2))
    tipodocumento = Column(String(2), default='01')
    portador = Column(String(2), default='01')
    juros = Column(Numeric(6,4))
    diavencimento = Column(Integer)
    tipodocumentojuros = Column(String(2))
    tipodocumentoent = Column(String(2))
    gid = Column(BigInteger, primary_key=True, nullable=False)

    def __init__(self, parametro='TIMOPARAMETRO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.tipodocumento = dados[parametro]['tipodocumento']
        self.portador = dados[parametro]['portador']
        self.juros = dados[parametro]['juros']
        self.diavencimento = dados[parametro]['diavencimento']
        self.tipodocumentojuros = dados[parametro]['tipodocumentojuros']
        self.tipodocumentoent = dados[parametro]['tipodocumentoent']
        self.gid = dados[parametro]['gid']


class TImoParametroTabPrice(Base):
    __tablename__ = 'TIMOPARAMETROTABPRICE'

    empresa = Column(String(2), primary_key=True, nullable=False)
    qtdmeses = Column(Integer, primary_key=True, nullable=False)
    coeficiente = Column(Numeric(10,5), primary_key=True, nullable=False)

    def __init__(self, parametro='TIMOPARAMETROTABPRICE'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.qtdmeses = dados[parametro]['qtdmeses']
        self.coeficiente = dados[parametro]['coeficiente']


class TMadParametro(Base):
    __tablename__ = 'TMADPARAMETRO'

    empresa = Column(String(2), primary_key=True, nullable=False)
    usaromaneio = Column(String(1), default='N')
    editaromaneio = Column(String(1), default='N')
    imprimeromaneio = Column(String(1), default='N')
    editapauta = Column(String(1), default='N')
    alterapauta = Column(String(1), default='N')
    fundei = Column(Numeric(6,3), default=0)
    fethab = Column(Numeric(6,3), default=0)
    usuario = Column(String(15))

    def __init__(self, parametro='TMADPARAMETRO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.usaromaneio = dados[parametro]['usaromaneio']
        self.editaromaneio = dados[parametro]['editaromaneio']
        self.imprimeromaneio = dados[parametro]['imprimeromaneio']
        self.editapauta = dados[parametro]['editapauta']
        self.alterapauta = dados[parametro]['alterapauta']
        self.fundei = dados[parametro]['fundei']
        self.fethab = dados[parametro]['fethab']
        self.usuario = dados[parametro]['usuario']


class TOrdParametro(Base):
    __tablename__ = 'TORDPARAMETRO'

    empresa = Column(String(2), primary_key=True, nullable=False)
    veiculo = Column(String(1), default='N')
    motor = Column(String(1), default='N')
    eletro = Column(String(1), default='N')
    outros = Column(String(1), default='N')
    itemrepetido = Column(String(1), default='N')

    def __init__(self, parametro='TORDPARAMETRO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.veiculo = dados[parametro]['veiculo']
        self.motor = dados[parametro]['motor']
        self.eletro = dados[parametro]['eletro']
        self.outros = dados[parametro]['outros']
        self.itemrepetido = dados[parametro]['itemrepetido']


class TPagParametro(Base):
    __tablename__ = 'TPAGPARAMETRO'

    empresa = Column(String(2), primary_key=True, nullable=False)
    tipodocentrada = Column(String(2))
    idpagamento = Column(Integer)
    tipodocdevcheque = Column(String(2))
    tipodocrequisicao = Column(String(2))
    instrucaorequisicao = Column(String(120))
    idrequisicao = Column(Integer, default=0)
    idfornecedor = Column(String(5))
    unificapagamento = Column(String(1), default='N')
    idsequenciaparcela = Column(Integer, default=0)

    def __init__(self, parametro='TORDPARAMETRO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.tipodocentrada = dados[parametro]['tipodocentrada']
        self.idpagamento = dados[parametro]['idpagamento']
        self.tipodocdevcheque = dados[parametro]['tipodocdevcheque']
        self.tipodocrequisicao = dados[parametro]['tipodocrequisicao']
        self.instrucaorequisicao = dados[parametro]['instrucaorequisicao']
        self.idrequisicao = dados[parametro]['idrequisicao']
        self.idfornecedor = dados[parametro]['idfornecedor']
        self.unificapagamento = dados[parametro]['unificapagamento']
        self.idsequenciaparcela = dados[parametro]['idsequenciaparcela']


class TRecParametro(Base):
    __tablename__ = 'TRECPARAMETRO'

    empresa = Column(String(2), primary_key=True, nullable=False)
    controlacredito = Column(String(1), default='S')
    trabalhacomindice = Column(String(1), default='N')
    portadorpadrao = Column(String(2))
    tipodocboleto = Column(String(2))
    tipodocjuro = Column(String(2))
    tipodocvenda = Column(String(2))
    idbaixa = Column(Integer)
    multa = Column(Numeric(6, 4))
    juros = Column(Numeric(6, 4))
    desconto = Column(Numeric(6, 4))
    diamaxdesconto = Column(Integer, default=0)
    tipojuro = Column(String(1), default='C')
    idbaixach = Column(Integer, default=0)
    idboleto = Column(Integer, default=0)
    portadorvenda = Column(String(1), default='P')
    diasprotesto = Column(SmallInteger, default=0)
    formainstrucao = Column(String(1), default='P')
    impboletovenda = Column(String(1), default='N')
    impinstdesconto = Column(String(1), default='N')
    impinstjuros = Column(String(1), default='N')
    impinstmulta = Column(String(1), default='N')
    impinstprotesto = Column(String(1), default='N')
    instrucao = Column(String(200))
    idsequencia = Column(Integer, default=0)
    iddocumentojuro = Column(Integer, default=0)
    captalizajuro = Column(String(1), default='N')
    editajurocaptalizado = Column(String(1), default='N')
    recebimentounificado = Column(String(1))
    unificarecebimento = Column(String(1), default='N')
    atrasomaxpermitido = Column(Integer, default=0)
    motivobloqchdevproprio = Column(String(2))
    motivobloqchdevterceiro = Column(String(2))
    altvendedor = Column(String(1), default='N')
    permitecpfduplicado = Column(String(1), default='N')
    desbloqueioautomaticoch = Column(String(1), default='S')
    unificarecebimentocredito = Column(String(1))
    imppromisnolandoc = Column(String(1), default='N')
    aviso1 = Column(String(1000))
    usadiautil = Column(String(1), default='S')
    cadastrodesatualizado = Column(Integer, default=0)
    impautenticacao = Column(String(1), default='N')
    idcliente = Column(Integer, default=0)
    tipodoccartao1 = Column(String(2))
    tipodoccartao2 = Column(String(2))
    tipodoccartao3 = Column(String(2))

    def __init__(self, parametro='TRECPARAMETRO'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PARAMETRO.json')

        self.empresa = dados[parametro]['empresa']
        self.controlacredito = dados[parametro]['controlacredito']
        self.trabalhacomindice = dados[parametro]['trabalhacomindice']
        self.portadorpadrao = dados[parametro]['portadorpadrao']
        self.tipodocboleto = dados[parametro]['tipodocboleto']
        self.tipodocjuro = dados[parametro]['tipodocjuro']
        self.tipodocvenda = dados[parametro]['tipodocvenda']
        self.idbaixa = dados[parametro]['idbaixa']
        self.multa = dados[parametro]['multa']
        self.juros = dados[parametro]['juros']
        self.desconto = dados[parametro]['desconto']
        self.diamaxdesconto = dados[parametro]['diamaxdesconto']
        self.tipojuro = dados[parametro]['tipojuro']
        self.idbaixach = dados[parametro]['idbaixach']
        self.idboleto = dados[parametro]['idboleto']
        self.portadorvenda = dados[parametro]['portadorvenda']
        self.diasprotesto = dados[parametro]['diasprotesto']
        self.formainstrucao = dados[parametro]['formainstrucao']
        self.impboletovenda = dados[parametro]['impboletovenda']
        self.impinstdesconto = dados[parametro]['impinstdesconto']
        self.impinstjuros = dados[parametro]['impinstjuros']
        self.impinstmulta = dados[parametro]['impinstmulta']
        self.impinstprotesto = dados[parametro]['impinstprotesto']
        self.instrucao = dados[parametro]['instrucao']
        self.idsequencia = dados[parametro]['idsequencia']
        self.iddocumentojuro = dados[parametro]['iddocumentojuro']
        self.captalizajuro = dados[parametro]['captalizajuro']
        self.editajurocaptalizado = dados[parametro]['editajurocaptalizado']
        self.recebimentounificado = dados[parametro]['recebimentounificado']
        self.unificarecebimento = dados[parametro]['unificarecebimento']
        self.atrasomaxpermitido = dados[parametro]['atrasomaxpermitido']
        self.motivobloqchdevproprio = dados[parametro]['motivobloqchdevproprio']
        self.motivobloqchdevterceiro = dados[parametro]['motivobloqchdevterceiro']
        self.altvendedor = dados[parametro]['altvendedor']
        self.permitecpfduplicado = dados[parametro]['permitecpfduplicado']
        self.desbloqueioautomaticoch = dados[parametro]['desbloqueioautomaticoch']
        self.unificarecebimentocredito = dados[parametro]['unificarecebimentocredito']
        self.imppromisnolandoc = dados[parametro]['imppromisnolandoc']
        self.aviso1 = dados[parametro]['aviso1']
        self.usadiautil = dados[parametro]['usadiautil']
        self.cadastrodesatualizado = dados[parametro]['cadastrodesatualizado']
        self.impautenticacao = dados[parametro]['impautenticacao']
        self.idcliente = dados[parametro]['idcliente']
        self.tipodoccartao1 = dados[parametro]['tipodoccartao1']
        self.tipodoccartao2 = dados[parametro]['tipodoccartao2']
        self.tipodoccartao3 = dados[parametro]['tipodoccartao3']


class TVenParametro(Base):
    __tablename__ = 'TVENPARAMETRO'

    empresa = Column(String(2), primary_key=True, nullable=False)
    pedidoid = Column(Integer, default=0)
    idcomissao = Column(Integer, default=0)
    idcomissaoseq = Column(Integer, default=0)
    usaregistradora = Column(String(1), default='S')
    usadeptocrediario = Column(String(1), default='N')
    emitepedido = Column(String(1), default='N')
    emitecarne = Column(String(1), default='N')
    emitenotapromissoria = Column(String(1), default='N')
    emitecontrato = Column(String(1), default='N')
    emiteduplicata = Column(String(1), default='N')
    emiteboleto = Column(String(1), default='N')
    emitelistaseparacao = Column(String(1), default='N')
    emiterecibo = Column(String(1), default='N')
    emitenotafiscal = Column(String(1), default='N')
    idnotafiscal = Column(Integer, default=0)
    emitecupomfiscal = Column(String(1), default='N')
    emitecupomvinculado = Column(String(1), default='N')
    impnomecliente = Column(String(1), default='N')
    impenderecocliente = Column(String(1), default='N')
    impcidadecliente = Column(String(1), default='N')
    impcnpjcpfcliente = Column(String(1), default='N')
    impdocumentoorigem = Column(String(1), default='N')
    impparcelas = Column(String(1), default='N')
    impmensagem = Column(String(1), default='N')
    mensagem1 = Column(String(48))
    mensagem2 = Column(String(48))
    ecfvenda = Column(String(2))
    tipopedido = Column(String(1), default='N')
    percissqn = Column(Numeric(9,6), default=0)
    aplicaracrescimo = Column(String(1), default='V')
    condicaopadrao = Column(String(3))
    naturezapadrao = Column(String(3))
    requisicaoobrigatoria = Column(String(1), default='N')
    confirmaboleto = Column(String(1), default='N')
    confirmacarne = Column(String(1), default='N')
    confirmaduplicata = Column(String(1), default='N')
    confirmapromissoria = Column(String(1), default='N')
    confirmacontrato = Column(String(1), default='N')
    confirmapedido = Column(String(1), default='N')
    confirmaseparacao = Column(String(1), default='N')
    confirmarecibo = Column(String(1), default='N')
    editaprecoproduto = Column(String(1), default='N')
    canceladesbloqueio = Column(String(1), default='N')
    embutirfinanceiro = Column(String(1), default='N')
    idsangriasuprimento = Column(Integer, default=0)
    idclienteconsumidor = Column(String(5))
    vendedortransf = Column(String(3))
    tipodocumentotransf = Column(String(2))
    iddevolucao = Column(Integer, default=0)
    emitepedidorecibo = Column(String(1), default='N')
    confirmapedidorecibo = Column(String(1), default='N')
    imppromisnolandoc = Column(String(1), default='N')
    imprimeaposvenda = Column(String(1), default='N')
    boletonavenda = Column(String(1), default='N')
    carnenavenda = Column(String(1), default='N')
    duplicatanavenda = Column(String(1), default='N')
    promissorianavenda = Column(String(1), default='N')
    contratonavenda = Column(String(1), default='N')
    pedidonavenda = Column(String(1), default='N')
    recibonavenda = Column(String(1), default='N')
    listanavenda = Column(String(1), default='N')
    atacadoporvenda = Column(String(1), default='S')
    pagcomissaobaixa = Column(String(1), default='S')
    pdvvendedorpadrao = Column(String(3))
    pdvcondicaopadrao = Column(String(3))
    pdvnaturezapadrao = Column(String(3))
    trocadeoleodiretonavenda = Column(String(1))
    digitaprodfracqtde = Column(String(1), default='N')
    idliberacaovenda = Column(Integer, default=0)
    manterprecovenda = Column(String(1), default='N')
    apresentateladetalhes = Column(String(1), default='N')
    usaagentevendas = Column(String(1), default='N')
    maxdescbaixa = Column(Numeric(6,4), default=0.00)
    pesquisadiretaprodutos = Column(String(1), default='N')
    editaobservacaonota = Column(String(1), default='N')
    idnotafiscalservico = Column(Integer)
    imprimecheque = Column(String(1), default='N')
    ordempedido = Column(Integer)
    impmediaconsumo = Column(String(1))
    impcomprador = Column(String(1), default='N')
    idrecarga = Column(Integer)
    iditenspendentes = Column(Integer)
    idabastecimento = Column(Integer)
    emitesaidaregistradora = Column(String(1))
    confirmasaidaregistradora = Column(String(1))
    retencaominimairrf = Column(Numeric(18,2))
    retencaominimacsll = Column(Numeric(18,2))
    abaterirrfproduto = Column(SmallInteger)
    abatercsllproduto = Column(SmallInteger)
    emitecomprovanteentregafut = Column(String(1), default='N')
    confirmacomprovanteentregafut = Column(String(1), default='N')
    comprovanteentregafutnavenda = Column(String(1), default='N')