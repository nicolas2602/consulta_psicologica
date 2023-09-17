import flet as ft
import bd.funcao.conexao as bd
from Itens.Principal import Principal
from Itens.Logging import Logging
from Itens.components.Carregamento import Carregamento
from Itens.Painel.PopUp import PopUp
from Itens.SemConexao import SemConexao
from modulos.AtualizarPagamento import AtualizarPagamento
from time import sleep


class TodoApp(ft.UserControl):

    def __init__(self,page):
        self.page = page

        self.login = Logging(self.page, self.logar)

        self.name = 'sistem'
        self.password = '1234'

        self.Carregar = Carregamento(self.page,"Carregando...")

        self.pagePrincipal = Principal(self.page, self.sair)

        self.designer = ft.Container(content = self.login.build(),expand=True)


    def build(self):
        if not bd.statosConexao():
            return SemConexao().build()
        else:
            return self.designer

    def openPopUp(self,msg,cor):
        '''Abre o msg informando o resultado da ação'''
        self.pop = PopUp(msg,cor).build()    
        self.page.snack_bar = self.pop
        self.page.snack_bar.open = True
        self.page.update()

    def logar(self,e):
        self.Carregar.openCarregamento(e)
        sleep(0.2)
        x =self.login.getValue()

        resutLog = (x['login'] == self.name)
        resutSn = (x['senha'] == self.password)
        
        msg = "Loggin e Senha incorretas!"

        if (resutLog and resutSn):
            #### Atualiza as Guia de Pagamento ####
            AtualizarPagamento().atualizar()

            self.login.limpar()
            sleep(0.2)
            self.designer.content = self.pagePrincipal.build()
            sleep(0.3)
            self.Carregar.closeCarregamento(e)

        else:
            sleep(0.5)
            self.Carregar.closeCarregamento(e)
            self.openPopUp(msg,ft.colors.RED)
            self.page.update()

    def sair(self,e):
        self.Carregar.openCarregamento(e)
        sleep(0.2)
        self.designer.content = self.login.build()
        sleep(0.2)
        self.Carregar.closeCarregamento(e)