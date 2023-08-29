import flet as ft

class IconButton(ft.UserControl):
    '''Botão Estilizado de Icone.'''
    
    def __init__(self,icone = None, corIcone = None, funcao = None):
        self.__desiner = ft.IconButton(
            icon= icone,
            on_click= funcao,
            icon_color = corIcone
        )

    def build(self):
        return self.__desiner