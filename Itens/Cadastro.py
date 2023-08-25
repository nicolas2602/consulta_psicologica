import flet as ft
from Itens.Painel.Painel import Painel
from Itens.components.buttons.IconButton import IconButton
from Itens.Tabela.Tabela import Tabela

class Cadastro(ft.UserControl):
    def __init__(self, page):
        self.page = page

    def build(self):


        self.addCadastro = Painel(self.page,"Novo Cadastro").build()

        self.addBotao = IconButton(ft.icons.ADD, ft.colors.GREEN , self.openPainel).build()

        self.tabela = Tabela(self.page).build()


        #self.desiner = ft.IconButton(icon=ft.icons.ADD,on_click= self.openPainel)

        self.desiner = ft.Column(
            controls=[
                ft.Row([self.addBotao, ft.TextField(label='Pesquisar por nome'),ft.FilledButton(text='Pesquisar')],expand=False),
                ft.Divider(),
                self.tabela, 
            ],expand=True,horizontal_alignment= ft.CrossAxisAlignment.CENTER
        )



        return self.desiner
    
    def openPainel(self,e):
        self.page.dialog = self.addCadastro
        self.addCadastro.open = True
        self.page.update()