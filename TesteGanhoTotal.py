from Itens.Campo.Graficos.GraficosGanhoTotal import GraficosGanhoTotal
from Itens.Campo.Graficos.GraficosGanhoFuturos import GraficosGanhoFuturos
from Itens.Campo.Graficos.GraficosMediaGanhoMes import GraficosMediaGanhoMes
from Itens.Campo.Graficos.GraficosValorNaoPago import GraficosValorNaoPago
from Itens.Campo.Graficos.GraficosStatusMes import GraficosStatusMes
from Itens.Campo.Graficos.GraficosLinhas import GraficosLinhas
from Itens.Campo.Graficos.GraficosPizza import GraficosPizza
import flet as ft

config_page={
    'color': ft.colors.BROWN_50,
    'width': 1250,
    'height':700,
    'min_height': 600,
    'min_width':1250,
    'title': "PsicoTeck"
}


def main(page: ft.Page):
    
    # Configuração da pagina
    page.theme_mode = ft.ThemeMode("light")
    page.window_height = config_page['height']
    page.window_width = config_page['width']
    page.window_min_height = config_page['min_height']
    page.window_min_width = config_page['min_width']
    page.title = config_page['title']
    page.update()

    # create application instance
    app1 = GraficosGanhoTotal('10560.00','2023')
    app2 = GraficosGanhoFuturos('2780.00','2023')
    app3 = GraficosMediaGanhoMes('3580.00')
    app4 = GraficosValorNaoPago('542.00')
    app5 = GraficosStatusMes("Julho","Janeiro")

    app = ft.Row([app1.build(),app2.build(),app3.build(),app4.build()])
    

    graf1 = GraficosLinhas('2023','2022')
    graf2 = GraficosPizza()

    graf3 = ft.Column([graf2.build(),app5.build()])

    graf = ft.Row([graf1.build(),graf3])

    # add application's root control to the page
    page.add(ft.Column([app,graf]))


ft.app(target=main)
#ft.app(target=main, view=ft.AppView.WEB_BROWSER)