import flet as ft
from Itens.Campo.CampoDrop import CampoDrop
#from Itens.Campo.Graficos.GraficosColunas import GraficosColunas
from Itens.Tabela.GraficosDashboard import GraficosDashboard
from Itens.components.buttons.ActionButton import ActionButton
from Itens.components.Titulo import Titulo
from modulos.DadosGraficos import DadosGraficos

class Graficos(ft.UserControl):
    def __init__(self, page):

        self.page = page
        self.dados = DadosGraficos()
        
        self.anos = CampoDrop('Anos',self.listaAnos())
        self.botao = ActionButton("Selecionar",ft.colors.GREEN_800,ft.icons.PLAY_ARROW,funcao=self.setGrafico)
        #self.anos.setValue('2023')

        #self.graficos = GraficosColunas()

        self.graficos = GraficosDashboard(self.page)

        self.designer = ft.Column(
            controls=[
                Titulo('Gráficos de Ganhos',ft.icons.QUERY_STATS).build(),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.anos.build(),self.botao.build()]),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.graficos.build()],expand=True,alignment="Center",vertical_alignment=ft.CrossAxisAlignment.START)
            ],expand=True
        )

    def build(self):
        return self.designer

    def listaAnos(self):
        dados = self.dados.anos()
        lista = []

        for anos in dados:
            lista.append(anos[0])

        return lista
    
    def setGrafico(self,e):
        x = self.anos.getValue()
        if x is not None:
            self.graficos.setValue(x)