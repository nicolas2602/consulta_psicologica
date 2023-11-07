import flet as ft

class GraficosMediaGanhoMes(ft.UserControl):
    def __init__(self,page,valor = "0"):
        self.page = page

        self.cor = ft.colors.ORANGE_400
        
        self.Titulo = ft.Text(f"Media por mes:",size=18,weight=ft.FontWeight.BOLD)

        self.icone = ft.Icon(ft.icons.MONETIZATION_ON,size=30,color=self.cor)

        self.texto = ft.Text(value=f"R$ {valor}",color= self.cor,size=30,weight=ft.FontWeight.BOLD)

        self.designerTitulo = ft.Row([self.icone,self.Titulo],alignment="Center")    
        self.designer = ft.Column([self.designerTitulo,self.texto],alignment="Center",horizontal_alignment="Center")

    def build(self):
        return ft.Container(content=self.designer,width=270,height=120,border=ft.border.all(2, ft.colors.GREY),border_radius=10, bgcolor=ft.colors.BLUE_GREY_50)

    def setValue(self,valor = "0"):
        self.texto.value = f"R$ {valor}"
        self.page.update()