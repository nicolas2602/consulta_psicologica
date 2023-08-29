import flet as ft
from Itens.Painel.Painel import Painel
from Itens.components.buttons.ActionButton import ActionButton
from Itens.Tabela.Tabela import Tabela
from Itens.Campo.CampoFormulario import CampoFormulario
from bd.funcao.cliente import *

class Cadastro(ft.UserControl):
    ''' Janela do Campo MENU Cadastro.
        Aqui, há todo a criação de contrução do campo MENU CADASTRO 
    '''
    def __init__(self, page):
        self.page = page

    def build(self):

        self.addCadastro = Painel(self.page,"Novo Cadastro",self.Salvar)

        self.addBotao = ActionButton('Adicionar',ft.colors.GREEN_800,ft.icons.ADD, self.openPainel).build()

        self.campoPesquisa = CampoFormulario("Pesquisa por nome")
        
        self.botaoPesquisa = ActionButton('Pesquisar', ft.colors.GREY_800 , ft.icons.SEARCH, self.getPesquisa).build()

        self.tabela = Tabela(self.page)

        self.desiner = ft.Column(
            controls=[
                ft.Row([self.addBotao, self.campoPesquisa.build(), self.botaoPesquisa], alignment= ft.MainAxisAlignment.CENTER, spacing= 50),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.tabela.build(),],vertical_alignment= ft.CrossAxisAlignment.START,expand=True) 
            ],
            expand=True,
        )

        return self.desiner
    
    #### Fuções do Cadastro ####
    def openPainel(self,e):
        '''Abre o Campo de Novo Cadastro'''
        self.page.dialog = self.addCadastro.build()
        self.addCadastro.build().open = True
        self.page.update()

    def getPesquisa(self,e):
        '''Função dedicada a pegar a informação do campo pesquisa, madar para o banco e atualizar a tabela'''
        x = self.campoPesquisa.getValue()
        self.tabela.dados = select(f"SELECT * FROM cliente WHERE nomeCliente LIKE '%{x}%'")
        self.tabela.montaTabela()
        self.page.update()

    def Salvar(self,e):
        # Dedicado ao Novo Cadastro
        '''Função e pega as informações do campo Novo cadastro e envia ao banco de dados.'''
        x = self.addCadastro.getValue()
        insert(x['nome'],x['sobrenome'],x['email'],x['telefone'])
        self.addCadastro.Cancelar(e)
        self.addCadastro.openPopUp("Cadastro com Sucesso", ft.colors.GREEN_700)
        self.tabela.dados = select(f"SELECT * FROM cliente")
        self.tabela.montaTabela()
        self.page.update()