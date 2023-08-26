import flet as ft
from Itens.Painel.Painel import Painel
from Itens.components.buttons.ActionButton import ActionButton
from Itens.Tabela.Tabela import Tabela
from Itens.Campo.CampoFormulario import CampoFormulario

class Cadastro(ft.UserControl):
    def __init__(self, page):
        self.page = page

    def build(self):


        self.addCadastro = Painel(self.page,"Novo Cadastro").build()

        self.addBotao = ActionButton('Adicionar',ft.colors.GREEN_800,ft.icons.ADD, self.openPainel).build()

        self.campoPesquisa = CampoFormulario("Pesquisa por nome")
        
        self.botaoPesquisa = ActionButton('Pesquisar', ft.colors.GREY_800 , ft.icons.SEARCH, self.getPesquisa).build()

        self.tabela = Tabela(self.page).build()


        #self.desiner = ft.IconButton(icon=ft.icons.ADD,on_click= self.openPainel)

        self.desiner = ft.Column(
            controls=[
                ft.Row([self.addBotao, self.campoPesquisa.build(), self.botaoPesquisa], alignment= ft.MainAxisAlignment.CENTER, spacing= 50),
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

    def getPesquisa(self,e):
        print(self.campoPesquisa.getValue())
        self.campoPesquisa.setValue()
        self.page.update()