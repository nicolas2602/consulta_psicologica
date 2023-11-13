import flet as ft
from Itens.Campo.Graficos.GraficosGanhoTotal import GraficosGanhoTotal
from Itens.Campo.Graficos.GraficosGanhoFuturos import GraficosGanhoFuturos
from Itens.Campo.Graficos.GraficosMediaGanhoMes import GraficosMediaGanhoMes
from Itens.Campo.Graficos.GraficosValorNaoPago import GraficosValorNaoPago
from Itens.Campo.Graficos.GraficosStatusMes import GraficosStatusMes
from Itens.Campo.Graficos.GraficosLinhas import GraficosLinhas
from Itens.Campo.Graficos.GraficosPizza import GraficosPizza
from modulos.DadosGraficos import DadosGraficos

class GraficosDashboard(ft.UserControl):
    def __init__(self,page):
        self.page = page

        self.dados = DadosGraficos()

        self.graf1 = GraficosGanhoTotal(self.page)
        self.graf2 = GraficosGanhoFuturos(self.page)
        self.graf3 = GraficosMediaGanhoMes(self.page)
        self.graf4 = GraficosValorNaoPago(self.page)
        self.graf5 = GraficosStatusMes(self.page)

        self.cabecalhoGrafico = ft.Row([self.graf1.build(),self.graf2.build(),self.graf3.build(),self.graf4.build()])

        self.grafLinhas = GraficosLinhas(self.page)
        self.grafPizza = GraficosPizza(self.page)

        self.grid = ft.Container(ft.Column([
            self.cabecalhoGrafico,     
            ft.Row([
                self.grafLinhas.build(),
                ft.Column([self.grafPizza.build(),self.graf5.build()])
            ])               
        ]),width=1150,height=620,padding=20,bgcolor="#007766",border_radius=ft.border_radius.all(10))


    def build(self):
        return ft.Column([self.grid],alignment="Center",scroll=ft.ScrollMode.ALWAYS)

    def setValue(self,ano):

        self.graf1.setValue(f"{ano}",f"{self.dados.totalAnoConcluido(ano)}")
        self.graf2.setValue(f"{ano}",f"{self.dados.totalAnoAndamento(ano)}")
        self.graf3.setValue(f"{self.dados.mediaAno(ano)}")
        self.graf4.setValue(f"{self.dados.totalAnoPendente(ano)}")
        self.graf5.setValue('junho', 'julho')
        self.grafLinhas.setValue(ano)
        self.grafPizza.setValue(ano)
        #self.page.update()