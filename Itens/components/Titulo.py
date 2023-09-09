import flet as ft

class Titulo(ft.UserControl):
    def __init__(self,txt, logo):
        self.txt = txt

        self.desiner = ft.Row(
            controls = [
                ft.Icon(logo,color= ft.colors.GREEN_900,size=50),
                ft.Text(value= self.txt,style=ft.TextThemeStyle.DISPLAY_SMALL)
                ])

    def build(self):
        return self.desiner
    

