from  Itens.Formulario.Formulario import Formulario
from  Itens.components.buttons.ActionButton import ActionButton
from  Itens.Painel.PopUp import PopUp
import flet as ft

class Painel(ft.UserControl):

    def __init__(self,page,titulo = None, id =None, nome = None, sobrenome = None, email = None, Telefone = None):
        self.page = page
        self.__titulo = titulo
        
        self.__form = Formulario(id, nome, sobrenome, email, Telefone)
        
        self.__desiner = ft.AlertDialog(
            title=ft.Column(
            controls=[
                ft.Text(self.__titulo),
                self.__form.build(),
                ft.Row(
                    [
                        ActionButton('Cancelar',ft.colors.RED,ft.icons.CANCEL_OUTLINED, self.fechar).build(),
                        ActionButton('Salvar',ft.colors.GREEN_800,ft.icons.FILE_DOWNLOAD_DONE_ROUNDED,self.ok).build(),
                    ]
                )   
            ]
            
        )
    
    )
    def build(self):
        return self.__desiner

    def setPaine(self,id =None, nome = None, sobrenome = None, email = None, Telefone = None):
        self.__form.setValue(id,nome,sobrenome,email,Telefone)
        # self.__desiner.title.controls[1] = self.__form
        self.page.update()

    def fechar(self,e):
        self.__desiner.open = False
        self.__form.setValue()
        self.page.update()

    def ok(self,e):
        x = self.__form.get_value()
        print(x)
        self.fechar(e)
        self.openPopUp("Sucesso", ft.colors.GREEN_700)
        
    def openPainel(self):
        self.page.dialog = self.__desiner
        self.__desiner.open = True
        self.page.update()

    def openPopUp(self,msg,cor):
        self.pop = PopUp(msg,cor).build()
        
        self.page.snack_bar = self.pop
        self.page.snack_bar.open = True
        self.page.update()

    def get(self):
        return self.__titulo