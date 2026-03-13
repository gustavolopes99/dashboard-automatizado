from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine.url import URL

#Cria conexão
_url = URL.create(drivername='firebird+fdb', username='SYSDBA', password='masterkey', host='127.0.0.1', port='3050', database='C:/ecosis/dados/ecodados.eco')
engine = create_engine(_url, echo=True)

#Cria instancia de sessão do banco para manipulação através da engine
Session = sessionmaker(bind=engine, autoflush=False)

#Cria objeto base para herança das classes
Base = declarative_base()

#Cria a sessão
Base.metadata.create_all(engine)
session = Session()


def verificar_conexao():
    _url = URL.create(drivername='firebird+fdb', username='SYSDBA', password='masterkey', host='127.0.0.1', port='3050', database='C:/ecosis/dados/ecodados.eco')
    engine = create_engine(_url, echo=True, pool_pre_ping=True)
    
def base_filial(caminho):
    #Fecha conexão da base ecodades.eco inicial
    #session.close()
        
    #Cria conexão
    _url = URL.create(drivername='firebird+fdb', username='SYSDBA', password='masterkey', host='127.0.0.1', port='3050', database='C:/ecosis/dados/ecodados.eco')
    engine = create_engine(_url, echo=True)

    #Cria instancia de sessão do banco para manipulação através da engine
    Session = sessionmaker(bind=engine, autoflush=False)

    #Cria objeto base para herança das classes
    Base = declarative_base()

    #Cria a sessão
    Base.metadata.create_all(engine)
    session = Session()
    
    return session