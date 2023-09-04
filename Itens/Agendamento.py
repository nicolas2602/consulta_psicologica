import flet as ft
from time import sleep, strftime
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.components.buttons.ActionButton import ActionButton
from Itens.components.Carregamento import Carregamento


class Agendamento(ft.UserControl):
    ''' Janela do Campo MENU Agendamento Consultas.
        Aqui, há todo a criação de contrução do campo MENU Agendamento 
    '''

    def __init__(self, page):
        self.page = page

    def build(self):

        self.addBotao = ActionButton('Adicionar',ft.colors.GREEN_800,ft.icons.ADD).build()
        
        self.campoNome = CampoFormulario("Digite o nome:")
        
        self.campoData = CampoFormulario("Data",strftime("%d/%m/%Y"),120)
        
        self.botaoPesquisa = ActionButton('Pesquisar', ft.colors.GREY_800 , ft.icons.SEARCH).build()

        self.carregamento = Carregamento(self.page,"Salvando dados...")

        self.desiner = ft.Column(
            controls=[
                ft.Row([self.addBotao, self.campoNome.build(), self.campoData.build(), self.botaoPesquisa], alignment= ft.MainAxisAlignment.CENTER, spacing= 50),
                ft.Divider(color=ft.colors.GREEN_900),
                #ft.Row([self.tabela.build(),],vertical_alignment= ft.CrossAxisAlignment.START,expand=True) 
            ],
            expand=True,
        )
        return self.desiner
    

