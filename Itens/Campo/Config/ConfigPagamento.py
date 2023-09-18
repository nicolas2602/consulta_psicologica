import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.Campo.CampoDrop import CampoDrop
from Itens.components.buttons.ActionButton import ActionButton

class ConfigPagamento(ft.UserControl):
    def __init__(self,page):
        self.page = page

        self.AddFormaPagamento = CampoFormulario("Horário Inicial",'07:00')
        self.horaInicio.setNaoAlter(True)