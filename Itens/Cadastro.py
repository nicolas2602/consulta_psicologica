import flet as ft
from Itens.Painel.Painel import Painel
from Itens.components.buttons.IconButton import IconButton

class Cadastro(ft.UserControl):

    def build(self):


        self.addCadastro = Painel(self, "Novo Cadastro")
        self.addBotao = IconButton(ft.icons.ADD, self.addCadastro.openPainel)

        self.desiner = self.addBotao.build()

        return self.desiner  