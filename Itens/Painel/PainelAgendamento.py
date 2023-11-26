import flet as ft
from  Itens.Formulario.FormularioAgendamento import FormularioAgendamento
from Itens.Campo.CampoPesquisa import CampoPesquisa
from  Itens.components.buttons.ActionButton import ActionButton
from  Itens.Painel.PopUp import PopUp
from time import sleep

class PainelAgendamento(ft.UserControl):
    '''Abre o Formulario de digitação para o cadastro com botões de comfimação.'''
    def __init__(self,page,titulo = None, funçãoSalvar = None):
        self.page = page
        self.__titulo = titulo

        self.__formPesquisar = CampoPesquisa(page, "Digite o nome do Paciente:", self.pegardadosPesquisados)
        
        self.__formAgendamento = FormularioAgendamento(self.page)


        self.__desinerPesquisar = ft.AlertDialog(
            title=ft.Column(
            controls=[
                ft.Text(self.__titulo),
                self.__formPesquisar.build(),
                ft.Row(
                    [   ## Botões ##
                        ActionButton('Cancelar',ft.colors.RED,ft.icons.CANCEL_OUTLINED, self.Cancelar).build(),
                    ],alignment="Center"
                )
            ],width=400))

        self.__desinerAgendamento = ft.AlertDialog(
            title=ft.Column(
            controls=[
                ft.Text(self.__titulo),
                self.__formAgendamento.build(),
                ft.Row(
                    [   ## Botões ##
                        ActionButton('Salvar',ft.colors.GREEN_800,ft.icons.FILE_DOWNLOAD_DONE_ROUNDED, funçãoSalvar).build(),
                        ActionButton('Cancelar',ft.colors.RED,ft.icons.CANCEL_OUTLINED, self.Cancelar).build(),
                    ]
                )   
            ])
        )

    def build(self,n = 1):
        if(n == 1):
            return self.__desinerPesquisar
        else:
            return self.__desinerAgendamento

    def setPaine(self,id =None,id_nome = None, nome = None, data = None, hora = None):
        '''Envia as informações para o formulario, normalmente usado como auto preenchimento da função editar.'''
        self.__formAgendamento.setValue(id,id_nome,nome,data,hora)
        # self.__desiner.title.controls[1] = self.__form
        self.page.update()
 
    def openPainelNovo(self):
        self.page.dialog = self.__desinerPesquisar
        self.__desinerPesquisar.open = True
        self.page.update()

    def openPainelEditar(self):
        self.page.dialog = self.__desinerAgendamento
        self.__desinerAgendamento.open = True
        self.page.update()

    def pegardadosPesquisados(self,dados):
        self.__formAgendamento.setNome(dados[0],f"{dados[1]} {dados[2]}")
        self.fechar(self)
        self.__formPesquisar.listaDados()
        sleep(0.3)

        self.openPainelEditar()

    def openPopUp(self,msg,cor):
        '''Abre o msg informando o resultado da ação, Ex: enviado com Sucesso ou Banco de dados.'''
        self.pop = PopUp(msg,cor).build()    
        self.page.snack_bar = self.pop
        self.page.snack_bar.open = True
        self.page.update()

    def Cancelar(self,e):
        self.__desinerPesquisar.open = False
        self.__desinerAgendamento.open = False
        self.__formPesquisar.listaDados()
        self.__formAgendamento.setValue()
        self.page.update()

    def fechar(self,e):
        self.__desinerPesquisar.open = False
        self.__desinerAgendamento.open = False
        self.page.update()

    def getValue(self):
        return self.__formAgendamento.getValue()
    
    def resetValue(self):
        self.__formAgendamento.setValue()