import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.components.buttons.ActionButton import ActionButton
from Itens.Campo.CampoDrop import CampoDrop
from Itens.Tabela.TabelaPagamento import TabelaPagamento
from Itens.components.Carregamento import Carregamento
from Itens.components.Titulo import Titulo
from time import sleep,strftime

class Pagamento(ft.UserControl):
    def __init__(self,page):
        
        self.page = page
        #"Pagamentos",ft.icons.MONETIZATION_ON,

        
    def build(self):

        self.campoNome = CampoFormulario("Digite o nome:")
        
        self.campoDataInicio = CampoFormulario("Data Inicial",strftime("%d/%m/%Y"),120)

        self.campoDataFinal = CampoFormulario("Data Final",strftime("%d/%m/%Y"),120)

        self.campoStatusPG = CampoDrop("Status",['Todos','Pago','Não Pago', 'Em Andamento'],160)
        self.campoStatusPG.setValue('Todos')

        self.botaoPesquisa = ActionButton('Pesquisar', ft.colors.GREY_800 , ft.icons.SEARCH).build()

        self.tabela = TabelaPagamento(self.page)

        self.designer = ft.Column(
            controls=[
                Titulo('Pagamentos',ft.icons.MONETIZATION_ON).build(),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.campoNome.build(), self.campoDataInicio.build(), self.campoDataFinal.build(), self.campoStatusPG.build(), self.botaoPesquisa], alignment= ft.MainAxisAlignment.CENTER, spacing= 15),
                ft.Divider(color=ft.colors.GREEN_900),

                ft.Row([self.tabela.build(),],vertical_alignment= ft.CrossAxisAlignment.START,expand=True),
                
                ft.Column([ft.Icon(name=ft.icons.CONSTRUCTION, size= 200),ft.Text("Pagamentos... Em Desenvolvimento...",size=20)])
                 
            ],
            expand=True,
        )

   
        return self.designer