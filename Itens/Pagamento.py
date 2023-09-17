import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.components.buttons.ActionButton import ActionButton
from Itens.Campo.CampoDropStatus import CampoDropStatus
from Itens.Tabela.TabelaPagamento import TabelaPagamento
from Itens.components.Carregamento import Carregamento
from modulos.Check.VerificadorData import VerificadorData
from Itens.components.Titulo import Titulo
import bd_pagamento.pagamento as pg
from time import sleep,strftime

class Pagamento(ft.UserControl):
    def __init__(self,page):
        
        self.page = page
        #"Pagamentos",ft.icons.MONETIZATION_ON,

        
    def build(self):

        self.campoNome = CampoFormulario("Digite o nome:")
        
        self.campoDataInicio = CampoFormulario("Data Inicial",None,120)

        self.campoDataFinal = CampoFormulario("Data Final",None,120)

        self.StatusPGLista = pg.listaStatusPg()

        self.campoStatusPG = CampoDropStatus("Status",self.StatusPGLista,160,True)
        self.campoStatusPG.setValue('Todos')

        self.botaoPesquisa = ActionButton('Pesquisar', ft.colors.GREY_800 , ft.icons.SEARCH, self.getPesquisa).build()

        self.tabela = TabelaPagamento(self.page)

        self.designer = ft.Column(
            controls=[
                Titulo('Pagamentos',ft.icons.MONETIZATION_ON).build(),
                ft.Divider(color=ft.colors.GREEN_900),
                ft.Row([self.campoNome.build(), self.campoDataInicio.build(), self.campoDataFinal.build(), self.campoStatusPG.build(), self.botaoPesquisa], alignment= ft.MainAxisAlignment.CENTER, spacing= 15),
                ft.Divider(color=ft.colors.GREEN_900),

                ft.Row([self.tabela.build(),],vertical_alignment= ft.CrossAxisAlignment.START,expand=True),
                    
            ],
            expand=True,
        )
   
        return self.designer
    
    def getPesquisa(self,e):
        '''Função dedicada a pegar a informação do campo pesquisa, madar para o banco e atualizar a tabela'''
        nome = self.campoNome.getValue()
        dataInicial = self.campoDataInicio.getValue()
        datafinal = self.campoDataFinal.getValue()
        status = self.campoStatusPG.getValue()

        # Se os 2 Campos estão com dados
        dataInicial = VerificadorData(dataInicial).verificar()
        datafinal = VerificadorData(datafinal).verificar()

        if (dataInicial[0] and datafinal[0]):
            resultados = pg.pesquisarComTodasInfo(nome,status[1],dataInicial[1],datafinal[1])

        else:
            resultados = pg.pesquisarSemData(nome,status[1])

        self.tabela.dados = resultados
        self.tabela.montaTabela()
        self.page.update()