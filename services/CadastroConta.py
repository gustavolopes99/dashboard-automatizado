import sys
import os
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.ConfiguracoesBase import session, engine, Base
from objects.OBJ_BAN001CA import TBanAgencia
from objects.OBJ_BAN002CA import TBanConta

class CadastroConta:
    def __init__(self):
            self.agencia = TBanAgencia()
            self.conta = TBanConta()

            session.add(self.agencia)
            session.commit()
            session.add(self.conta)
            session.commit()

            print('Conta inserida no banco de dados')