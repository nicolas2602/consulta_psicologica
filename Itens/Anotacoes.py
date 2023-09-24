import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.components.buttons.ActionButton import ActionButton
from Itens.components.Titulo import Titulo
from Itens.Tabela.TabelaAnotacoes import TabelaAnotacoes
from modulos.Check.VerificadorData import VerificadorData
from bd.funcao.anotacao_consulta import pesquisaAnotacoesNome,pesquisaAnotacoesNomeData
from time import sleep, strftime

class Anotacoes(ft.UserControl):
    ''' Janela do Campo MENU Anotações Consultas.
        Aqui, há todo a criação de contrução do campo MENU Anotações 
    '''

    def __init__(self, page):
        self.page = page
    
    def build(self):

        self.campoNome = CampoFormulario("Digite o nome:",None,None,self.getPesquisa)

        self.campoData = CampoFormulario("Data",strftime("%d/%m/%Y"),120,self.getPesquisa)

        self.botaoPesquisa = ActionButton('Pesquisar', ft.colors.GREY_800 , ft.icons.SEARCH, self.getPesquisa).build()

        self.tabela = TabelaAnotacoes(self.page)
        
        self.designer = ft.Column(
            controls=[
                Titulo('Anotações',ft.icons.EDIT_DOCUMENT).build(),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.campoNome.build(), self.campoData.build(), self.botaoPesquisa], alignment= ft.MainAxisAlignment.CENTER, spacing= 15),
                ft.Divider(color=ft.colors.GREEN_900),

                ft.Row([self.tabela.build()],vertical_alignment= ft.CrossAxisAlignment.START,expand=True),   
            ],
            expand=True,
        )
   
        return self.designer
    
    def getPesquisa(self,e):
        '''Função dedicada a pegar a informação do campo pesquisa, madar para o banco e atualizar a tabela'''

        nome = self.campoNome.getValue()
        data = self.campoData.getValue()

        # Se os 2 Campos estão com dados
        data = VerificadorData(data).verificar()

        if (data[0]):
            resultados = pesquisaAnotacoesNomeData(nome,data[1])

        else:
            resultados = pesquisaAnotacoesNome(nome)

        self.tabela.dados = resultados
        self.tabela.montaTabela()
        self.page.update()