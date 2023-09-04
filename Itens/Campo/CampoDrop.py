import flet as ft

class CampoDrop(ft.UserControl):
    '''Campo com opções de seleção estilizado para o Projeto'''
        
    def __init__(self, nome = None, listaOpções = None, width = None):

        self.__nome = nome
        self.__lista = listaOpções
        # self.__config_form = {
        #     'color': ft.colors.BLACK,
        #     'bg': ft.colors.GREEN_700
        # }

        self.__desiner = ft.Dropdown(
            width= width,
            label= self.__nome,
            label_style= ft.TextStyle(color = ft.colors.GREEN_900),
            #value= valor,
            options=[],
            border_color= ft.colors.GREEN_900,
            border_radius = 15
            )

    def build(self):
        '''Retorna o Desiner do Campo de Digitação'''
        self.addlista()
        return self.__desiner
    
    def addlista(self):
        for item in self.__lista:
            self.__desiner.options.append(ft.dropdown.Option(item))


    def getValue(self):
        return self.__desiner.value
    
    def setValue(self,valor = None):
        self.__desiner.value = valor