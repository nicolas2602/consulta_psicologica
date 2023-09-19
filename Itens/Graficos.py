import flet as ft
from Itens.Campo.CampoDrop import CampoDrop
from Itens.Campo.GraficosColunas import GraficosColunas
from Itens.components.Titulo import Titulo

class Graficos(ft.UserControl):
    def __init__(self):
        
        self.anos = CampoDrop('Anos',['2023'])
        self.anos.setValue('2023')

        self.graficos = GraficosColunas()

        self.designer = ft.Column(
            controls=[
                Titulo('Gráficos de Ganhos',ft.icons.QUERY_STATS).build(),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.anos.build()]),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.graficos.build()])
            ],expand=True
        )

    def build(self):
        return self.designer
