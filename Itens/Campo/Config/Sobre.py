import flet as ft

class Sobre(ft.UserControl):
    '''Campo Sobre na Configurações,
        contem informações sobre o Software e quem desenvolveu.
    '''
    def __init__(self):

        self.designer = ft.Container(
            content= ft.Column([
                ft.Icon(ft.icons.SELF_IMPROVEMENT_OUTLINED,color=ft.colors.GREEN_900,size=40),
                ft.Text("PsicoTech",style=ft.TextThemeStyle.TITLE_LARGE),
                ft.Text("Desenvolvido pelos alunos do 4º semestre de Sistemas de Informação, da Faculdade UNASP Hortolândia-SP - Ano 2023"),
                ft.Text("Integrantes:",style=ft.TextThemeStyle.TITLE_MEDIUM),
                ft.Text("Caio Gabriel"),
                ft.Text("Eduardo Silva"),
                ft.Text("Gabriel Martins"),
                ft.Text("Lucas Lima"),
                ft.Text("Nicolas Yonekawa"),
                ft.Text("Olivia Prestes"),
                ft.Text("Proteção de Dados Pessoais",style=ft.TextThemeStyle.TITLE_MEDIUM),
                ft.Text("Este aplicativo garante a proteção de seus dados pessoais conforme definido pela LGPD (Lei nº 13.709 de 14 de agosto de 2018)")
            ],horizontal_alignment="Center",alignment="Center"),
            bgcolor=ft.colors.GREY_100,
            width=320, height=530,expand=False,padding=15,
            border_radius = 10,
            border=ft.border.all(2,ft.colors.BLACK26)
        )

    def build(self):
        return ft.Column([ft.Divider(opacity=0),self.designer],spacing=10,expand=True,horizontal_alignment="Center",alignment="Center",scroll=ft.ScrollMode.ALWAYS)