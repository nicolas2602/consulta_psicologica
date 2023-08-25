import flet as ft
from Itens.Painel.Painel import Painel
from Itens.components.buttons.IconButton import IconButton

class Cadastro(ft.UserControl):
    def __init__(self, page):
        self.page = page

    def build(self):


        self.addCadastro = Painel(self.page,"Novo Cadastro").build()

        self.addBotao = IconButton(ft.icons.ADD, ft.colors.GREEN , self.openPainel)

        self.addBotao.build()

        #self.desiner = ft.IconButton(icon=ft.icons.ADD,on_click= self.openPainel)

        return self.addBotao.build()  
    
    def openPainel(self,e):
        self.page.dialog = self.addCadastro
        self.addCadastro.open = True
        self.page.update()