import flet as ft
class GraficosLinhas(ft.UserControl):
    def __init__(self, anoSelect, anoAnterior):

        self.cor1 = ft.colors.RED_ACCENT
        self.cor2 = ft.colors.BLUE_ACCENT

        self.Titulo = ft.Text(value="Levantamento de Ganhos:",weight=ft.FontWeight.BOLD,size=20)

        self.anoEscolhido = ft.Text(value= anoSelect,color=self.cor1,weight=ft.FontWeight.BOLD,size=20)
        self.anoAnterior = ft.Text(value= anoAnterior,color=self.cor2,weight=ft.FontWeight.BOLD,size=20)

        self.designerTexto1 = ft.Row([ft.Text(value="Ano Atual:"),self.anoEscolhido])
        self.designerTexto2 = ft.Row([ft.Text(value="Ano Anterior:"),self.anoAnterior])

        # anoAnterior 2022
        self.data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(0, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(1, 2000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(2, 5000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(3, 3100,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(4, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(5, 3000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(6, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(7, 6500,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(8, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(9, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(10, 5000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(11, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ],
                stroke_width=5,
                color=self.cor2,
                curved=False,
                stroke_cap_round=True,
            ),

            # anoEscolhido 2023
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(0, 3000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(1, 3440,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(2, 3440,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(3, 3440,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(4, 3440,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(5, 3440,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(6, 10000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(7, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(8, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(9, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(10, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                    ft.LineChartDataPoint(11, 4000,tooltip_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ],
                stroke_width=5,
                color=self.cor1,
                curved=False,
                stroke_cap_round=True,
            )
        ]

        self.chart = ft.LineChart(
            data_series= self.data_1,
            border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
            horizontal_grid_lines=ft.ChartGridLines(
                interval=1000, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
            ),
            vertical_grid_lines=ft.ChartGridLines(
                interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
            ),
            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=0,
                        label=ft.Text("0", size=14, weight=ft.FontWeight.BOLD),
                    ),

                    ft.ChartAxisLabel(
                        value=1000,
                        label=ft.Text("1K", size=14, weight=ft.FontWeight.BOLD),
                    ),

                    ft.ChartAxisLabel(
                        value=2000,
                        label=ft.Text("2K", size=14, weight=ft.FontWeight.BOLD),
                    ),

                    ft.ChartAxisLabel(
                        value=3000,
                        label=ft.Text("3K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=4000,
                        label=ft.Text("4K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=5000,
                        label=ft.Text("5K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=6000,
                        label=ft.Text("6K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=7000,
                        label=ft.Text("7K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=8000,
                        label=ft.Text("8K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=9000,
                        label=ft.Text("9K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=10000,
                        label=ft.Text("10K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=11000,
                        label=ft.Text("11K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=12000,
                        label=ft.Text("12K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=13000,
                        label=ft.Text("13K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=14000,
                        label=ft.Text("14K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=15000,
                        label=ft.Text("15K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=16000,
                        label=ft.Text("16K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=17000,
                        label=ft.Text("17K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=18000,
                        label=ft.Text("18K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=19000,
                        label=ft.Text("19K", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=20000,
                        label=ft.Text("20K", size=14, weight=ft.FontWeight.BOLD),
                    ),

                ],
                labels_interval=2000,
                labels_size=40,
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=0,
                        label=ft.Container(
                            ft.Text(
                                "JAN",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=1,
                        label=ft.Container(
                            ft.Text(
                                "FER",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=2,
                        label=ft.Container(
                            ft.Text(
                                "MAR",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=3,
                        label=ft.Container(
                            ft.Text(
                                "ABR",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=4,
                        label=ft.Container(
                            ft.Text(
                                "MAI",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=5,
                        label=ft.Container(
                            ft.Text(
                                "JUN",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=6,
                        label=ft.Container(
                            ft.Text(
                                "JUL",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=7,
                        label=ft.Container(
                            ft.Text(
                                "AGO",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=8,
                        label=ft.Container(
                            ft.Text(
                                "SET",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=9,
                        label=ft.Container(
                            ft.Text(
                                "OUT",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=10,
                        label=ft.Container(
                            ft.Text(
                                "NOV",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=11,
                        label=ft.Container(
                            ft.Text(
                                "DEZ",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                ],
                labels_interval=1,
                labels_size=32,
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.2, ft.colors.BLUE_GREY),
            min_y=0,
            max_y=20000,
            min_x=0,
            max_x=11,
            # animate=5000,
            expand=True,
        )

        #### Designer Montado Com Titulo ####
        self.designer = ft.Column([
            ft.Row([ft.Icon(ft.icons.QUERY_STATS,color=ft.colors.RED_800,size=30),self.Titulo]),
            ft.Row([
                self.designerTexto1,
                self.designerTexto2
            ],alignment= ft.MainAxisAlignment.SPACE_EVENLY),
            self.chart
        ])


    def build(self):
        return ft.Container(content=self.designer,width=650,height=450,padding=25,border=ft.border.all(2, ft.colors.GREY),border_radius=10, bgcolor=ft.colors.BLUE_GREY_50)