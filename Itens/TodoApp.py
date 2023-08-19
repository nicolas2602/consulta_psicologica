import flet as ft
from Itens.MenuPrincipal import MenuPrincipal
from Itens.Cadastro import Cadastro

class TodoApp(ft.UserControl):

    def build(self):

        self.menu = MenuPrincipal(self.cadastro, self.agendamentos,self.anotações,self.pagamentos)

        self.bodyCadastro = Cadastro(self)

        self.desiner =ft.Column(
                controls=[
                    self.menu.build(),
                    ft.Divider(color=ft.colors.GREEN_900),
                ]
            )
        

        return self.desiner

    def cadastro(self,e):
        if (len(self.desiner.controls) > 2):
            self.desiner.controls.pop(2)
            self.desiner.controls.append(ft.Column([self.bodyCadastro]))

        else:
            self.desiner.controls.append(ft.Column([self.bodyCadastro]))
        self.update()

    def agendamentos(self,e):
        if (len(self.desiner.controls) > 2):
            self.desiner.controls.pop(2)
            self.desiner.controls.append(ft.Column([ft.Text("Teste2")]))

        else:
            self.desiner.controls.append(ft.Column([ft.Text("Teste2")]))
        self.update()

    def anotações(self,e):
        pass

    def pagamentos(self,e):
        pass

        
    
        