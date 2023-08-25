import flet as ft

class AddButton(ft.UserControl):

    def __init__(self, funcao = None):
        self.__desiner = ft.IconButton(
            icon= ft.icons.ADD,
            on_click= funcao,
            icon_color = ft.colors.WHITE,
            bgcolor= ft.colors.GREEN_700
        )

    def build(self):
        return self.__desiner