class ComponentesCXA000CA: # Pywinauto
    def __init__(self, app):
        self.app = app
        self.tela = app.window(title="Cadastro de caixas", class_name='TFCXA000CA', top_level_only=False)
        self.eb_caixa = self.tela.Edit4
        self.eb_descricao = self.tela.Edit2
        self.ch_ativo = self.tela.child_window(title="Ativo", class_name="TCheckBox")
        self.bt_confirmar = self.tela.child_window(title="&Confirmar", class_name="TBitBtn")
        self.bt_cancelar = self.tela.child_window(title="C&ancelar", class_name="TBitBtn")
        self.bt_sair = self.tela.child_window(title="Sai&r", class_name="TBitBtn")

    @property
    def bt_novo(self):
        return self.tela.type_keys('%n')
    @property
    def bt_editar(self):
        return self.tela.type_keys('%e')
    @property
    def bt_consultar(self):
        return self.tela.type_keys('%o')
    @property
    def bt_excluir(self):
        return self.tela.type_keys('%x')