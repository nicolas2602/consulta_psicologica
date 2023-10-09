import flet as ft

class GraficosPizza(ft.UserControl):
    def __init__(self):
        
        self.corGanhos = ft.colors.GREEN_700
        self.corGanhosFuturos = ft.colors.BLUE
        self.corNaoPago = ft.colors.RED_900

        self.textoConcluido = ft.Text(value="Concluido",weight=ft.FontWeight.BOLD)
        self.textoAndamento = ft.Text(value="Em Andamento",weight=ft.FontWeight.BOLD)
        self.textoPendente = ft.Text(value="Pendente",weight=ft.FontWeight.BOLD)

        self.icon1 = ft.Icon(ft.icons.MONETIZATION_ON,color=self.corGanhos,)
        self.icon2 = ft.Icon(ft.icons.MONETIZATION_ON,color=self.corGanhosFuturos,)
        self.icon3 = ft.Icon(ft.icons.MONETIZATION_ON,color=self.corNaoPago,)

        self.designerLegenda = ft.Column([
            ft.Row([self.icon1,self.textoConcluido]),
            ft.Row([self.icon2,self.textoAndamento]),
            ft.Row([self.icon3,self.textoPendente])
        ])


        # parametro do Grafico
        self.normal_radius = 100
        self.hover_radius = 110
        self.normal_title_style = ft.TextStyle(
            size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
        )
        self.hover_title_style = ft.TextStyle(
            size=20,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.BOLD,
            shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
        )
        self.normal_badge_size = 40
        self.hover_badge_size = 50

    
        self.chart = ft.PieChart(
            sections=[
                #### Não Pagos ####
                ft.PieChartSection(
                    5,
                    title="5%",
                    title_style=self.normal_title_style,
                    color=self.corNaoPago,
                    radius=self.normal_radius,
                    badge=self.badge(ft.icons.MONETIZATION_ON,self.corNaoPago,self.normal_badge_size),
                    badge_position=0.98,
                ),

                #### Ganhos ####
                ft.PieChartSection(
                    70,
                    title="70%",
                    title_style=self.normal_title_style,
                    color=self.corGanhos,
                    radius=self.normal_radius,
                    badge=self.badge(ft.icons.MONETIZATION_ON, self.corGanhos, self.normal_badge_size),
                    badge_position=0.98,
                ),

                #### Ganhos Futuros ####
                ft.PieChartSection(
                    25,
                    title="25%",
                    title_style=self.normal_title_style,
                    color=self.corGanhosFuturos,
                    radius=self.normal_radius,
                    badge=self.badge(ft.icons.MONETIZATION_ON, self.corGanhosFuturos, self.normal_badge_size),
                    badge_position=0.98,
                ),
            ],
            sections_space=0,
            center_space_radius=0,
            on_chart_event=self.on_chart_event,
            expand=True,
        )


        self.designer = ft.Column([
            ft.Row([ft.Icon(ft.icons.LOCAL_PIZZA,size=30,color=ft.colors.ORANGE_800),ft.Text(value="Percentual Dos Status Pagamento:",weight=ft.FontWeight.BOLD,size=20)]),
            ft.Row([
                self.chart,
                self.designerLegenda
                ],height=230)
            ])

    

    def build(self):
        return ft.Container(content=self.designer,width=450,height=320,padding=25,border=ft.border.all(2, ft.colors.GREY),border_radius=10, bgcolor=ft.colors.BLUE_GREY_50)

    def badge(self, icon, cor, size):
        return ft.Container(
            ft.Icon(icon,color=cor),
            width=size,
            height=size,
            border=ft.border.all(1, ft.colors.BROWN),
            border_radius=size / 2,
            bgcolor=ft.colors.WHITE,
        )

    def on_chart_event(self,e: ft.PieChartEvent):
        for idx, section in enumerate(self.chart.sections):
            if idx == e.section_index:
                section.radius = self.hover_radius
                section.title_style = self.hover_title_style
            else:
                section.radius = self.normal_radius
                section.title_style = self.normal_title_style
        self.chart.update()