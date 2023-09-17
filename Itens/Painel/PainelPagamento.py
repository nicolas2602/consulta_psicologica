import flet as ft
from  Itens.Formulario.FormularioPagamento import FormularioPagamento
from  Itens.components.buttons.ActionButton import ActionButton
from  Itens.Painel.PopUp import PopUp


class PainelPagamento(ft.UserControl):

    '''Abre o Formulario de Edição para o Pagamento com botões de comfimação'''

    def __init__(self,page,titulo = None, funçãoSalvar = None):

        self.page = page
        self.__titulo = titulo

        self.__formPagamento = FormularioPagamento()
        
        self.__designer = ft.AlertDialog(
            title=ft.Column(
            controls=[
                ft.Text(self.__titulo),
                self.__formPagamento.build(),
                ft.Row(
                    [   ## Botões ##
                        ActionButton('Salvar',ft.colors.GREEN_800,ft.icons.FILE_DOWNLOAD_DONE_ROUNDED, funçãoSalvar).build(),
                        ActionButton('Cancelar',ft.colors.RED,ft.icons.CANCEL_OUTLINED, self.Cancelar).build(),
                    ]
                )   
            ])
        )


    def build(self):
        return self.__designer

    def setPaine(self,idBD = None, valor = None, data = None, formaPg = None , statusPg = None):
        '''Envia as informações para o formulario, normalmente usado como auto preenchimento da função editar.'''
        self.__formPagamento.setValue(idBD,valor,data,formaPg,statusPg)
        self.page.update()
 
    def openPainel(self):
        self.page.dialog = self.__designer
        self.__designer.open = True
        self.page.update()

    def openPopUp(self,msg,cor):
        '''Abre o msg informando o resultado da ação, Ex: enviado com Sucesso ou Banco de dados.'''
        self.pop = PopUp(msg,cor).build()    
        self.page.snack_bar = self.pop
        self.page.snack_bar.open = True
        self.page.update()

    def Cancelar(self,e):
        self.__designer.open = False
        self.__formPagamento.setValue()
        self.page.update()

    def fechar(self,e):
        self.__designer.open = False
        self.page.update()

    def getValue(self):
        return self.__formPagamento.getValue()
    
    def resetValue(self):
        self.__formPagamento.setValue()