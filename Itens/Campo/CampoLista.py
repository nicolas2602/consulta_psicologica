import flet as ft

class CampoLista(ft.UserControl):

    def __init__(self,lista=None,largura=None,altura=None,funcao=None):

        self.lista = lista

        self.funcao=funcao

        self.OpcoesLista = ft.ListView(controls=[])

        self.designer = ft.Container(content=self.OpcoesLista,width=largura,height=altura,border_radius = 10,
            border=ft.border.all(2,ft.colors.BLACK26),expand=False)

    def build(self):
        return self.designer

    def addOpcoes(self):
        '''Gera a lista do conteudo da pesquisa'''
        for item in self.lista:
            self.opcao(item)

    def opcao(self,dados):
        '''Gera o botão Texto da Lista'''
        self.OpcoesLista.controls.append(ft.TextButton(text=f"{dados[1]}", on_click= lambda e: self.funcao(dados),style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.GREEN_900})))

    def setNaoAlter(self,valor = False):
        self.OpcoesLista.disabled = valor