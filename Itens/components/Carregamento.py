import flet as ft
from time import sleep

class Carregamento(ft.UserControl):

    def __init__(self,page,msg,time = 1):
        self.page = page
        self.time = time
        self.IconeCaregamento = ft.ProgressRing(height=170)
        self.desiner = ft.AlertDialog(title=ft.Text(value= msg), content= ft.Container(content=self.IconeCaregamento),modal=True, content_padding= 50)

    def build(self):
        return self.desiner
    
    def openCarregamento(self,e):
        self.page.dialog = self.desiner
        self.desiner.open = True
        self.page.update()

        # sleep(self.time)
        # self.closeCarregamento(e)

    def closeCarregamento(self,e):
        self.desiner.open = False
        self.page.update()