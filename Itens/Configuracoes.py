import flet as ft
from Itens.components.Titulo import Titulo

class Configuracoes(ft.UserControl):
    ''' Janela do Campo MENU Anotações Consultas.
        Aqui, há todo a criação de contrução do campo MENU Anotações 
    '''
    def __init__(self, page):
        self.page = page

        self.Tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Horários",
                icon=ft.icons.ACCESS_TIME,
                content=ft.Container(
                    content=ft.Column([ft.Icon(name=ft.icons.CONSTRUCTION, size= 200),ft.Text("Configurações... Em Desenvolvimento...",size=20)])
                ),
            ),
            ft.Tab(
                text="Pagamentos",
                icon=ft.icons.MONETIZATION_ON,
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Senhas",
                icon=ft.icons.KEY,
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                text="Sobre",
                icon=ft.icons.INFO,
                content=ft.Column([
                    ft.Text("PsicoTeck"),
                    ft.Text("Desenvolvido pelos alunos do 4º sementre de sistemas de Informação"),
                    ft.Text("Integrantes:"),
                    ft.Text("Caio"),
                    ft.Text("Eduardo"),
                    ft.Text("Gabriel"),
                    ft.Text("Lucas"),
                    ft.Text("Nicolas"),
                    ft.Text("Olivia"),
                    ])
            ),
        ],
        expand=1,
        )
        
        self.designer = ft.Column(
            controls=[
                Titulo('Configurações',ft.icons.SETTINGS).build(),
                ft.Divider(color=ft.colors.GREEN_900),
                self.Tabs,
            ],
            expand=True,
        )

    def build(self):
        return self.designer