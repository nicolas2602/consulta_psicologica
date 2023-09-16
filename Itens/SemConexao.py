import flet as ft
class SemConexao(ft.UserControl):

    '''Retorna o designer quando não à conexão com o Banco da Dados'''
    def __init__(self):

        self.designer = ft.Container(content=ft.Column([
            ft.Icon(ft.icons.CONSTRUCTION_SHARP,size=70),
            ft.Text("Sem Conexão com o servidor MySQL",style=ft.TextThemeStyle.LABEL_LARGE,size=30),
            ft.Text("Por favor, entrar em contato com o administrador",style=ft.TextThemeStyle.LABEL_LARGE)
        ],horizontal_alignment="Center",expand=True),
        bgcolor=ft.colors.ERROR_CONTAINER,
        border_radius=10,
        width=600,
        height=200,
        padding=20,
        )

    def build(self):
        return ft.Row(
            controls=[self.designer],
            alignment="Center",
            expand=True,
        )
        
        