class ComponentesBAN004CA:
    def __init__(self, app):
        self.app = app
    
    @property
    def tela_movimentos(self):
        return self.app.window(title="Cadastro de movimentos", top_level_only=False)
    
    @property
    def bt_sair(self):
        return self.tela_movimentos.child_window(title="Sai&r", class_name="TBitBtn")
    
    @property
    def bt_cancelar(self):
        return self.tela_movimentos.child_window(title="C&ancelar", class_name="TBitBtn")
    
    @property
    def bt_confirmar(self):
        return self.tela_movimentos.child_window(title="&Confirmar", class_name="TBitBtn")