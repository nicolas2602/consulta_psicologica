import flet as ft
from Itens.Campo.Graficos.GraficosGanhoTotal import GraficosGanhoTotal
from Itens.Campo.Graficos.GraficosGanhoFuturos import GraficosGanhoFuturos
from Itens.Campo.Graficos.GraficosMediaGanhoMes import GraficosMediaGanhoMes
from Itens.Campo.Graficos.GraficosValorNaoPago import GraficosValorNaoPago
from Itens.Campo.Graficos.GraficosStatusMes import GraficosStatusMes
from Itens.Campo.Graficos.GraficosLinhas import GraficosLinhas
from Itens.Campo.Graficos.GraficosPizza import GraficosPizza

class GraficosDashboard(ft.UserControl):
    def __init__(self):

        self.graf1 = GraficosGanhoTotal('10560.00','2023')
        self.graf2 = GraficosGanhoFuturos('2780.00','2023')
        self.graf3 = GraficosMediaGanhoMes('3580.00')
        self.graf4 = GraficosValorNaoPago('542.00')
        self.graf5 = GraficosStatusMes("Julho","Janeiro")

        self.cabecalhoGrafico = ft.Row([self.graf1.build(),self.graf2.build(),self.graf3.build(),self.graf4.build()])

        self.grafLinhas = GraficosLinhas('2023','2022')
        self.grafPizza = GraficosPizza()

        self.grid = ft.Container(ft.Column([
            self.cabecalhoGrafico,     
            ft.Row([
                self.grafLinhas.build(),
                ft.Column([self.grafPizza.build(),self.graf5.build()])
            ])               
        ]),width=1150,height=620,padding=20,bgcolor="#007766",border_radius=ft.border_radius.all(10))


    def build(self):
        return ft.Column([self.grid],alignment="Center",scroll=ft.ScrollMode.ALWAYS)