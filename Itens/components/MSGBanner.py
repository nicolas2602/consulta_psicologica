import flet as ft
from time import sleep


class MSGBanner(ft.UserControl):
    def __init__(self,page):
        self.page = page

        self.texto = ft.Container(ft.Column([
            ft.Text("AWS:",size=14,weight=ft.FontWeight.W_500),
            ft.Text("THIS IS A MSG!!!",size=20,weight=ft.FontWeight.W_600)
            ],
            height=60),padding=20,
            bgcolor= ft.colors.GREEN_300,
            border_radius=ft.BorderRadius(top_left=15,top_right=15,bottom_left=0,bottom_right=0))

        self.designer = ft.BottomSheet(
        content= self.texto,
        )

    
    def setMsg(self,msg,cor):
        self.texto.bgcolor = cor
        self.texto.content.controls[1] = ft.Text(f"{msg}",size=20,weight=ft.FontWeight.W_600)

    def show_banner(self):
        self.page.overlay.append(self.designer)
        self.designer.open = True
        self.page.update()

        sleep(3)
        self.close_banner()
        

    def close_banner(self):
        self.designer.open = False
        self.page.update()