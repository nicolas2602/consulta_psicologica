from  Itens.Formulario.Formulario import Formulario
import flet as ft

class Painel(ft.UserControl):

    def __init__(self,page,titulo = None, id =None, nome = None, email = None, Telefone = None):
        self.page = page

        self.__titulo = titulo
        
        self.__form = Formulario(id, nome, email, Telefone)
        
        self.__desiner = ft.AlertDialog(
            title=ft.Column(
            controls=[
                ft.Text(self.__titulo),
                self.__form.build(),
                ft.Row(
                    [
                        ft.FilledButton(text='Cancelar',on_click= self.fechar),
                        ft.FilledButton(text='OK',on_click= self.ok)
                    ]
                )   
            ]
            
        )
    
    )
    def build(self):
        return self.__desiner

    def setPaine(self,id =None, nome = None, email = None, Telefone = None):
        self.__form.setValue(id,nome,email,Telefone)
        # self.__desiner.title.controls[1] = self.__form
        self.page.update()

    def fechar(self,e):
        self.__desiner.open = False
        self.page.update()

    def ok(self,e):
        x = self.__form.get_value()
        print(x)
        self.fechar(e)
        
    def openPainel(self):
        self.page.dialog = self.__desiner
        self.__desiner.open = True
        self.page.update()

    def get(self):
        return self.__titulo