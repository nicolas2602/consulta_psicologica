import flet as ft
from time import sleep, strftime
from datetime import date
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.components.buttons.ActionButton import ActionButton
from Itens.components.Carregamento import Carregamento
from Itens.Tabela.TabelaAgendamento import TabelaAgendamento
from Itens.Painel.PainelAgendamento import PainelAgendamento
from Itens.components.Titulo import Titulo
from modulos.Check.VerificadorData import VerificadorData
from modulos.Check.VerificadorAgendamentoExiste import VerificadorAgendamentoExiste
import bd.funcao.agendamento as ag
import bd.funcao.pagamento as pg
import bd.funcao.anotacao_consulta as ac
from modulos.Log import Log


class Agendamento(ft.UserControl):
    ''' Janela do Campo MENU Agendamento Consultas.
        Aqui, há todo a criação de contrução do campo MENU Agendamento 
    '''

    def __init__(self, page):
        self.page = page

    def build(self):

        self.addBotao = ActionButton('Adicionar',ft.colors.GREEN_800,ft.icons.ADD , self.openPainel).build()
        
        self.campoNome = CampoFormulario("Digite o nome:",None,None,self.getPesquisa)
        
        self.campoData = CampoFormulario("Data",strftime("%d/%m/%Y"),120,self.getPesquisa)
        
        self.botaoPesquisa = ActionButton('Pesquisar', ft.colors.GREY_800 , ft.icons.SEARCH, self.getPesquisa).build()

        self.tabela = TabelaAgendamento(self.page)

        self.carregamento = Carregamento(self.page,"Salvando dados...")

        self.painelAgendamento = PainelAgendamento(self.page,"Novo Agendamento:",self.Salvar)

        self.desiner = ft.Column(
            controls=[
                Titulo('Agendamento de Consultas',ft.icons.CALENDAR_MONTH,).build(),
                ft.Divider(color=ft.colors.GREEN_900),
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

    def getPesquisa(self,e):
        '''Função dedicada a pegar a informação do campo pesquisa, madar para o banco e atualizar a tabela'''
        nome = self.campoNome.getValue()
        data = self.campoData.getValue()
        resultados = None

        # Se os 2 Campos estão com dados
        data = VerificadorData(data).verificar()

        if (nome != ''and data[0]):
            resultados = ag.pesquisaNomeData(nome,data[1])

        elif(nome != '' and not data[0]):
            resultados = ag.pesquisaNome(nome)

        elif(nome == '' and data[0]):
            resultados = ag.pesquisaData(data[1])
        
        else:
            resultados = ag.pesquisaTudo()

        if (resultados != None):
            self.tabela.dados = resultados
            self.tabela.montaTabela()
            self.page.update()

    def Salvar(self,e):
        # Dedicado ao Novo Cadastro
        '''Função e pega as informações do campo Novo cadastro e envia ao banco de dados.'''

        x = self.painelAgendamento.getValue()

        self.painelAgendamento.fechar(e)
        sleep(0.3)

        #### Tela de carregamento ####
        self.carregamento.openCarregamento(e)

        #### Variavel de Controle ####

        Carregando = True
        msg = "Consulta agendada com Sucesso"
        cor = ft.colors.GREEN_700
        salvarNoBD = [False,'']

        while Carregando:

            héValido = VerificadorData(x['data']).verificar()

            if(héValido[0]):
                if(x['hora'] != '' and x['hora'] != None):
                    data = héValido[1].strftime("%d/%m/%Y")

                    #### INSERE AGENDAMENTO NO BD #####
                    if (not VerificadorAgendamentoExiste().AgendaExiste(héValido[1],x['hora'])[0]):
                        #### INSERE AGENDAMENTO NO BD #####
                        ag.insert(data,x['hora'],int(x['idNome']))
                        sleep(0.5)

                        #### INSERE PAGAMENTO NO BD #####
                        novoDados = ag.pesquisaIdNomeDataHora(x['idNome'],héValido[1],x['hora'])
                        pg.insertAgendPg(novoDados[0][0])
                        ac.insertAnotacao(novoDados[0][0])

                        #### Salvo ####
                        salvarNoBD = [True,novoDados[0][0]]

                        #### ATUALIZA A TABELA ####
                        self.tabela.dados = ag.pesquisaData(héValido[1])
                        self.tabela.montaTabela()
                        self.painelAgendamento.resetValue()
                    else:
                        msg = "Agendamento já exitente"
                        cor = ft.colors.RED_700
                else:
                    msg = "Hora Invalida"
                    cor = ft.colors.RED_700
            else:
                msg = héValido[1] # retorna msg de erro
                cor = ft.colors.RED_700

            sleep(1)
            Carregando = False

        self.carregamento.closeCarregamento(e)
        #### Fim do Carregamento ####

        self.painelAgendamento.openPopUp(msg, cor)
        self.page.update()

        sleep(1)
        if salvarNoBD[0]:
            self.awdEnvido("Create",salvarNoBD[1])

    def awdEnvido(self,tipo,id):
        x = Log(self.page)
        x.submit("agendamento_consulta",id,tipo,"user")