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
from fordev.generators import people, company, state_registration
from unidecode import unidecode
from objects.OBJ_GER002CA import TGerCidade

class Cliente:
    def __init__(self, cliente='CLIENTE_PF', email=False):
        dados_adicionais = DadosAdicionais()
        global cpf_cnpj, rg_ie, rg_pr
        
        if 'PF' in cliente:
            cpf_cnpj = dados_adicionais.dados_cpfcnpj('F')
            rg_ie = dados_adicionais.dados_rgie('F')
            rg_pr = dados_adicionais.dados_rgpr('F')

            self.trecclientegeral = TRecClienteGeral(cliente)
            self.trecpfisica = TRecPFisica(cliente)
            self.treccliente = TRecCliente(cliente)
            
        elif 'PJ' in cliente:
            cpf_cnpj = dados_adicionais.dados_cpfcnpj('J')
            rg_ie = dados_adicionais.dados_rgie('J')
            rg_pr = dados_adicionais.dados_rgpr('J')
        
            self.trecclientegeral = TRecClienteGeral(cliente)
            self.trecpjuridica = TRecPJuridica(cliente)
            self.treccliente = TRecCliente(cliente)
            
        elif 'PR' in cliente:
            cpf_cnpj = dados_adicionais.dados_cpfcnpj('P')
            rg_ie = dados_adicionais.dados_rgie('P')
            rg_pr = dados_adicionais.dados_rgpr('P')
            
            self.trecclientegeral = TRecClienteGeral(cliente)
            self.trecpfisica = TRecPFisica(cliente)
            self.treccliente = TRecCliente(cliente)
            
        if email:
            self.tgeremail = TGerEmail(cliente)
            self.tgeremail.cpfcnpj = cpf_cnpj
        
class TRecClienteGeral(Base):
    
    __tablename__ = 'TRECCLIENTEGERAL'
    
    gid = Column(BigInteger)
    codigo = Column(String(5), primary_key=True, nullable=False)
    pessoa = Column(String(1), nullable=False)
    cpfcnpj = Column(String(14), nullable=False)
    rgie = Column(String(20), nullable=False)
    orgaoexpedidor = Column(String(12))
    rgpr = Column(String(20))
    nome = Column(String(50), nullable=False)
    fantasia = Column(String(50), nullable=False)
    endereco = Column(String(60), nullable=False)
    complemento = Column(String(30))
    bairro = Column(String(60), nullable=False)
    cidade = Column(String(4), nullable=False)
    cep = Column(String(8), nullable=False)
    caixapostal = Column(String(5))
    fone = Column(String(12))
    fax = Column(String(12))
    email = Column(String(50))
    homepage = Column(String(50))
    enderecocob = Column(String(60))
    complcobranca = Column(String(30))
    bairrocob = Column(String(60))
    cidadecob = Column(String(4))
    cepcob = Column(String(8))
    caixapostalcob = Column(String(5))
    portador = Column(String(2), nullable=False)
    atividade = Column(String(3), nullable=False)
    refban1 = Column(String(30))
    agrefban1 = Column(String(10))
    fonerefban1 = Column(String(12))
    refban2 = Column(String(30))
    agrefban2 = Column(String(10))
    fonerefban2 = Column(String(12))
    refban3 = Column(String(30))
    agrefban3 = Column(String(10))
    fonerefban3 = Column(String(12))
    bemimov1 = Column(String(15))
    localbemimov1 = Column(String(15))
    valorbemimov1 = Column(Numeric(18,2), default=0)
    bemimov2 = Column(String(15))
    localbemimov2 = Column(String(15))
    valorbemimov2 = Column(Numeric(18,2), default=0)
    bemimov3 = Column(String(15))
    localbemimov3 = Column(String(15))
    valorbemimov3 = Column(Numeric(18,2), default=0)
    bem1 = Column(String(15))
    tipobem1 = Column(String(15))
    valorbem1 = Column(Numeric(18,2), default=0)
    bem2 = Column(String(15))
    tipobem2 = Column(String(15))
    valorbem2 = Column(Numeric(18,2), default=0)
    bem3 = Column(String(15))
    tipobem3 = Column(String(15))
    valorbem3 = Column(Numeric(18,2), default=0)
    refcom1 = Column(String(40))
    fonerefcom1 = Column(String(12))
    refcom2 = Column(String(40))
    fonerefcom2 = Column(String(12))
    refcom3 = Column(String(40))
    fonerefcom3 = Column(String(12))
    areabemimov1 = Column(String(10))
    areabemimov2 = Column(String(10))
    areabemimov3 = Column(String(10))
    clientedesde = Column(Date, nullable=False)
    aprovadopor = Column(String(15), nullable=False)
    datacadastro = Column(Date, nullable=False)
    bloqueado = Column(String(1), default='N')
    usuario = Column(String(15), nullable=False)
    empresaconvenio = Column(String(5))
    convenenteconveniado = Column(String(1))
    conveniocancelado = Column(String(1), default='S')
    obsrefcom1 = Column(String(50))
    obsrefcom2 = Column(String(50))
    obsrefcom3 = Column(String(50))
    limite = Column(Numeric(18,2), default=0)
    limiteglobal = Column(String(1), default='N')
    venctolimite = Column(Date)
    concedidopor = Column(String(15))
    concedidoem = Column(Date)
    limiteant = Column(Numeric(18,2), default=0)
    venctolimiteant = Column(Date)
    concedidoemant = Column(Date)
    concedidoporant = Column(String(15))
    limiteconvenio = Column(Numeric(18,2))
    venctolimiteconv = Column(Date)
    concedidoporconv = Column(String(15))
    concedidoemconv = Column(Date)
    limiteantconv = Column(Numeric(18,2), default=0)
    venctolimiteantconv = Column(Date)
    concedidoemantconv = Column(Date)
    concedidoporantconv = Column(String(15))
    autorizaemail = Column(String(1), default='N')
    dataultimoenvio = Column(Date)
    ultatualizacaodata = Column(Date, default='TODAY')
    ultatualizacaousuario = Column(String(15))
    enviadocartaofidelidade = Column(String(1), default='N')
    tipoimovel = Column(String(1))
    melhordiarecebimento = Column(Integer)
    diretoriorequisicaotef = Column(String(100))
    diretoriorespostatef = Column(String(100))
    codigosuframa = Column(String(9))
    fonecelular = Column(String(12))
    obsnota = Column(String(256))
    substitutoissqn = Column(String(1))
    cartaofidelidade = Column(Integer)
    propriedaderural = Column(SmallInteger)
    identfidcliente = Column(String(16))
    isentoissqn = Column(String(1))
    supersimples = Column(String(1))
    codigocartao = Column(String(16))
    autorizado1 = Column(String(50))
    autorizado2 = Column(String(50))
    autorizado3 = Column(String(50))
    autorizado4 = Column(String(50))
    autorizado5 = Column(String(50))
    imprimeautorizados = Column(String(1))
    imprimetextospcserasa = Column(String(1))
    diavctoqualicard = Column(Integer)
    placa = Column(String(8))
    idcontrolenotebook = Column(BigInteger)
    idalteracaodebito = Column(Integer, default=0)
    contarefban1 = Column(String(10))
    contarefban2 = Column(String(10))
    contarefban3 = Column(String(10))
    bloqueiaplacanaocadastrada = Column(String(1), default='N')
    inscricaomunicipal = Column(String(15))
    datahoraalteracao = Column(DateTime, default='NOW')
    enviarordemcompra = Column(String(1), default='N')
    fidelidade = Column(String(1))
    numeroendereco = Column(String(10))
    numeroenderecocob = Column(String(10))
    idestrangeiro = Column(String(20))
    nirf = Column(String(10))
    nirf_old = Column(String(10))
    obs = Column(String(10000))
    obsfinanceira = Column(String(10000))
    textospcserasa = Column(String(10000))
    codigoibge = Column(Integer, default=0, nullable=False)
    codigoibgecob = Column(Integer, default=0, nullable=False)
    replicado = Column(SmallInteger, default=0, nullable=False)
    cpfcnpjconvenio = Column(String(14))
    nirfconvenio = Column(String(10), default='0000')
    bloqueiavendasemplaca = Column(String(1))
    substitutoirrf = Column(String(1))
    substitutocsll = Column(String(1))
    substitutoinss = Column(String(1))
    substitutopiscofins = Column(String(1))
    gidmeiopublic = Column(BigInteger)
    gidregiao = Column(BigInteger)
    gidtipocliente = Column(BigInteger)
    gid_endereco = Column(BigInteger)
    destinorevenda = Column(SmallInteger, default=0)
    destinoarmazenador = Column(SmallInteger, default=0)
    anvisa_ms_data_afe = Column(DateTime)
    anvisa_ms_data_ae = Column(DateTime)
    creditopresumido = Column(String(1), default='N')

    fk_trecpfisica = relationship('TRecPFisica', back_populates='fk_trecclientegeral')
    fk_trecpjuridica = relationship('TRecPJuridica', back_populates='fk_trecclientegeral')
    fk_treccliente = relationship('TRecCliente', back_populates='fk_trecclientegeral')
    
    def __init__(self, cliente_geral="CLIENTE_PF"):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC000CA.json')
        self.gid = self._buscar_proximo_gid_cliente()
        self.pessoa_gerada = people(uf_code='MT', formatting=False)[0]                
        self.codigo = self._buscar_proximo_codigo_cliente()
        self.pessoa = dados[cliente_geral]['TRECCLIENTEGERAL']['pessoa']
        self.cpfcnpj = cpf_cnpj
        self.rgie = rg_ie
        self.orgaoexpedidor = dados[cliente_geral]['TRECCLIENTEGERAL']['orgaoexpedidor']
        self.rgpr = rg_pr
        self.nome = str(unidecode(self.pessoa_gerada['nome'][:50])).upper()
        self.fantasia = str(unidecode(self.pessoa_gerada['nome'][:50])).upper()
        self.endereco = str(unidecode(self.pessoa_gerada['endereco'][:60])).upper()
        self.complemento = dados[cliente_geral]['TRECCLIENTEGERAL']['complemento']
        self.bairro = str(unidecode(self.pessoa_gerada['bairro'][:20])).upper()
        self.cidade = self._buscar_codigo_cidade_da_pessoa_gerada()
        self.cep = str(self.pessoa_gerada['cep'])
        self.caixapostal = dados[cliente_geral]['TRECCLIENTEGERAL']['caixapostal']
        self.fone = str(self.pessoa_gerada['telefone_fixo'])
        self.fax = dados[cliente_geral]['TRECCLIENTEGERAL']['fax']
        self.email = str(unidecode(self.pessoa_gerada['email'][:50]))
        self.homepage = dados[cliente_geral]['TRECCLIENTEGERAL']['homepage']
        self.enderecocob = str(unidecode(self.pessoa_gerada['endereco'][:60])).upper()
        self.complcobranca = dados[cliente_geral]['TRECCLIENTEGERAL']['complcobranca']
        self.bairrocob = str(unidecode(self.pessoa_gerada['bairro'][:60])).upper()
        self.cidadecob = self._buscar_codigo_cidade_da_pessoa_gerada()
        self.cepcob = str(self.pessoa_gerada['cep'])
        self.caixapostalcob = dados[cliente_geral]['TRECCLIENTEGERAL']['caixapostalcob']
        self.portador = dados[cliente_geral]['TRECCLIENTEGERAL']['portador']
        self.atividade = dados[cliente_geral]['TRECCLIENTEGERAL']['atividade']
        self.refban1 = dados[cliente_geral]['TRECCLIENTEGERAL']['refban1']
        self.agrefban1 = dados[cliente_geral]['TRECCLIENTEGERAL']['agrefban1']
        self.fonerefban1 = dados[cliente_geral]['TRECCLIENTEGERAL']['fonerefban1']
        self.refban2 = dados[cliente_geral]['TRECCLIENTEGERAL']['refban2']
        self.agrefban2 = dados[cliente_geral]['TRECCLIENTEGERAL']['agrefban2']
        self.fonerefban2 = dados[cliente_geral]['TRECCLIENTEGERAL']['fonerefban2']
        self.refban3 = dados[cliente_geral]['TRECCLIENTEGERAL']['refban3']
        self.agrefban3 = dados[cliente_geral]['TRECCLIENTEGERAL']['agrefban3']
        self.fonerefban3 = dados[cliente_geral]['TRECCLIENTEGERAL']['fonerefban3']
        self.bemimov1 = dados[cliente_geral]['TRECCLIENTEGERAL']['bemimov1']
        self.localbemimov1 = dados[cliente_geral]['TRECCLIENTEGERAL']['localbemimov1']
        self.valorbemimov1 = dados[cliente_geral]['TRECCLIENTEGERAL']['valorbemimov1']
        self.bemimov2 = dados[cliente_geral]['TRECCLIENTEGERAL']['bemimov2']
        self.localbemimov2 = dados[cliente_geral]['TRECCLIENTEGERAL']['localbemimov2']
        self.valorbemimov2 = dados[cliente_geral]['TRECCLIENTEGERAL']['valorbemimov2']
        self.bemimov3 = dados[cliente_geral]['TRECCLIENTEGERAL']['bemimov3']
        self.localbemimov3 = dados[cliente_geral]['TRECCLIENTEGERAL']['localbemimov3']
        self.valorbemimov3 = dados[cliente_geral]['TRECCLIENTEGERAL']['valorbemimov3']
        self.bem1 = dados[cliente_geral]['TRECCLIENTEGERAL']['bem1']
        self.tipobem1 = dados[cliente_geral]['TRECCLIENTEGERAL']['tipobem1']
        self.valorbem1 = dados[cliente_geral]['TRECCLIENTEGERAL']['valorbem1']
        self.bem2 = dados[cliente_geral]['TRECCLIENTEGERAL']['bem2']
        self.tipobem2 = dados[cliente_geral]['TRECCLIENTEGERAL']['tipobem2']
        self.valorbem2 = dados[cliente_geral]['TRECCLIENTEGERAL']['valorbem2']
        self.bem3 = dados[cliente_geral]['TRECCLIENTEGERAL']['bem3']
        self.tipobem3 = dados[cliente_geral]['TRECCLIENTEGERAL']['tipobem3']
        self.valorbem3 = dados[cliente_geral]['TRECCLIENTEGERAL']['valorbem3']
        self.refcom1 = dados[cliente_geral]['TRECCLIENTEGERAL']['refcom1']
        self.fonerefcom1 = dados[cliente_geral]['TRECCLIENTEGERAL']['fonerefcom1']
        self.refcom2 = dados[cliente_geral]['TRECCLIENTEGERAL']['refcom2']
        self.fonerefcom2 = dados[cliente_geral]['TRECCLIENTEGERAL']['fonerefcom2']
        self.refcom3 = dados[cliente_geral]['TRECCLIENTEGERAL']['refcom3']
        self.fonerefcom3 = dados[cliente_geral]['TRECCLIENTEGERAL']['fonerefcom3']
        self.areabemimov1 = dados[cliente_geral]['TRECCLIENTEGERAL']['areabemimov1']
        self.areabemimov2 = dados[cliente_geral]['TRECCLIENTEGERAL']['areabemimov2']
        self.areabemimov3 = dados[cliente_geral]['TRECCLIENTEGERAL']['areabemimov3']
        self.clientedesde = dados[cliente_geral]['TRECCLIENTEGERAL']['clientedesde']
        self.aprovadopor = dados[cliente_geral]['TRECCLIENTEGERAL']['aprovadopor']
        self.datacadastro = dados[cliente_geral]['TRECCLIENTEGERAL']['datacadastro']
        self.bloqueado = dados[cliente_geral]['TRECCLIENTEGERAL']['bloqueado']
        self.usuario = dados[cliente_geral]['TRECCLIENTEGERAL']['usuario']
        self.empresaconvenio = dados[cliente_geral]['TRECCLIENTEGERAL']['empresaconvenio']
        self.convenenteconveniado = dados[cliente_geral]['TRECCLIENTEGERAL']['convenenteconveniado']
        self.conveniocancelado = dados[cliente_geral]['TRECCLIENTEGERAL']['conveniocancelado']
        self.obsrefcom1 = dados[cliente_geral]['TRECCLIENTEGERAL']['obsrefcom1']
        self.obsrefcom2 = dados[cliente_geral]['TRECCLIENTEGERAL']['obsrefcom2']
        self.obsrefcom3 = dados[cliente_geral]['TRECCLIENTEGERAL']['obsrefcom3']
        self.limite = dados[cliente_geral]['TRECCLIENTEGERAL']['limite']
        self.limiteglobal = dados[cliente_geral]['TRECCLIENTEGERAL']['limiteglobal']
        self.venctolimite = dados[cliente_geral]['TRECCLIENTEGERAL']['venctolimite']
        self.concedidopor = dados[cliente_geral]['TRECCLIENTEGERAL']['concedidopor']
        self.concedidoem = dados[cliente_geral]['TRECCLIENTEGERAL']['concedidoem']
        self.limiteant = dados[cliente_geral]['TRECCLIENTEGERAL']['limiteant']
        self.venctolimiteant = dados[cliente_geral]['TRECCLIENTEGERAL']['venctolimiteant']
        self.concedidoemant = dados[cliente_geral]['TRECCLIENTEGERAL']['concedidoemant']
        self.concedidoporant = dados[cliente_geral]['TRECCLIENTEGERAL']['concedidoporant']
        self.limiteconvenio = dados[cliente_geral]['TRECCLIENTEGERAL']['limiteconvenio']
        self.venctolimiteconv = dados[cliente_geral]['TRECCLIENTEGERAL']['venctolimiteconv']
        self.concedidoporconv = dados[cliente_geral]['TRECCLIENTEGERAL']['concedidoporconv']
        self.concedidoemconv = dados[cliente_geral]['TRECCLIENTEGERAL']['concedidoemconv']
        self.limiteantconv = dados[cliente_geral]['TRECCLIENTEGERAL']['limiteantconv']
        self.venctolimiteantconv = dados[cliente_geral]['TRECCLIENTEGERAL']['venctolimiteantconv']
        self.concedidoemantconv = dados[cliente_geral]['TRECCLIENTEGERAL']['concedidoemantconv']
        self.concedidoporantconv = dados[cliente_geral]['TRECCLIENTEGERAL']['concedidoporantconv']
        self.autorizaemail = dados[cliente_geral]['TRECCLIENTEGERAL']['autorizaemail']
        self.dataultimoenvio = dados[cliente_geral]['TRECCLIENTEGERAL']['dataultimoenvio']
        self.ultatualizacaodata = dados[cliente_geral]['TRECCLIENTEGERAL']['ultatualizacaodata']
        self.ultatualizacaousuario = dados[cliente_geral]['TRECCLIENTEGERAL']['ultatualizacaousuario']
        self.enviadocartaofidelidade = dados[cliente_geral]['TRECCLIENTEGERAL']['enviadocartaofidelidade']
        self.tipoimovel = dados[cliente_geral]['TRECCLIENTEGERAL']['tipoimovel']
        self.melhordiarecebimento = dados[cliente_geral]['TRECCLIENTEGERAL']['melhordiarecebimento']
        self.diretoriorequisicaotef = dados[cliente_geral]['TRECCLIENTEGERAL']['diretoriorequisicaotef']
        self.diretoriorespostatef = dados[cliente_geral]['TRECCLIENTEGERAL']['diretoriorespostatef']
        self.codigosuframa = dados[cliente_geral]['TRECCLIENTEGERAL']['codigosuframa']
        self.fonecelular = dados[cliente_geral]['TRECCLIENTEGERAL']['fonecelular']
        self.obsnota = dados[cliente_geral]['TRECCLIENTEGERAL']['obsnota']
        self.substitutoissqn = dados[cliente_geral]['TRECCLIENTEGERAL']['substitutoissqn']
        self.cartaofidelidade = dados[cliente_geral]['TRECCLIENTEGERAL']['cartaofidelidade']
        self.propriedaderural = dados[cliente_geral]['TRECCLIENTEGERAL']['propriedaderural']
        self.identfidcliente = dados[cliente_geral]['TRECCLIENTEGERAL']['identfidcliente']
        self.isentoissqn = dados[cliente_geral]['TRECCLIENTEGERAL']['isentoissqn']
        self.supersimples = dados[cliente_geral]['TRECCLIENTEGERAL']['supersimples']
        self.codigocartao = dados[cliente_geral]['TRECCLIENTEGERAL']['codigocartao']
        self.autorizado1 = dados[cliente_geral]['TRECCLIENTEGERAL']['autorizado1']
        self.autorizado2 = dados[cliente_geral]['TRECCLIENTEGERAL']['autorizado2']
        self.autorizado3 = dados[cliente_geral]['TRECCLIENTEGERAL']['autorizado3']
        self.autorizado4 = dados[cliente_geral]['TRECCLIENTEGERAL']['autorizado4']
        self.autorizado5 = dados[cliente_geral]['TRECCLIENTEGERAL']['autorizado5']
        self.imprimeautorizados = dados[cliente_geral]['TRECCLIENTEGERAL']['imprimeautorizados']
        self.imprimetextospcserasa = dados[cliente_geral]['TRECCLIENTEGERAL']['imprimetextospcserasa']
        self.diavctoqualicard = dados[cliente_geral]['TRECCLIENTEGERAL']['diavctoqualicard']
        self.placa = dados[cliente_geral]['TRECCLIENTEGERAL']['placa']
        self.idcontrolenotebook = dados[cliente_geral]['TRECCLIENTEGERAL']['idcontrolenotebook']
        self.idalteracaodebito = dados[cliente_geral]['TRECCLIENTEGERAL']['idalteracaodebito']
        self.contarefban1 = dados[cliente_geral]['TRECCLIENTEGERAL']['contarefban1']
        self.contarefban2 = dados[cliente_geral]['TRECCLIENTEGERAL']['contarefban2']
        self.contarefban3 = dados[cliente_geral]['TRECCLIENTEGERAL']['contarefban3']
        self.bloqueiaplacanaocadastrada = dados[cliente_geral]['TRECCLIENTEGERAL']['bloqueiaplacanaocadastrada']
        self.inscricaomunicipal = dados[cliente_geral]['TRECCLIENTEGERAL']['inscricaomunicipal']
        self.datahoraalteracao = dados[cliente_geral]['TRECCLIENTEGERAL']['datahoraalteracao']
        self.enviarordemcompra = dados[cliente_geral]['TRECCLIENTEGERAL']['enviarordemcompra']
        self.fidelidade = dados[cliente_geral]['TRECCLIENTEGERAL']['fidelidade']
        self.numeroendereco = str(self.pessoa_gerada['numero'])
        self.numeroenderecocob = str(self.pessoa_gerada['numero'])
        self.idestrangeiro = dados[cliente_geral]['TRECCLIENTEGERAL']['idestrangeiro']
        self.nirf = dados[cliente_geral]['TRECCLIENTEGERAL']['nirf']
        self.nirf_old = dados[cliente_geral]['TRECCLIENTEGERAL']['nirf_old']
        self.obs = dados[cliente_geral]['TRECCLIENTEGERAL']['obs']
        self.obsfinanceira = dados[cliente_geral]['TRECCLIENTEGERAL']['obsfinanceira']
        self.textospcserasa = dados[cliente_geral]['TRECCLIENTEGERAL']['textospcserasa']
        self.codigoibge = dados[cliente_geral]['TRECCLIENTEGERAL']['codigoibge']
        self.codigoibgecob = dados[cliente_geral]['TRECCLIENTEGERAL']['codigoibgecob']
        self.replicado = dados[cliente_geral]['TRECCLIENTEGERAL']['replicado']
        self.cpfcnpjconvenio = dados[cliente_geral]['TRECCLIENTEGERAL']['cpfcnpjconvenio']
        self.nirfconvenio = dados[cliente_geral]['TRECCLIENTEGERAL']['nirfconvenio']
        self.bloqueiavendasemplaca = dados[cliente_geral]['TRECCLIENTEGERAL']['bloqueiavendasemplaca']
        self.substitutoirrf = dados[cliente_geral]['TRECCLIENTEGERAL']['substitutoirrf']
        self.substitutocsll = dados[cliente_geral]['TRECCLIENTEGERAL']['substitutocsll']
        self.substitutoinss = dados[cliente_geral]['TRECCLIENTEGERAL']['substitutoinss']
        self.substitutopiscofins = dados[cliente_geral]['TRECCLIENTEGERAL']['substitutopiscofins']
        self.gidmeiopublic = dados[cliente_geral]['TRECCLIENTEGERAL']['gidmeiopublic']
        self.gidregiao = dados[cliente_geral]['TRECCLIENTEGERAL']['gidregiao']
        self.gidtipocliente = dados[cliente_geral]['TRECCLIENTEGERAL']['gidtipocliente']
        self.gid_endereco = dados[cliente_geral]['TRECCLIENTEGERAL']['gid_endereco']
        self.destinorevenda = dados[cliente_geral]['TRECCLIENTEGERAL']['destinorevenda']
        self.destinoarmazenador = dados[cliente_geral]['TRECCLIENTEGERAL']['destinoarmazenador']
        self.anvisa_ms_data_afe = dados[cliente_geral]['TRECCLIENTEGERAL']['anvisa_ms_data_afe']
        self.anvisa_ms_data_ae = dados[cliente_geral]['TRECCLIENTEGERAL']['anvisa_ms_data_ae']
        self.creditopresumido = dados[cliente_geral]['TRECCLIENTEGERAL']['creditopresumido']

    def _buscar_proximo_codigo_cliente(self):               
        with engine.connect() as con:
            sequencia = con.execute(text("select MAX(codigo) from TRECCLIENTEGERAL where codigo < '88888'")).scalar()

        if sequencia is not None and sequencia.strip() != "":
            codigo_completo = str(int(sequencia) + 1)
        else:
            codigo_completo = '1'  

        return codigo_completo.zfill(5)
        

    def _buscar_proximo_gid_cliente(self):               
        codigo = session.query(func.max(TRecClienteGeral.gid)).first()
        
        if codigo[0]: 
            codigo = codigo[0] + 1
        else:
            codigo = 1

        return codigo
        
        
    def _buscar_codigo_cidade_da_pessoa_gerada(self):
        
        cidade = unidecode(self.pessoa_gerada['cidade'].upper())
        
        pesquisa_codigo = session.query(TGerCidade.codigo).filter(TGerCidade.nome == cidade, TGerCidade.estado == 'MT').first()
        
        while pesquisa_codigo is None:
            pessoa_gerada = people(uf_code='MT', formatting=False)[0]
            cidade_de_novo = unidecode(pessoa_gerada['cidade'].upper())
            pesquisa_codigo = session.query(TGerCidade.codigo).filter(TGerCidade.nome == cidade_de_novo, TGerCidade.estado == 'MT').first()
            if pesquisa_codigo:
                break
        return str(pesquisa_codigo[0])
        

class TRecPFisica(Base):

    __tablename__ = 'TRECPFISICA'

    codigo = Column(String(5), ForeignKey('TRECCLIENTEGERAL.codigo'), primary_key=True, nullable=False)
    datanasc = Column(Date)
    sexo = Column(String(1))
    estadocivil = Column(String(1))
    naturalidade = Column(String(20))
    ufnatural = Column(String(2))
    nomemae = Column(String(40))
    nomepai = Column(String(40))
    responsavel = Column(String(40))
    nomeconjuge = Column(String(40))
    cpfconjuge = Column(String(11))
    rgconjuge = Column(String(12))
    localtrabalho = Column(String(30))
    fonetrabalho = Column(String(12))
    cargo = Column(String(20))
    admissao = Column(Date)
    salario = Column(Numeric(18,2), default=0)
    contato = Column(String(20))
    refpessoal1 = Column(String(30))
    fonerefpessoal1 = Column(String(12))
    refpessoal2 = Column(String(30))
    fonerefpessoal2 = Column(String(12))
    refpessoal3 = Column(String(30))
    fonerefpessoal3 = Column(String(12))
    avalista1 = Column(String(40))
    rgaval1 = Column(String(12))
    cpfaval1 = Column(String(11))
    enderecoaval1 = Column(String(60))
    complaval1 = Column(String(30))
    bairroaval1 = Column(String(60))
    cidadeaval1 = Column(String(4))
    foneaval1 = Column(String(12))
    conjugeaval1 = Column(String(40))
    cpfconjugeaval1 = Column(String(11))
    rgconjugeaval1 = Column(String(12))
    avalista2 = Column(String(40))
    rgaval2 = Column(String(12))
    cpfaval2 = Column(String(11))
    enderecoaval2 = Column(String(60))
    complaval2 = Column(String(30))
    bairroaval2 = Column(String(60))
    cidadeaval2 = Column(String(4))
    foneaval2 = Column(String(12))
    conjugeaval2 = Column(String(40))
    cpfconjugeaval2 = Column(String(11))
    rgconjugeaval2 = Column(String(12))
    avalista3 = Column(String(40))
    rgaval3 = Column(String(12))
    cpfaval3 = Column(String(11))
    enderecoaval3 = Column(String(60))
    bairroaval3 = Column(String(60))
    cidadeaval3 = Column(String(4))
    foneaval3 = Column(String(12))
    conjugeaval3 = Column(String(40))
    cpfconjugeaval3 = Column(String(11))
    rgconjugeaval3 = Column(String(12))
    cepaval1 = Column(String(8))
    caixapostalaval1 = Column(String(5))
    emailaval1 = Column(String(50))
    cepaval2 = Column(String(8))
    caixapostalaval2 = Column(String(5))
    emailaval2 = Column(String(50))
    nomedep1 = Column(String(40))
    parentescodep1 = Column(String(15))
    dtnascdep1 = Column(Date)
    nomedep2 = Column(String(40))
    parentescodep2 = Column(String(15))
    dtnascdep2 = Column(Date)
    nomedep3 = Column(String(40))
    parentescodep3 = Column(String(15))
    dtnascdep3 = Column(Date)
    nomedep4 = Column(String(40))
    parentescodep4 = Column(String(15))
    dtnascdep4 = Column(Date)
    nomedep5 = Column(String(40))
    parentescodep5 = Column(String(15))
    dtnascdep5 = Column(Date)
    nomedep6 = Column(String(40))
    parentescodep6 = Column(String(15))
    dtnascdep6 = Column(Date)
    enderecolocaltrabalho = Column(String(60))
    localtrabalhoconj = Column(String(40))
    cargoconj = Column(String(20))
    fonetrabalhoconj = Column(String(12))
    salarioconj = Column(Numeric(18,2))
    tipoempresatrabalho = Column(SmallInteger)
    bairrotrabalho = Column(String(20))
    idcidadetrabalho = Column(String(4))
    complemento = Column(String(30))
    ceptrabalho = Column(String(8))
    outrasrendas = Column(String(100))
    valoroutrasrendas = Column(Numeric(18,2), default=0)
    datanascimentoconj = Column(Date)
    nomepaiconj = Column(String(40))
    nomemaeconj = Column(String(40))
    tipoempresatrabalhoconj = Column(SmallInteger)
    admissaoconj = Column(Date)
    enderecotrabalhoconj = Column(String(60))
    bairrotrabalhoconj = Column(String(20))
    idcidadetrabalhoconj = Column(String(4))
    complementotrabalhoconj = Column(String(30))
    ceptrabalhoconj = Column(String(8))
    origemoutrasrendasconj = Column(String(100))
    valoroutrasrendasconj = Column(Numeric(18,2), default=0)
    datahoraalteracao = Column(DateTime, default='NOW')
    nomemaeaval1 = Column(String(40))
    nomepaiaval1 = Column(String(40))
    datanascaval1 = Column(Date)
    nomemaeaval2 = Column(String(40))
    nomepaiaval2 = Column(String(40))
    datanascaval2 = Column(Date)
    cpfcnpj = Column(String(14), default='    ', nullable=False)
    nirf = Column(String(10), default='0000', nullable=False)
    replicado = Column(SmallInteger, default=0, nullable=False)

    fk_trecclientegeral = relationship('TRecClienteGeral', back_populates='fk_trecpfisica')

    def __init__(self, pessoa_fisica):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC000CA.json')

        self.codigo = self._buscar_proximo_codigo_cliente()
        self.datanasc = dados[pessoa_fisica]['TRECPFISICA']['datanasc']
        self.sexo = dados[pessoa_fisica]['TRECPFISICA']['sexo']
        self.estadocivil = dados[pessoa_fisica]['TRECPFISICA']['estadocivil']
        self.naturalidade = dados[pessoa_fisica]['TRECPFISICA']['naturalidade']
        self.ufnatural = dados[pessoa_fisica]['TRECPFISICA']['ufnatural']
        self.nomemae = dados[pessoa_fisica]['TRECPFISICA']['nomemae']
        self.nomepai = dados[pessoa_fisica]['TRECPFISICA']['nomepai']
        self.responsavel = dados[pessoa_fisica]['TRECPFISICA']['responsavel']
        self.nomeconjuge = dados[pessoa_fisica]['TRECPFISICA']['nomeconjuge']
        self.cpfconjuge = dados[pessoa_fisica]['TRECPFISICA']['cpfconjuge']
        self.rgconjuge = dados[pessoa_fisica]['TRECPFISICA']['rgconjuge']
        self.localtrabalho = dados[pessoa_fisica]['TRECPFISICA']['localtrabalho']
        self.fonetrabalho = dados[pessoa_fisica]['TRECPFISICA']['fonetrabalho']
        self.cargo = dados[pessoa_fisica]['TRECPFISICA']['cargo']
        self.admissao = dados[pessoa_fisica]['TRECPFISICA']['admissao']
        self.salario = dados[pessoa_fisica]['TRECPFISICA']['salario']
        self.contato = dados[pessoa_fisica]['TRECPFISICA']['contato']
        self.refpessoal1 = dados[pessoa_fisica]['TRECPFISICA']['refpessoal1']
        self.fonerefpessoal1 = dados[pessoa_fisica]['TRECPFISICA']['fonerefpessoal1']
        self.refpessoal2 = dados[pessoa_fisica]['TRECPFISICA']['refpessoal2']
        self.fonerefpessoal2 = dados[pessoa_fisica]['TRECPFISICA']['fonerefpessoal2']
        self.refpessoal3 = dados[pessoa_fisica]['TRECPFISICA']['refpessoal3']
        self.fonerefpessoal3 = dados[pessoa_fisica]['TRECPFISICA']['fonerefpessoal3']
        self.avalista1 = dados[pessoa_fisica]['TRECPFISICA']['avalista1']
        self.rgaval1 = dados[pessoa_fisica]['TRECPFISICA']['rgaval1']
        self.cpfaval1 = dados[pessoa_fisica]['TRECPFISICA']['cpfaval1']
        self.enderecoaval1 = dados[pessoa_fisica]['TRECPFISICA']['enderecoaval1']
        self.complaval1 = dados[pessoa_fisica]['TRECPFISICA']['complaval1']
        self.bairroaval1 = dados[pessoa_fisica]['TRECPFISICA']['bairroaval1']
        self.cidadeaval1 = dados[pessoa_fisica]['TRECPFISICA']['cidadeaval1']
        self.foneaval1 = dados[pessoa_fisica]['TRECPFISICA']['foneaval1']
        self.conjugeaval1 = dados[pessoa_fisica]['TRECPFISICA']['conjugeaval1']
        self.cpfconjugeaval1 = dados[pessoa_fisica]['TRECPFISICA']['cpfconjugeaval1']
        self.rgconjugeaval1 = dados[pessoa_fisica]['TRECPFISICA']['rgconjugeaval1']
        self.avalista2 = dados[pessoa_fisica]['TRECPFISICA']['avalista2']
        self.rgaval2 = dados[pessoa_fisica]['TRECPFISICA']['rgaval2']
        self.cpfaval2 = dados[pessoa_fisica]['TRECPFISICA']['cpfaval2']
        self.enderecoaval2 = dados[pessoa_fisica]['TRECPFISICA']['enderecoaval2']
        self.complaval2 = dados[pessoa_fisica]['TRECPFISICA']['complaval2']
        self.bairroaval2 = dados[pessoa_fisica]['TRECPFISICA']['bairroaval2']
        self.cidadeaval2 = dados[pessoa_fisica]['TRECPFISICA']['cidadeaval2']
        self.foneaval2 = dados[pessoa_fisica]['TRECPFISICA']['foneaval2']
        self.conjugeaval2 = dados[pessoa_fisica]['TRECPFISICA']['conjugeaval2']
        self.cpfconjugeaval2 = dados[pessoa_fisica]['TRECPFISICA']['cpfconjugeaval2']
        self.rgconjugeaval2 = dados[pessoa_fisica]['TRECPFISICA']['rgconjugeaval2']
        self.avalista3 = dados[pessoa_fisica]['TRECPFISICA']['avalista3']
        self.rgaval3 = dados[pessoa_fisica]['TRECPFISICA']['rgaval3']
        self.cpfaval3 = dados[pessoa_fisica]['TRECPFISICA']['cpfaval3']
        self.enderecoaval3 = dados[pessoa_fisica]['TRECPFISICA']['enderecoaval3']
        self.bairroaval3 = dados[pessoa_fisica]['TRECPFISICA']['bairroaval3']
        self.cidadeaval3 = dados[pessoa_fisica]['TRECPFISICA']['cidadeaval3']
        self.foneaval3 = dados[pessoa_fisica]['TRECPFISICA']['foneaval3']
        self.conjugeaval3 = dados[pessoa_fisica]['TRECPFISICA']['conjugeaval3']
        self.cpfconjugeaval3 = dados[pessoa_fisica]['TRECPFISICA']['cpfconjugeaval3']
        self.rgconjugeaval3 = dados[pessoa_fisica]['TRECPFISICA']['rgconjugeaval3']
        self.cepaval1 = dados[pessoa_fisica]['TRECPFISICA']['cepaval1']
        self.caixapostalaval1 = dados[pessoa_fisica]['TRECPFISICA']['caixapostalaval1']
        self.emailaval1 = dados[pessoa_fisica]['TRECPFISICA']['emailaval1']
        self.cepaval2 = dados[pessoa_fisica]['TRECPFISICA']['cepaval2']
        self.caixapostalaval2 = dados[pessoa_fisica]['TRECPFISICA']['caixapostalaval2']
        self.emailaval2 = dados[pessoa_fisica]['TRECPFISICA']['emailaval2']
        self.nomedep1 = dados[pessoa_fisica]['TRECPFISICA']['nomedep1']
        self.parentescodep1 = dados[pessoa_fisica]['TRECPFISICA']['parentescodep1']
        self.dtnascdep1 = dados[pessoa_fisica]['TRECPFISICA']['dtnascdep1']
        self.nomedep2 = dados[pessoa_fisica]['TRECPFISICA']['nomedep2']
        self.parentescodep2 = dados[pessoa_fisica]['TRECPFISICA']['parentescodep2']
        self.dtnascdep2 = dados[pessoa_fisica]['TRECPFISICA']['dtnascdep2']
        self.nomedep3 = dados[pessoa_fisica]['TRECPFISICA']['nomedep3']
        self.parentescodep3 = dados[pessoa_fisica]['TRECPFISICA']['parentescodep3']
        self.dtnascdep3 = dados[pessoa_fisica]['TRECPFISICA']['dtnascdep3']
        self.nomedep4 = dados[pessoa_fisica]['TRECPFISICA']['nomedep4']
        self.parentescodep4 = dados[pessoa_fisica]['TRECPFISICA']['parentescodep4']
        self.dtnascdep4 = dados[pessoa_fisica]['TRECPFISICA']['dtnascdep4']
        self.nomedep5 = dados[pessoa_fisica]['TRECPFISICA']['nomedep5']
        self.parentescodep5 = dados[pessoa_fisica]['TRECPFISICA']['parentescodep5']
        self.dtnascdep5 = dados[pessoa_fisica]['TRECPFISICA']['dtnascdep5']
        self.nomedep6 = dados[pessoa_fisica]['TRECPFISICA']['nomedep6']
        self.parentescodep6 = dados[pessoa_fisica]['TRECPFISICA']['parentescodep6']
        self.dtnascdep6 = dados[pessoa_fisica]['TRECPFISICA']['dtnascdep6']
        self.enderecolocaltrabalho = dados[pessoa_fisica]['TRECPFISICA']['enderecolocaltrabalho']
        self.localtrabalhoconj = dados[pessoa_fisica]['TRECPFISICA']['localtrabalhoconj']
        self.cargoconj = dados[pessoa_fisica]['TRECPFISICA']['cargoconj']
        self.fonetrabalhoconj = dados[pessoa_fisica]['TRECPFISICA']['fonetrabalhoconj']
        self.salarioconj = dados[pessoa_fisica]['TRECPFISICA']['salarioconj']
        self.tipoempresatrabalho = dados[pessoa_fisica]['TRECPFISICA']['tipoempresatrabalho']
        self.bairrotrabalho = dados[pessoa_fisica]['TRECPFISICA']['bairrotrabalho']
        self.idcidadetrabalho = dados[pessoa_fisica]['TRECPFISICA']['idcidadetrabalho']
        self.complemento = dados[pessoa_fisica]['TRECPFISICA']['complemento']
        self.ceptrabalho = dados[pessoa_fisica]['TRECPFISICA']['ceptrabalho']
        self.outrasrendas = dados[pessoa_fisica]['TRECPFISICA']['outrasrendas']
        self.valoroutrasrendas = dados[pessoa_fisica]['TRECPFISICA']['valoroutrasrendas']
        self.datanascimentoconj = dados[pessoa_fisica]['TRECPFISICA']['datanascimentoconj']
        self.nomepaiconj = dados[pessoa_fisica]['TRECPFISICA']['nomepaiconj']
        self.nomemaeconj = dados[pessoa_fisica]['TRECPFISICA']['nomemaeconj']
        self.tipoempresatrabalhoconj = dados[pessoa_fisica]['TRECPFISICA']['tipoempresatrabalhoconj']
        self.admissaoconj = dados[pessoa_fisica]['TRECPFISICA']['admissaoconj']
        self.enderecotrabalhoconj = dados[pessoa_fisica]['TRECPFISICA']['enderecotrabalhoconj']
        self.bairrotrabalhoconj = dados[pessoa_fisica]['TRECPFISICA']['bairrotrabalhoconj']
        self.idcidadetrabalhoconj = dados[pessoa_fisica]['TRECPFISICA']['idcidadetrabalhoconj']
        self.complementotrabalhoconj = dados[pessoa_fisica]['TRECPFISICA']['complementotrabalhoconj']
        self.ceptrabalhoconj = dados[pessoa_fisica]['TRECPFISICA']['ceptrabalhoconj']
        self.origemoutrasrendasconj = dados[pessoa_fisica]['TRECPFISICA']['origemoutrasrendasconj']
        self.valoroutrasrendasconj = dados[pessoa_fisica]['TRECPFISICA']['valoroutrasrendasconj']
        self.datahoraalteracao = dados[pessoa_fisica]['TRECPFISICA']['datahoraalteracao']
        self.nomemaeaval1 = dados[pessoa_fisica]['TRECPFISICA']['nomemaeaval1']
        self.nomepaiaval1 = dados[pessoa_fisica]['TRECPFISICA']['nomepaiaval1']
        self.datanascaval1 = dados[pessoa_fisica]['TRECPFISICA']['datanascaval1']
        self.nomemaeaval2 = dados[pessoa_fisica]['TRECPFISICA']['nomemaeaval2']
        self.nomepaiaval2 = dados[pessoa_fisica]['TRECPFISICA']['nomepaiaval2']
        self.datanascaval2 = dados[pessoa_fisica]['TRECPFISICA']['datanascaval2']
        self.cpfcnpj = cpf_cnpj
        self.nirf = dados[pessoa_fisica]['TRECPFISICA']['nirf']
        self.replicado = dados[pessoa_fisica]['TRECPFISICA']['replicado']

    def _buscar_proximo_codigo_cliente(self):
        with engine.connect() as con:
            sequencia = con.execute(text('select gen_id("GERSEQUENCE_CLIENTE", 0) FROM RDB$DATABASE')).fetchone()

        codigo_ultimo_cliente = sequencia[0]
        
        if codigo_ultimo_cliente: 
            codigo_completo = str(codigo_ultimo_cliente+1)
        else:
            codigo_completo = '1'  
                
        return codigo_completo.zfill(5)

class TRecPJuridica(Base):

    __tablename__ = 'TRECPJURIDICA'

    codigo = Column(String(5), ForeignKey('TRECCLIENTEGERAL.codigo'), primary_key=True, nullable=False)
    socio1 = Column(String(40))
    cpfsocio1 = Column(String(11))
    datanascsocio1 = Column(Date)
    socio2 = Column(String(40))
    cpfsocio2 = Column(String(11))
    datanascsocio2 = Column(Date)
    socio3 = Column(String(40))
    cpfsocio3 = Column(String(11))
    datanascsocio3 = Column(Date)
    socio4 = Column(String(40))
    cpfsocio4 = Column(String(11))
    datanascsocio4 = Column(Date)
    datafundacao = Column(Date)
    capitalsocial = Column(Numeric(18,2), default=0)
    faturamentobruto = Column(Numeric(18,2), default=0)
    regjuntacom = Column(String(12))
    endsocio1 = Column(String(60))
    rgsocio1 = Column(Integer)
    endsocio2 = Column(String(60))
    rgsocio2 = Column(Integer)
    endsocio3 = Column(String(60))
    rgsocio3 = Column(Integer)
    endsocio4 = Column(String(60))
    rgsocio4 = Column(Integer)
    datahoraalteracao = Column(DateTime, default='NOW')
    cpfcnpj = Column(String(14), default='    ', nullable=False)
    nirf = Column(String(10), default='0000', nullable=False)
    replicado = Column(SmallInteger, default=0, nullable=False)

    fk_trecclientegeral = relationship('TRecClienteGeral', back_populates='fk_trecpjuridica')

    def __init__(self, pessoa_juridica):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC000CA.json')

        self.codigo = self._buscar_proximo_codigo_cliente()
        self.socio1 = dados[pessoa_juridica]['TRECPJURIDICA']['socio1']
        self.cpfsocio1 = dados[pessoa_juridica]['TRECPJURIDICA']['cpfsocio1']
        self.datanascsocio1 = dados[pessoa_juridica]['TRECPJURIDICA']['datanascsocio1']
        self.socio2 = dados[pessoa_juridica]['TRECPJURIDICA']['socio2']
        self.cpfsocio2 = dados[pessoa_juridica]['TRECPJURIDICA']['cpfsocio2']
        self.datanascsocio2 = dados[pessoa_juridica]['TRECPJURIDICA']['datanascsocio2']
        self.socio3 = dados[pessoa_juridica]['TRECPJURIDICA']['socio3']
        self.cpfsocio3 = dados[pessoa_juridica]['TRECPJURIDICA']['cpfsocio3']
        self.datanascsocio3 = dados[pessoa_juridica]['TRECPJURIDICA']['datanascsocio3']
        self.socio4 = dados[pessoa_juridica]['TRECPJURIDICA']['socio4']
        self.cpfsocio4 = dados[pessoa_juridica]['TRECPJURIDICA']['cpfsocio4']
        self.datanascsocio4 = dados[pessoa_juridica]['TRECPJURIDICA']['datanascsocio4']
        self.datafundacao = dados[pessoa_juridica]['TRECPJURIDICA']['datafundacao']
        self.capitalsocial = dados[pessoa_juridica]['TRECPJURIDICA']['capitalsocial']
        self.faturamentobruto = dados[pessoa_juridica]['TRECPJURIDICA']['faturamentobruto']
        self.regjuntacom = dados[pessoa_juridica]['TRECPJURIDICA']['regjuntacom']
        self.endsocio1 = dados[pessoa_juridica]['TRECPJURIDICA']['endsocio1']
        self.rgsocio1 = dados[pessoa_juridica]['TRECPJURIDICA']['rgsocio1']
        self.endsocio2 = dados[pessoa_juridica]['TRECPJURIDICA']['endsocio2']
        self.rgsocio2 = dados[pessoa_juridica]['TRECPJURIDICA']['rgsocio2']
        self.endsocio3 = dados[pessoa_juridica]['TRECPJURIDICA']['endsocio3']
        self.rgsocio3 = dados[pessoa_juridica]['TRECPJURIDICA']['rgsocio3']
        self.endsocio4 = dados[pessoa_juridica]['TRECPJURIDICA']['endsocio4']
        self.rgsocio4 = dados[pessoa_juridica]['TRECPJURIDICA']['rgsocio4']
        self.datahoraalteracao = dados[pessoa_juridica]['TRECPJURIDICA']['datahoraalteracao']
        self.cpfcnpj = cpf_cnpj
        self.nirf = dados[pessoa_juridica]['TRECPJURIDICA']['nirf']
        self.replicado = dados[pessoa_juridica]['TRECPJURIDICA']['replicado']

    def _buscar_proximo_codigo_cliente(self):
        with engine.connect() as con:
            sequencia = con.execute(text("select MAX(codigo) from TRECPJURIDICA")).scalar()

        if sequencia is not None and sequencia.strip() != "":
            codigo_completo = str(int(sequencia) + 1)
        else:
            codigo_completo = '1'

        return codigo_completo.zfill(5)

class TRecCliente(Base):
    __tablename__ = "TRECCLIENTE"

    gid = Column(BigInteger, nullable=False)
    empresa = Column(String(2), primary_key=True, nullable=False)
    codigo = Column(String(5), ForeignKey('TRECCLIENTEGERAL.codigo'), primary_key=True, nullable=False)
    jurosatraso = Column(Numeric(18,4), default=0)
    acrescimoespecial = Column(Numeric(6,4), default=0)
    descontoespecial = Column(Numeric(6,4), default=0)
    atrasomaxpermitido = Column(Integer, default=0)
    compracrediario = Column(String(1), default='N')
    compracheque = Column(String(1), default='N')
    compraadministradora = Column(String(1))
    condpagtopadrao = Column(String(3))
    desconto = Column(Numeric(6,4), default=0)
    diamaxdesconto = Column(Integer, default=0)
    dataultcompra = Column(Date)
    vendedor = Column(String(3))
    geracomissao = Column(String(1))
    usuario = Column(String(15), nullable=False)
    valorultcompra = Column(Numeric(18,2))
    ultchequedata = Column(Date)
    ultchequevalor = Column(Numeric(18,2))
    maiorcompradata = Column(Date)
    maiorcompravalor = Column(Numeric(18,2))
    maiorchequedata = Column(Date)
    maiorchequevalor = Column(Numeric(18,2))
    maiorparceladata = Column(Date)
    maiorparcelavalor = Column(Numeric(18,2))
    pontualidade = Column(Integer)
    maiorprazodata = Column(Date)
    maiorprazo = Column(Integer)
    ativo = Column(String(1), default='S')
    compraconvenio = Column(String(1), default='N')
    ultimaativacao = Column(DateTime)
    ultimadesativacao = Column(DateTime)
    taxabancaria = Column(Numeric(10,3), default=0)
    senha = Column(String(32))
    temcartao = Column(String(1))
    cartaovalidado = Column(String(1))
    datavalidacao = Column(Date)
    datavalidade = Column(Date)
    dataprimeiracompra = Column(Date)
    valorprimeiracompra = Column(Numeric(18,2))
    diascarenciajuros = Column(SmallInteger, default=0)
    editadescontonopdv = Column(String(1), default='N')
    perctoleranciacartafrete = Column(Numeric(18,2), default=0)
    descontoproduto = Column(Numeric(12,2), default=0)
    descontoservico = Column(Numeric(12,2), default=0)
    programacao = Column(Date)
    contabanco = Column(String(2))
    tipovenda = Column(String(1), default='T')
    idtabelapreco = Column(Integer)
    mva = Column(Numeric(6,2), default=0)
    cargamedia = Column(Numeric(6,2), default=0)
    idalteracao = Column(Integer, default=0, nullable=False)
    idenviopaf = Column(Integer, default=0, nullable=False)
    idenviopafdebito = Column(Integer, default=0, nullable=False)
    idvinculotributario = Column(Integer)
    perccomissao = Column(Numeric(6,2))
    tipooperacao = Column(String(3))
    tributacaoespecialsc = Column(String(1), default='N')
    reidi = Column(String(1), default='N')
    datahoraalteracao = Column(DateTime, default='NOW')
    idvinculoicms = Column(Integer)
    cpfcnpj = Column(String(14), default='    ', nullable=False)
    nirf = Column(String(10), default='0000', nullable=False)
    replicado = Column(SmallInteger, default=0, nullable=False)
    agente = Column(String(3))
    idtabelaprecob2b = Column(BigInteger)

    fk_trecclientegeral = relationship('TRecClienteGeral', back_populates='fk_treccliente')

    def __init__(self, cliente):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC000CA.json')

        self.gid = self._buscar_proximo_gid_cliente()
        self.empresa = dados[cliente]['TRECCLIENTE']['empresa']
        self.codigo = self._buscar_proximo_codigo_cliente()
        self.jurosatraso = dados[cliente]['TRECCLIENTE']['jurosatraso']
        self.acrescimoespecial = dados[cliente]['TRECCLIENTE']['acrescimoespecial']
        self.descontoespecial = dados[cliente]['TRECCLIENTE']['descontoespecial']
        self.atrasomaxpermitido = dados[cliente]['TRECCLIENTE']['atrasomaxpermitido']
        self.compracrediario = dados[cliente]['TRECCLIENTE']['compracrediario']
        self.compracheque = dados[cliente]['TRECCLIENTE']['compracheque']
        self.compraadministradora = dados[cliente]['TRECCLIENTE']['compraadministradora']
        self.condpagtopadrao = dados[cliente]['TRECCLIENTE']['condpagtopadrao']
        self.desconto = dados[cliente]['TRECCLIENTE']['desconto']
        self.diamaxdesconto = dados[cliente]['TRECCLIENTE']['diamaxdesconto']
        self.dataultcompra = dados[cliente]['TRECCLIENTE']['dataultcompra']
        self.vendedor = dados[cliente]['TRECCLIENTE']['vendedor']
        self.geracomissao = dados[cliente]['TRECCLIENTE']['geracomissao']
        self.usuario = dados[cliente]['TRECCLIENTE']['usuario']
        self.valorultcompra = dados[cliente]['TRECCLIENTE']['valorultcompra']
        self.ultchequedata = dados[cliente]['TRECCLIENTE']['ultchequedata']
        self.ultchequevalor = dados[cliente]['TRECCLIENTE']['ultchequevalor']
        self.maiorcompradata = dados[cliente]['TRECCLIENTE']['maiorcompradata']
        self.maiorcompravalor = dados[cliente]['TRECCLIENTE']['maiorcompravalor']
        self.maiorchequedata = dados[cliente]['TRECCLIENTE']['maiorchequedata']
        self.maiorchequevalor = dados[cliente]['TRECCLIENTE']['maiorchequevalor']
        self.maiorparceladata = dados[cliente]['TRECCLIENTE']['maiorparceladata']
        self.maiorparcelavalor = dados[cliente]['TRECCLIENTE']['maiorparcelavalor']
        self.pontualidade = dados[cliente]['TRECCLIENTE']['pontualidade']
        self.maiorprazodata = dados[cliente]['TRECCLIENTE']['maiorprazodata']
        self.maiorprazo = dados[cliente]['TRECCLIENTE']['maiorprazo']
        self.ativo = dados[cliente]['TRECCLIENTE']['ativo']
        self.compraconvenio = dados[cliente]['TRECCLIENTE']['compraconvenio']
        self.ultimaativacao = dados[cliente]['TRECCLIENTE']['ultimaativacao']
        self.ultimadesativacao = dados[cliente]['TRECCLIENTE']['ultimadesativacao']
        self.taxabancaria = dados[cliente]['TRECCLIENTE']['taxabancaria']
        self.senha = dados[cliente]['TRECCLIENTE']['senha']
        self.temcartao = dados[cliente]['TRECCLIENTE']['temcartao']
        self.cartaovalidado = dados[cliente]['TRECCLIENTE']['cartaovalidado']
        self.datavalidacao = dados[cliente]['TRECCLIENTE']['datavalidacao']
        self.datavalidade = dados[cliente]['TRECCLIENTE']['datavalidade']
        self.dataprimeiracompra = dados[cliente]['TRECCLIENTE']['dataprimeiracompra']
        self.valorprimeiracompra = dados[cliente]['TRECCLIENTE']['valorprimeiracompra']
        self.diascarenciajuros = dados[cliente]['TRECCLIENTE']['diascarenciajuros']
        self.editadescontonopdv = dados[cliente]['TRECCLIENTE']['editadescontonopdv']
        self.perctoleranciacartafrete = dados[cliente]['TRECCLIENTE']['perctoleranciacartafrete']
        self.descontoproduto = dados[cliente]['TRECCLIENTE']['descontoproduto']
        self.descontoservico = dados[cliente]['TRECCLIENTE']['descontoservico']
        self.programacao = dados[cliente]['TRECCLIENTE']['programacao']
        self.contabanco = dados[cliente]['TRECCLIENTE']['contabanco']
        self.tipovenda = dados[cliente]['TRECCLIENTE']['tipovenda']
        self.idtabelapreco = dados[cliente]['TRECCLIENTE']['idtabelapreco']
        self.mva = dados[cliente]['TRECCLIENTE']['mva']
        self.cargamedia = dados[cliente]['TRECCLIENTE']['cargamedia']
        self.idalteracao = dados[cliente]['TRECCLIENTE']['idalteracao']
        self.idenviopaf = dados[cliente]['TRECCLIENTE']['idenviopaf']
        self.idenviopafdebito = dados[cliente]['TRECCLIENTE']['idenviopafdebito']
        self.idvinculotributario = dados[cliente]['TRECCLIENTE']['idvinculotributario']
        self.perccomissao = dados[cliente]['TRECCLIENTE']['perccomissao']
        self.tipooperacao = dados[cliente]['TRECCLIENTE']['tipooperacao']
        self.tributacaoespecialsc = dados[cliente]['TRECCLIENTE']['tributacaoespecialsc']
        self.reidi = dados[cliente]['TRECCLIENTE']['reidi']
        self.datahoraalteracao = dados[cliente]['TRECCLIENTE']['datahoraalteracao']
        self.idvinculoicms = dados[cliente]['TRECCLIENTE']['idvinculoicms']
        self.cpfcnpj = cpf_cnpj
        self.nirf = dados[cliente]['TRECCLIENTE']['nirf']
        self.replicado = dados[cliente]['TRECCLIENTE']['replicado']
        self.agente = dados[cliente]['TRECCLIENTE']['agente']
        self.idtabelaprecob2b = dados[cliente]['TRECCLIENTE']['idtabelaprecob2b']

    def _buscar_proximo_codigo_cliente(self):               
        with engine.connect() as con:
            sequencia = con.execute(text("select MAX(codigo) from TRECCLIENTE where codigo < '88888'")).scalar()

        if sequencia is not None and sequencia.strip() != "":
            codigo_completo = str(int(sequencia) + 1)
        else:
            codigo_completo = '1'  

        return codigo_completo.zfill(5)

    def _buscar_proximo_gid_cliente(self):
        codigo = session.query(func.max(TRecCliente.gid)).scalar()
        
        if codigo: 
            codigo = codigo + 1
        else:
            codigo = 1

        return codigo

        
class TGerEmail(Base):
    __tablename__ = "TGEREMAIL"
    
    idemail = Column(Integer, primary_key=True, nullable=False)
    cpfcnpj = Column(String(14), nullable=False)
    email = Column(String(100), nullable=False)
    nome = Column(String(50))
    todos = Column(SmallInteger)
    nfe = Column(SmallInteger)
    compras = Column(SmallInteger)
    vendas = Column(SmallInteger)
    boletos = Column(SmallInteger)
    financeiro = Column(SmallInteger)
    rh = Column(SmallInteger)
    dataalteracao = Column(Date)
    horaalteracao = Column(Time)
    enviaremailxml = Column(SmallInteger)
	
    def __init__(self, cliente):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_REC000CA.json')
        
        self.idemail = self._buscar_proximo_id_email()
        self.cpfcnpj = dados[cliente]['TGEREMAIL']['cpfcnpj']
        self.email = dados[cliente]['TGEREMAIL']['email']
        self.nome = dados[cliente]['TGEREMAIL']['nome']
        self.todos = dados[cliente]['TGEREMAIL']['todos']
        self.nfe = dados[cliente]['TGEREMAIL']['nfe']
        self.compras = dados[cliente]['TGEREMAIL']['compras']
        self.vendas = dados[cliente]['TGEREMAIL']['vendas']
        self.boletos = dados[cliente]['TGEREMAIL']['boletos']
        self.financeiro = dados[cliente]['TGEREMAIL']['financeiro']
        self.rh = dados[cliente]['TGEREMAIL']['rh']
        self.dataalteracao = dados[cliente]['TGEREMAIL']['dataalteracao']
        self.horaalteracao = dados[cliente]['TGEREMAIL']['horaalteracao']
        self.enviaremailxml = dados[cliente]['TGEREMAIL']['enviaremailxml']
        
    def _buscar_proximo_id_email(self):
        codigo = session.query(func.max(TGerEmail.idemail)).scalar()
        
        if codigo: 
            codigo = codigo + 1
        else:
            codigo = 1

        return codigo
        
        
class DadosAdicionais:
    def __init__(self):
        self.pessoa_gerada = people(uf_code='MT', formatting=False)[0]
        self.empresa = company(uf_code='MT', formatting=False)

    # Adiciona documentos aleatórios para as tabelas de TRECCLIENTE, TRECCLIENTEGERAL e TRECPFISICA/TRECPJURIDICA.
    def dados_cpfcnpj(self, pessoa):
        if pessoa == 'F':
            return self.pessoa_gerada['cpf']
        elif pessoa == 'J':
            return self.empresa['CNPJ']
        elif pessoa == 'P':
            return self.pessoa_gerada['cpf']
    
    def dados_rgie(self, pessoa):
        if pessoa == 'F':
            return self.pessoa_gerada['rg']
        elif pessoa == 'J':
            return self.empresa['Inscrição Estadual']
        elif pessoa == 'P':
            return self.empresa['Inscrição Estadual']

    def dados_rgpr(self, pessoa):
        if pessoa == 'P':
            return self.pessoa_gerada['rg']
        else:
            return ''

class TRecClienteVeiculo(Base):
    
    __tablename__ = 'TRECCLIENTEVEICULO'
    
    cliente = Column(String(5), ForeignKey('TRECCLIENTEGERAL.codigo'), nullable=False, primary_key=True)
    placa = Column(String(8), nullable=False, primary_key=True)
    tipoveiculo = Column(Integer, default=0, nullable=False)
    marca = Column(String(30))
    modelo = Column(String(40))
    ano = Column(String(4))
    cor = Column(String(20))
    combustivel = Column(Integer, default=0)
    idenviopaf = Column(Integer, default=0)
    idalteracao = Column(Integer, default=0)
    frota = Column(String(10))
    identfid = Column(String(16))
    datahoraalteracao = Column(DateTime, default='NOW')
    cpfcnpj = Column(String(14), default='    ', nullable=False)
    nirf = Column(String(20), default='0000', nullable=False)
    replicado = Column(Integer, default=0, nullable=False)