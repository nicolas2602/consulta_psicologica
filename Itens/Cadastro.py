import flet as ft
from Itens.Painel.Painel import Painel
from Itens.components.buttons.AddButton import AddButton
from Itens.Tabela.Tabela import Tabela
from Itens.Campo.CampoFormulario import CampoFormulario

class Cadastro(ft.UserControl):
    def __init__(self, page):
        self.page = page

    def build(self):


        self.addCadastro = Painel(self.page,"Novo Cadastro").build()

        self.addBotao = AddButton(self.openPainel).build()

        self.campoPesquisa = CampoFormulario("Pesquisa por nome")

        self.tabela = Tabela(self.page).build()


        #self.desiner = ft.IconButton(icon=ft.icons.ADD,on_click= self.openPainel)

        self.desiner = ft.Column(
            controls=[
                ft.Row([self.addBotao, self.campoPesquisa.build(), ft.FilledButton(text='Pesquisar')], alignment= ft.MainAxisAlignment.CENTER, spacing= 50),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.tabela,],vertical_alignment= ft.CrossAxisAlignment.START,expand=True) 
            ],
            expand=True,
        )

        return self.desiner
    
    def openPainel(self,e):
        self.page.dialog = self.addCadastro
        self.addCadastro.open = True
        self.page.update()