from Itens.Formulario.Formulario import Formulario
import flet as ft

class Painel(ft.UserControl):

    def __init__(self,titulo = None):

        self.__titulo = titulo
        
        self.__form = Formulario()
        
        self.__desiner = ft.AlertDialog(
            title=ft.Column(
            [
                ft.Text(self.__titulo),
                self.__form.build(),
                ft.Row(
                    [
                        ft.FilledButton(text='Cancelar'),
                        ft.FilledButton(text='OK')
                    ]
                )   
            ]
            
        )
    
    )


    def build(self):
        return self.__desiner
        
