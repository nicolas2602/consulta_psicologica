import flet as ft
from bd.funcao.cliente import *

class CampoPesquisa(ft.UserControl):
    '''Campo de pesquisa de Clientes que mostrará opções de seleção estilizado para o Projeto'''
        
    def __init__(self,page, nome = None, funcao = None):

        self.__nome = nome
        self.page = page

        self.funcao = funcao

        self.texto = ft.TextField(
            label= self.__nome,
            icon= ft.icons.SEARCH_SHARP,
            label_style= ft.TextStyle(color = ft.colors.GREEN_900),
            #value= valor,
            border_color= ft.colors.GREEN_900,
            border_radius = 15,
            on_change= self.onChange
            )
        
        self.Opcoes = ft.ListView(controls=[],visible= False)

        self.__desiner =ft.Column(controls=[self.texto,self.Opcoes])



    def build(self):
        '''Retorna o Desiner do Campo de Digitação'''
        return self.__desiner
    
    def onChange(self,e):
        ''' Metodo que é execultado quando digitar no campo pesquisa
            ele é reponsavel em pegar o campo digitado e adicionar uma
            lista de posiveis clientes.
        '''
        x = self.getValue()
        y = []
        
        if (x == None or x == ""):
            y = None
            self.addOpcoes(y)
            self.page.update()
        else:
            y = select(f"SELECT IdCliente,nomeCliente,sobrenomeCliente FROM cliente WHERE nomeCliente LIKE '%{x}%'")
            self.addOpcoes(y)
            self.page.update()

    def addOpcoes(self,valor):
        '''Gera a lista do conteudo da pesquisa'''
        if(valor == None or valor == ""):
            self.Opcoes.visible = False
        else:
            self.Opcoes.visible = True
            self.Opcoes.controls = []

            for item in valor:
                self.opcao(item)
        
    def opcao(self,dados):
        '''Gera o botão Texto da Lista'''
        self.Opcoes.controls.append(ft.TextButton(text=f"{dados[1]} {dados[2]}", on_click= lambda e: self.funcao(dados)))


    def getValue(self):
        return self.texto.value
    
    def setValue(self,valor = None):
        self.texto.value = valor

    def listaDados(self):
        self.texto.value = None
        self.Opcoes.visible = False
        self.Opcoes.controls = []