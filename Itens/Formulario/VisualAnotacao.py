import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
import bd.funcao.pagamento as pg

class VisualAnotacao(ft.UserControl):

    '''Cria um conjunto de capos visual para Anotação.'''

    def __init__(self,page,Titulo = None, Anotacoes=None):
        self.page = page

        self.__titulo = ft.Text(value=Titulo,width=410,size=20,weight=ft.FontWeight.BOLD)
        self.__anotacoes = ft.Text(value=Anotacoes,width=410,size=15)

        self.__desginer = ft.Column(controls=[
            self.__titulo,
            self.__anotacoes
        ],scroll= ft.ScrollMode.ALWAYS)

    def build(self):
        return self.__desginer

    def setValue(self, Titulo = None, Anotacoes=None):
        '''Seta os valores do Campo (auto preenchimento).'''

        self.__titulo.value = Titulo
        self.__anotacoes.value = Anotacoes

    