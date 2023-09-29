import flet as ft

class ActionButton(ft.UserControl):
    '''Botão Estilizado para um tipo de ação, EX: Botão de Cancelar, botão de ok e Etc...'''

    def __init__(self,texto = None,cor = None,icon = None,funcao = None):
        
        self.__desiner = ft.OutlinedButton(
            text= texto,
            icon= icon,
            icon_color = ft.colors.WHITE,
            on_click= funcao,
            style= ft.ButtonStyle(
                    color= {
                        ft.MaterialState.DEFAULT: ft.colors.WHITE,
                    },
                    bgcolor= {
                        ft.MaterialState.DEFAULT: cor,
                        ft.MaterialState.HOVERED: cor,
                    },
                    shape= ft.RoundedRectangleBorder(radius = 10)
                ),
            #bgcolor= ft.colors.GREEN_700
        )

    def build(self):
        return self.__desiner
    
    def setDisabled(self,valor=False):
        self.__desiner.disabled = valor