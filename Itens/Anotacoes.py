import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.components.buttons.ActionButton import ActionButton
from Itens.components.Titulo import Titulo
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
        
        self.designer = ft.Column(
            controls=[
                Titulo('Anotações',ft.icons.EDIT_DOCUMENT).build(),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.campoNome.build(), self.campoData.build(), self.botaoPesquisa], alignment= ft.MainAxisAlignment.CENTER, spacing= 15),
                ft.Divider(color=ft.colors.GREEN_900),

                ft.Column([ft.Icon(name=ft.icons.CONSTRUCTION, size= 200),ft.Text("Anotações... Em Desenvolvimento...",size=20)])

                #ft.Row([self.tabela.build(),],vertical_alignment= ft.CrossAxisAlignment.START,expand=True),   
            ],
            expand=True,
        )
   
        return self.designer
    
    def getPesquisa(self,e):
        '''Função dedicada a pegar a informação do campo pesquisa, madar para o banco e atualizar a tabela'''
        pass
        # nome = self.campoNome.getValue()
        # dataInicial = self.campoDataInicio.getValue()
        # datafinal = self.campoDataFinal.getValue()
        # status = self.campoStatusPG.getValue()

        # # Se os 2 Campos estão com dados
        # dataInicial = VerificadorData(dataInicial).verificar()
        # datafinal = VerificadorData(datafinal).verificar()

        # if (dataInicial[0] and datafinal[0]):
        #     resultados = pg.pesquisarComTodasInfo(nome,status[1],dataInicial[1],datafinal[1])

        # else:
        #     resultados = pg.pesquisarSemData(nome,status[1])

        # self.tabela.dados = resultados
        # self.tabela.montaTabela()
        # self.page.update()