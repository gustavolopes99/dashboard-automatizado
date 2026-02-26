import time

class AcessoEco:
    
    def __init__(self, app):
        self.app = app
    
    def login_eco(self, senha='eco123'):
        login_eco = self.app.top_window()
        login_eco.set_focus()
        login_eco.type_keys(senha + "{ENTER 2}", with_spaces=True)
    
    def acesso_tela(self, tela):
        principal_eco = self.app.top_window()
        principal_eco.set_focus()
        principal_eco.type_keys(f"^o")
        time.sleep(1)
        tela_busca = self.app.top_window()
        tela_busca.type_keys(tela + "{ENTER}", with_spaces=True)
        time.sleep(1)