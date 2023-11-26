import flet as ft
from Itens.components.Titulo import Titulo
from Itens.Campo.Config.Sobre import Sobre
from Itens.Campo.Config.ConfigHoras import ConfigHoras
from Itens.Campo.Config.ConfigSenha import ConfigSenha
from Itens.Campo.Config.ConfigPagamento import ConfigPagamento

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
                    content=ConfigHoras(self.page).build()
                ),
            ),
            ft.Tab(
                text="Pagamentos",
                icon=ft.icons.MONETIZATION_ON,
                content=ConfigPagamento(self.page).build()
            ),
            ft.Tab(
                text="Senhas",
                icon=ft.icons.KEY,
                content= ConfigSenha(self.page).build()
            ),
            ft.Tab(
                text="Sobre",
                icon=ft.icons.INFO,
                content= Sobre().build()
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