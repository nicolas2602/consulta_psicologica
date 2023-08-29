import flet as ft
from time import sleep

class Checagem(ft.UserControl):
    '''Uma Janela com uma msg definida com botões de comfimação (Sim ou Não)'''

    def __init__(self,page,msg):
        self.page = page
        self.resultado = False

        self.desiner = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar:"),
            content=ft.Text(msg),
            actions=[
                ## botões ##
                ft.TextButton("Sim", on_click= self.__setResutado),
                ft.TextButton("Não", on_click= self.__fecharDialogo),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),)
        
    def build(self):
        return self.desiner
    
    def __setResutado(self,e):
        self.resultado = True
        self.__fecharDialogo(e)
        

    def __fecharDialogo(self,e):
        self.desiner.open = False
        self.page.update()

    def checar(self):
        '''Abre o dialogo e returna "True ou False" de acordo com a Interação do usuario'''

        self.page.dialog = self.desiner
        self.desiner.open = True
        self.page.update()

        #### Tempo de espera até a interação do usuario ####
        while (self.desiner.open == True):
            sleep(1)

        return self.resultado