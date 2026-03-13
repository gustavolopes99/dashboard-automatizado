from services.FA_ManipulacaoDeArquivos import ler_json
from sqlalchemy import (Column, String, Integer, Date, Numeric, ForeignKey, SmallInteger, DateTime, Boolean, BigInteger, Time)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func, text
from datetime import date
import sys
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.ConfiguracoesBase import Base, engine, session
from fordev.generators import people, company
from unidecode import unidecode

class Fornecedor:
    def __init__(self, fornecedor='TPAGFORNECEDOR'):
        self.tpagfornecedor = TPagFornecedor(fornecedor)
        self.tpagfornecedoriest = TPagFornecedorIEST()
        self.tpagreferenciabancaria = TPagReferenciaBancaria()

        self.tpagfornecedoriest.fk_codfornecedor = self.tpagfornecedor
        self.tpagreferenciabancaria.fk_fornecedor = self.tpagfornecedor
        
class TPagFornecedor(Base):
    __tablename__ = 'TPAGFORNECEDOR'
    
    codigo = Column(String(5), primary_key=True, nullable=False)
    nome = Column(String(40), nullable=False)
    fantasia = Column(String(40), nullable=False)
    pessoa = Column(String(1), nullable=False)
    cpfcnpj = Column(String(14), nullable=False)
    rgie = Column(String(20))
    orgaoexpedidor = Column(String(12))
    endereco = Column(String(60), nullable=False)
    complemento = Column(String(30))
    bairro = Column(String(60), nullable=False)
    cidade = Column(String(4), nullable=False)
    cep = Column(String(11), nullable=False)
    caixapostal = Column(String(5), nullable=False)
    fone = Column(String(12), nullable=False)
    fax = Column(String(12), nullable=False)
    homepage = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    contato = Column(String(30), nullable=False)
    fonecontato = Column(String(12), nullable=False)
    taxanegcheque = Column(Numeric(6,2), nullable=False)
    nomevendedor = Column(String(50))
    fonecomervend = Column(String(12))
    foneresidvend = Column(String(12))
    celularvend = Column(String(12))
    emailvend = Column(String(50))
    fonetelevendas = Column(String(12))
    codtelevendas = Column(String(15))
    datacadastro = Column(Date, nullable=False)
    usuario = Column(String(15), nullable=False)
    observacao = Column(String(80))
    ativo = Column(String(1), default='S', nullable=False)
    factoring = Column(String(1), default='N')
    pedidoonline = Column(String(6))
    produtorrural = Column(String(1), default='N')
    idvinculotributario = Column(SmallInteger)
    codigocrt = Column(Integer)
    numeroendereco = Column(String(10))
    idestrangeiro = Column(String(20))
    datahoraalteracao = Column(DateTime)
    contribuinte = Column(String(1), default='N')
    obs = Column(String(10000))
    armazenadororigem = Column(String(1), default='N')
    
    def __init__(self, fornecedor):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PAG000CA.json')
        pessoa_gerada = False
        while isinstance(pessoa_gerada, dict) == False:
            pessoa_gerada = company(state='MT', formatting=False)
        
        self.codigo = self._buscar_proximo_codigo_fornecedor()
        self.nome = unidecode(pessoa_gerada['Nome'][:40]).upper()
        self.fantasia = self.nome
        self.pessoa = dados[fornecedor]['pessoa']
        self.cpfcnpj = pessoa_gerada['CNPJ'] 
        self.rgie = pessoa_gerada['Inscrição Estadual']
        self.orgaoexpedidor = dados[fornecedor]['orgaoexpedidor']
        self.endereco = unidecode(pessoa_gerada['Endereço'][:60])
        self.complemento = dados[fornecedor]['complemento']
        self.bairro = unidecode(pessoa_gerada['Bairro'][:60])
        self.cidade = dados[fornecedor]['cidade']
        self.cep = dados[fornecedor]['cep']
        self.caixapostal = dados[fornecedor]['caixapostal']
        self.fone = pessoa_gerada['Telefone']
        self.fax = dados[fornecedor]['fax']
        self.homepage = dados[fornecedor]['homepage']
        self.email = dados[fornecedor]['email']
        self.contato = dados[fornecedor]['contato']
        self.fonecontato = pessoa_gerada['Celular']
        self.taxanegcheque = dados[fornecedor]['taxanegcheque']
        self.nomevendedor = dados[fornecedor]['nomevendedor']
        self.fonecomervend = dados[fornecedor]['fonecomervend']
        self.foneresidvend = dados[fornecedor]['foneresidvend']
        self.celularvend = dados[fornecedor]['celularvend']
        self.emailvend = dados[fornecedor]['emailvend']
        self.fonetelevendas = dados[fornecedor]['fonetelevendas']
        self.codtelevendas = dados[fornecedor]['codtelevendas']
        self.datacadastro = dados[fornecedor]['datacadastro']
        self.usuario = dados[fornecedor]['usuario']
        self.observacao = dados[fornecedor]['observacao']
        self.ativo = dados[fornecedor]['ativo']
        self.factoring = dados[fornecedor]['factoring']
        self.pedidoonline = dados[fornecedor]['pedidoonline']
        self.produtorrural = dados[fornecedor]['produtorrural']
        self.idvinculotributario = dados[fornecedor]['idvinculotributario']
        self.codigocrt = dados[fornecedor]['codigocrt']
        self.numeroendereco = pessoa_gerada['Número']
        self.idestrangeiro = dados[fornecedor]['idestrangeiro']
        self.datahoraalteracao = dados[fornecedor]['datahoraalteracao']
        self.contribuinte = dados[fornecedor]['contribuinte']
        self.obs = dados[fornecedor]['obs']
        self.armazenadororigem = dados[fornecedor]['armazenadororigem']
        
    def _buscar_proximo_codigo_fornecedor(self):
        code = ''
        with engine.connect() as con:
            code = con.execute(text('SELECT MAX(Codigo) AS Codigo FROM TPagFornecedor;')).fetchall()
            
        if code[0][0]:
            codigo = int(code[0][0])
            codigo += 1
        else:
            codigo = 1
         
        return str(codigo).zfill(5)

class TPagFornecedorIEST(Base):
    __tablename__ = 'TPAGFORNECEDORIEST'

    gid = Column(BigInteger, primary_key=True, nullable=False)
    codfornecedor = Column(String(5), ForeignKey('TPAGFORNECEDOR.codigo'))
    uf = Column(String(2))
    iest = Column(String(14))

    fk_codfornecedor = relationship('TPagFornecedor', foreign_keys='TPagFornecedorIEST.codfornecedor')

    def __init__(self, iest='TPAGFORNECEDORIEST'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PAG006CA.json')
        
        self.gid = self._buscar_proximo_codigo_iest()
        self.codfornecedor = dados[iest]['codfornecedor']
        self.uf = dados[iest]['uf']
        self.iest = dados[iest]['iest']

    def _buscar_proximo_codigo_iest(self):             
        codigo = session.query(func.max(TPagFornecedorIEST.gid)).first()

        if codigo[0]: 
            codigo = codigo[0]+1
        else:
            codigo = 1

        return codigo

class TPagReferenciaBancaria(Base):

    __tablename__ = 'TPAGREFERENCIABANCARIA'

    codigo = Column(Integer, primary_key=True, nullable=False)
    fornecedor = Column(String(5), ForeignKey('TPAGFORNECEDOR.codigo'), nullable=False)
    banco = Column(String(3), nullable=False)
    agencia = Column(String(10), nullable=False)
    contacorrente = Column(String(15), nullable=False)
    fone = Column(String(12))

    fk_fornecedor = relationship('TPagFornecedor', foreign_keys='TPagReferenciaBancaria.fornecedor')

    def __init__(self, referencia='TPAGREFERENCIABANCARIA'):
        dados = ler_json('C:\\Fontes\\sistemaEco\\Certificacao\\DashboardBDD\\data\\MA_PAG000CB.json')

        self.codigo = self._buscar_proximo_codigo_banco()
        self.fornecedor = dados[referencia]['fornecedor']
        self.banco = dados[referencia]['banco']
        self.agencia = dados[referencia]['agencia']
        self.contacorrente = dados[referencia]['contacorrente']
        self.fone = dados[referencia]['fone']

    def _buscar_proximo_codigo_banco(self):        
        codigo = session.query(func.max(TPagReferenciaBancaria.codigo)).first()

        if codigo[0]: 
            codigo = codigo[0]+1
        else:
            codigo = 1

        return codigo