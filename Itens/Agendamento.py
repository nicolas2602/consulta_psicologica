import flet as ft
from time import sleep, strftime
from datetime import date
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.components.buttons.ActionButton import ActionButton
from Itens.components.Carregamento import Carregamento
from Itens.Tabela.TabelaAgendamento import TabelaAgendamento
from Itens.Painel.PainelAgendamento import PainelAgendamento
from modulos.Check.VerificadorData import VerificadorData
import bd_agend.agendamento as ag


class Agendamento(ft.UserControl):
    ''' Janela do Campo MENU Agendamento Consultas.
        Aqui, há todo a criação de contrução do campo MENU Agendamento 
    '''

    def __init__(self, page):
        self.page = page

    def build(self):

        self.addBotao = ActionButton('Adicionar',ft.colors.GREEN_800,ft.icons.ADD , self.openPainel).build()
        
        self.campoNome = CampoFormulario("Digite o nome:")
        
        self.campoData = CampoFormulario("Data",strftime("%d/%m/%Y"),120)
        
        self.botaoPesquisa = ActionButton('Pesquisar', ft.colors.GREY_800 , ft.icons.SEARCH).build()

        self.tabela = TabelaAgendamento(self.page)

        self.carregamento = Carregamento(self.page,"Salvando dados...")

        self.painelAgendamento = PainelAgendamento(self.page,"Novo Agendamento:",self.Salvar)

        self.desiner = ft.Column(
            controls=[
                ft.Row([self.addBotao, self.campoNome.build(), self.campoData.build(), self.botaoPesquisa], alignment= ft.MainAxisAlignment.CENTER, spacing= 50),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.tabela.build(),],vertical_alignment= ft.CrossAxisAlignment.START,expand=True) 
            ],
            expand=True,
        )
        return self.desiner
    
    def openPainel(self,e):
        '''Abre o Campo de Novo Agendamento'''
        self.painelAgendamento.openPainelNovo()

    def Salvar(self,e):
        # Dedicado ao Novo Cadastro
        '''Função e pega as informações do campo Novo cadastro e envia ao banco de dados.'''

        x = self.painelAgendamento.getValue()
        print(x)
        self.painelAgendamento.fechar(e)
        sleep(0.3)

        #### Tela de carregamento ####
        self.carregamento.openCarregamento(e)

        #### Variavel de Controle ####

        Carregando = True
        msg = "Consulta agendada com Sucesso"
        cor = ft.colors.GREEN_700


        while Carregando:

            héValido = VerificadorData(x['data']).verificar()

            if(héValido[0]):
                print(héValido[1])
                ag.insert(str(héValido[1]),x['hora'],int(x['idNome']))
                self.tabela.dados = ag.select("SELECT * from agendamento_consulta ORDER BY dataAgendCon,horarioAgendCon;")
                self.tabela.montaTabela()
                self.painelAgendamento.resetValue()

            else:
                msg = héValido[1] # retorna msg de erro
                cor = ft.colors.RED_700

            sleep(1)
            Carregando = False

        self.carregamento.closeCarregamento(e)
        #### Fim do Carregamento ####

        self.painelAgendamento.openPopUp(msg, cor)
        self.page.update()