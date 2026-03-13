import sys
import os
sys.path.append(r'C:\Fontes\sistemaEco\Certificacao\DashboardBDD')
from services.ConfiguracoesBase import session, engine, Base
from objects.OBJ_GER607RA import Autonomia
from objects.OBJ_GER624RA import TGerTipoBloqueioRemoto

class AplicacaoAutonomias:
    def __init__(self):
        self.liberar_autonomia('143')
        self.liberar_autonomia('144')
        self.liberar_autonomia('145')
        self.liberar_autonomia('146')

    def liberar_autonomia(self, numero):
        autonomia = Autonomia(numero)
        session.add(autonomia.tgerbloqueiousuario)
        session.commit()
        print(f"Autonomia {numero} liberada com sucesso! ✅")