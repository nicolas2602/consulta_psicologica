import flet as ft
from  Itens.Formulario.FormularioAnotacao import FormularioAnotacao
from  Itens.Formulario.NomeDataAnotação import NomeDataAnotação
from  Itens.components.buttons.ActionButton import ActionButton
from  Itens.Painel.PopUp import PopUp


class PainelAnotacoes(ft.UserControl):

    '''Abre o Formulario de Edição para o Pagamento com botões de comfimação'''

    def __init__(self,page,titulo = None, funçãoSalvar = None):

        self.page = page
        self.__titulo = titulo

        self.__formAnotacao = FormularioAnotacao(self.page)
 
        self.__NomeDataAnota = NomeDataAnotação(self.page)
        
        self.__designer = ft.AlertDialog(
            title=ft.Column(
            controls=[
                ft.Row([ft.Icon(ft.icons.EDIT_DOCUMENT,color=ft.colors.GREEN_900),ft.Text(self.__titulo)]),
                ft.Divider(color=ft.colors.GREEN_800),
                ft.Row(
                    [
                        self.__NomeDataAnota.build(),
                        ft.VerticalDivider(color=ft.colors.GREEN_800),
                        self.__formAnotacao.build(),
                    ],height=380,width=600
                ),  
                ft.Row(
                    [   ## Botões ##
                        ActionButton('Salvar',ft.colors.GREEN_800,ft.icons.FILE_DOWNLOAD_DONE_ROUNDED, funçãoSalvar).build(),
                        ActionButton('Cancelar',ft.colors.RED,ft.icons.CANCEL_OUTLINED, self.Cancelar).build(),
                    ],alignment="Center"
                )   
            ],width=600)
        )


    def build(self):
        return self.__designer

    def setPaine(self,idBD = None, Nome=None, SobreNome=None, data=None, hora=None, titulo = None, anotacao=None):
        '''Envia as informações para o formulario, normalmente usado como auto preenchimento da função editar.'''
        self.__NomeDataAnota.setValue(Nome,SobreNome,data,hora)
        self.__formAnotacao.setValue(idBD,titulo,anotacao)
        self.__designer = self.__designer
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
        self.__formAnotacao.setValue()
        self.page.update()

    def fechar(self,e):
        self.__designer.open = False
        self.page.update()

    def getValue(self):
        return self.__formAnotacao.getValue()
    
    def resetValue(self):
        self.__formAnotacao.setValue()