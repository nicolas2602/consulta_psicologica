from Itens.TodoApp import *
import flet as ft

config_page={
    'color': ft.colors.BROWN_50,
    'width': 1250,
    'height':700,
    'min_height': 600,
    'min_width':1250,
    'title': "PsicoTech"
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
    app = TodoApp(page)

    # add application's root control to the page
    page.add(app.build())


ft.app(target=main)
#ft.app(target=main, view=ft.AppView.WEB_BROWSER)