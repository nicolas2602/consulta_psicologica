import flet as ft

class CampoFormularioSenha(ft.UserControl):
    '''Campo de Digitação Estilizado para o Projeto'''
        
    def __init__(self, nome = None, valor = None, largura = None, funcao = None):

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
            password= True,
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

    def getPassVisual(self):
        return self.__desiner.password
    
    def setPassVisual(self,valor = True):
        self.__desiner.password =valor