import flet as ft

class GraficosStatusMes(ft.UserControl):
    def __init__(self,mesMaior, mesMenor):

        self.corBom = ft.colors.GREEN_900
        self.corRuin = ft.colors.RED_900
        
        self.Titulo1 = ft.Text(f"Melhor Mês",size=16,weight=ft.FontWeight.BOLD)
        self.Titulo2 = ft.Text(f"Pior Mês",size=16,weight=ft.FontWeight.BOLD)

        self.icone1 = ft.Icon(ft.icons.CALENDAR_MONTH,size=30,color=self.corBom)
        self.icone2 = ft.Icon(ft.icons.CALENDAR_MONTH,size=30,color=self.corRuin)

        self.textoMesMaior = ft.Text(value=f"{mesMaior}",color= self.corBom,size=25,weight=ft.FontWeight.BOLD)
        self.textoMesMenor = ft.Text(value=f"{mesMenor}",color= self.corRuin,size=25,weight=ft.FontWeight.BOLD)
        
        self.designer = ft.Row([

            ft.Column([ft.Row([self.icone1,self.Titulo1]),
            self.textoMesMaior],alignment="Center"),
            
            ft.VerticalDivider(thickness=2,color=ft.colors.GREY),

            ft.Column([ft.Row([self.icone2,self.Titulo2]),
            self.textoMesMenor],alignment="Center")

        ],alignment=ft.MainAxisAlignment.SPACE_EVENLY, vertical_alignment=ft.CrossAxisAlignment.CENTER )

        # self.designerTitulo = ft.Row([self.icone,self.Titulo],alignment="Center")    
        # self.designer = ft.Column([self.designerTitulo,self.designerTexto],alignment="Center",horizontal_alignment="Center")

    def build(self):
        return ft.Container(content=self.designer,width=450,height=120,padding=10,border=ft.border.all(2, ft.colors.GREY),border_radius=10, bgcolor=ft.colors.BLUE_GREY_50)