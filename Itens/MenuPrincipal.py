import flet as ft
from Itens.components.buttons.MenuButon import MenuButon

class MenuPrincipal(ft.UserControl):
    def __init__(self, fCadastro, fConsultas, fAnotações, fPagamentos):

        self.__botao1 = MenuButon("Cadastro",ft.icons.PERSON, fCadastro)
        self.__botao2 = MenuButon("Consultas",ft.icons.CALENDAR_MONTH, fConsultas)
        self.__botao3 = MenuButon("Anotações",ft.icons.EDIT_DOCUMENT, fAnotações)
        self.__botao4 = MenuButon("Pagamentos",ft.icons.MONETIZATION_ON, fPagamentos)
        self.__desiner = ft.Column(
            [
                self.__botao1.build(),
                self.__botao2.build(),
                self.__botao3.build(),
                self.__botao4.build(),
            ],
            #alignment= ft.MainAxisAlignment.SPACE_EVENLY,
            expand=False
            
        )

    def build(self):
        return self.__desiner

