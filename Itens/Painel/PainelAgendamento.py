import flet as ft

class PainelAgendamento(ft.UserControl):
    '''Abre o Formulario de digitação para o cadastro com botões de comfimação.'''
    def __init__(self,page,titulo = None, funçãoSalvar = None):
        self.page = page
        self.__titulo = titulo