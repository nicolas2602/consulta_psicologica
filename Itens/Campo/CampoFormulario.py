import flet as ft

class CampoFormulario(ft.UserControl):
        
    def __init__(self, nome = None, valor = None):
        self.__nome = nome

        self.__config_form = {
            'color': ft.colors.BLACK,
            'bg': ft.colors.GREEN_700
        }

        self.__desiner = ft.TextField(
            label= self.__nome,
            label_style= ft.TextStyle(color = ft.colors.GREEN_900),
            value= valor,
            border_color= ft.colors.GREEN_900,
    
            )

    def build(self):
        return self.__desiner
    
    def getValue(self,e):
        return self.__desiner.value
    
    def setValue(self,valor):
        self.__desiner.value = valor