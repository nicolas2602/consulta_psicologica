import flet as ft
from time import sleep

class Checagem(ft.UserControl):
    def __init__(self,page,msg):
        self.page = page
        self.resultado = False

        self.desiner = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar:"),
            content=ft.Text(msg),
            actions=[
                ft.TextButton("Sim", on_click= self.setResutado),
                ft.TextButton("Não", on_click= self.fecharDialogo),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),)
        
    def build(self):
        return self.desiner
    
    def setResutado(self,e):
        self.resultado = True
        self.fecharDialogo(e)
        

    def fecharDialogo(self,e):
        self.desiner.open = False
        self.page.update()

    def checar(self):
        self.page.dialog = self.desiner
        self.desiner.open = True
        self.page.update()
        while (self.desiner.open == True):
            sleep(1)
        return self.resultado