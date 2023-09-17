import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.Campo.CampoDrop import CampoDrop

class ConfigHoras(ft.UserControl):
    def __init__(self):

        self.horaInicio = CampoFormulario("Horário Inicial")
        self.horaFinal = CampoFormulario("Horário Final")
        self.horaInicioAlmoco = CampoFormulario("Horário Inicial do Intervalo")
        self.horaFinalAlmoco = CampoFormulario("Horário Final do Intervalo")
        self.horaDaSessao = CampoDrop("Tempo da Consulta em minutos",['30','35','40','45','50','55','60'],300)

        self.designer = ft.Column(
            controls = [
                ft.Text("Horário de Trabalho"),
                ft.Row([self.horaInicio.build(),self.horaFinal.build()]),
                ft.Text("Horário de Pausa"),
                ft.Row([self.horaInicioAlmoco.build(),self.horaFinalAlmoco.build()]),
                ft.Text("Tempo da Consulta"),
                self.horaDaSessao.build()
            ]
        )

    ft.Text
        

    def build(self):
        return self.designer