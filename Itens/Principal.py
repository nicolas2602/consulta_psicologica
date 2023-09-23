import flet as ft
from Itens.MenuPrincipal import MenuPrincipal
from Itens.Cadastro import Cadastro
from Itens.Agendamento import Agendamento
from Itens.Pagamento import Pagamento
from Itens.Anotacoes import Anotacoes
from Itens.Configuracoes import Configuracoes
from Itens.Graficos import Graficos

class Principal(ft.UserControl):
    '''Classe como as Definições dos menus'''
    def __init__(self,page,fSair):
        self.page = page

        self.menu = MenuPrincipal(self.cadastro, self.agendamento,self.anotações,self.pagamentos,self.graficos, self.configuracoes,fSair)

    def build(self):

        # self.bodyCadastro = Cadastro(self.page).build()
        # self.bodyAgendamento = Agendamento(self.page).build()
        # self.bodyAnotacoes = Anotacoes(self.page).build()
        # self.bodyPagamento = Pagamento(self.page).build()
        # self.bodyConfiguracao = Configuracoes(self.page).build()
        # self.bodyGraficos = Graficos().build()


        self.desiner =ft.Row(
                controls=[
                    self.menu.build(),
                    #ft.Divider(color=ft.colors.GREEN_900),
                    ft.VerticalDivider(color=ft.colors.GREEN_900)
                ],
                expand=True
            )
        

        return self.desiner

    def cadastro(self,e):
        '''Quando selecionado, abre o janela cadastro'''

        #### Se houver uma janela já aberta, ele fecha a aberta e abre a janela selecionada. 
        if (len(self.desiner.controls) > 2):
            self.desiner.controls.pop(2)
            self.desiner.controls.append(Cadastro(self.page).build())

        else:
            self.desiner.controls.append(Cadastro(self.page).build())
        self.page.update()

    def agendamento(self,e):
        '''Quando selecionado, abre o janela Agendamento consultas'''
        #### Se houver uma janela já aberta, ele fecha a aberta e abre a janela selecionada. 
        if (len(self.desiner.controls) > 2):
            self.desiner.controls.pop(2)
            self.desiner.controls.append(Agendamento(self.page).build())

        else:
            self.desiner.controls.append(Agendamento(self.page).build())
        self.page.update()

    def anotações(self,e):
        '''Quando selecionado, abre o janela anotações'''
        #### Se houver uma janela já aberta, ele fecha a aberta e abre a janela selecionada. 
        if (len(self.desiner.controls) > 2):
            self.desiner.controls.pop(2)
            self.desiner.controls.append(Anotacoes(self.page).build())

        else:
            self.desiner.controls.append(Anotacoes(self.page).build())
        self.page.update()

    def pagamentos(self,e):
        '''Quando selecionado, abre o janela pagamentos'''
        #### Se houver uma janela já aberta, ele fecha a aberta e abre a janela selecionada. 
        if (len(self.desiner.controls) > 2):
            self.desiner.controls.pop(2)
            self.desiner.controls.append(Pagamento(self.page).build())

        else:
            self.desiner.controls.append(Pagamento(self.page).build())
        self.page.update()

    def graficos(self,e):
        '''Quando selecionado, abre o janela graficos'''
        #### Se houver uma janela já aberta, ele fecha a aberta e abre a janela selecionada. 
        if (len(self.desiner.controls) > 2):
            self.desiner.controls.pop(2)
            self.desiner.controls.append(Graficos().build())

        else:
            self.desiner.controls.append(Graficos().build())
        self.page.update()

    def configuracoes(self,e):
        '''Quando selecionado, abre o janela graficos'''
        #### Se houver uma janela já aberta, ele fecha a aberta e abre a janela selecionada. 
        if (len(self.desiner.controls) > 2):
            self.desiner.controls.pop(2)
            self.desiner.controls.append(Configuracoes(self.page).build())

        else:
            self.desiner.controls.append(Configuracoes(self.page).build())
        self.page.update()    
    
        