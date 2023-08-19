import flet as ft


#definir estilo para botão com função de icone


class IconButton(ft.UserControl):


    def __init__(self,icone = None, funcao = None):

        self.__funcao = funcao

        self.__desiner = ft.IconButton(
            icon= icone,
            on_click= self.__funcao
        )

    def build(self):
        return self.__desiner