from  Itens.Formulario.Formulario import Formulario
from  Itens.components.buttons.ActionButton import ActionButton
from  Itens.Painel.PopUp import PopUp
from bd.funcao.cliente import *
import flet as ft

class Painel(ft.UserControl):
    '''Abre o Formulario de digitação para o cadastro com botões de comfimação.'''
    def __init__(self,page,titulo = None, funçãoSalvar = None):
        self.page = page
        self.__titulo = titulo
        
        self.__form = Formulario()
        
        self.__desiner = ft.AlertDialog(
            title=ft.Column(
            controls=[
                ft.Text(self.__titulo),
                self.__form.build(),
                ft.Row(
                    [   ## Botões ##
                        ActionButton('Cancelar',ft.colors.RED,ft.icons.CANCEL_OUTLINED, self.Cancelar).build(),
                        ActionButton('Salvar',ft.colors.GREEN_800,ft.icons.FILE_DOWNLOAD_DONE_ROUNDED, funçãoSalvar).build(),
                    ]
                )   
            ]
            
        )
    
    )
    def build(self):
        return self.__desiner

    def setPaine(self,id =None, nome = None, sobrenome = None, email = None, Telefone = None):
        '''Envia as informações para o formulario, normalmente usado como auto preenchimento da função editar.'''
        self.__form.setValue(id,nome,sobrenome,email,Telefone)
        # self.__desiner.title.controls[1] = self.__form
        self.page.update()
 
    def openPainel(self):
        self.page.dialog = self.__desiner
        self.__desiner.open = True
        self.page.update()

    def openPopUp(self,msg,cor):
        '''Abre o msg informando o resultado da ação, Ex: enviado com Sucesso ou Banco de dados.'''
        self.pop = PopUp(msg,cor).build()    
        self.page.snack_bar = self.pop
        self.page.snack_bar.open = True
        self.page.update()

    # def get(self):
    #     return self.__titulo
    

    def Cancelar(self,e):
        self.__desiner.open = False
        self.__form.setValue()
        self.page.update()

    def fechar(self,e):
        self.__desiner.open = False
        self.page.update()

    def getValue(self):
        return self.__form.getValue()
    
    def resetValue(self):
        self.__form.setValue()