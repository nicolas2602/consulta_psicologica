import flet as ft

class GraficosColunas(ft.UserControl):
    def __init__(self):

        self.grafColum = ft.BarChart(
            #### colunas do item com cor ####
            bar_groups=[
                ft.BarChartGroup(
                x=0,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=6700,
                        width=40,
                        color=ft.colors.AMBER,
                        tooltip="6700",
                        border_radius=0,
                    )]
                ),
                ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=5000,
                        width=40,
                        color=ft.colors.RED,
                        tooltip="5000",
                        border_radius=0,
                    )]
                ),
                ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=8900,
                        width=40,
                        color=ft.colors.BLUE,
                        tooltip="8900",
                        border_radius=0,
                    )]
                ),
            ],
            border=ft.border.all(1, ft.colors.GREY_400),
            ##### Colunas a Esqueda com a numerações ####
            left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Ganhos Brutos por Mes"), title_size=40
            ),
            ##### Eixo de baixo como os nome das colunas ####
            bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0, label=ft.Container(ft.Text("Outubro"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=1, label=ft.Container(ft.Text("Novembro"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=2, label=ft.Container(ft.Text("Desembro"), padding=10)
                ),
            ],labels_size=40,
            ),
            #### marcações que auxilia a visão dentro do graficos (linha guias) ####
            horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
            #### define configuração do tamanho maximo ####
            max_y=10000,
            interactive=True,
            expand=True,
        )


    def build(self):
        return ft.Container(content=self.grafColum,width=500,height=400)
    
