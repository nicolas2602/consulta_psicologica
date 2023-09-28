import flet as ft

class CampoFormulario(ft.UserControl):
    '''Campo de Digitação Estilizado para o Projeto'''
        
    def __init__(self, nome = None, valor = None, largura = None, funcao=None):

        self.__nome = nome

        # self.__config_form = {
        #     'color': ft.colors.BLACK,
        #     'bg': ft.colors.GREEN_700
        # }

        self.__desiner = ft.TextField(
            label= self.__nome,
            label_style= ft.TextStyle(color = ft.colors.GREEN_900),
            value= valor,
            border_color= ft.colors.GREEN_900,
            border_radius = 15,
            width= largura,
            on_submit= funcao
            )

    def build(self):
        '''Retorna o Desiner do Campo de Digitação'''
        return self.__desiner
    
    def getValue(self):
        return self.__desiner.value
    
    def setValue(self,valor = None):
        self.__desiner.value = valor

    def setNaoAlter(self,valor = False):
        self.__desiner.read_only = valor

    def setPlaceHolder(self,valor = None):
        self.__desiner.hint_text =valor

    def setMultiline(self,valor=False,qtd=None):
        self.__desiner.multiline = valor
        self.__desiner.max_lines = qtd

    def setOnChange(self,funcao=None):
        self.__desiner.on_change = funcao