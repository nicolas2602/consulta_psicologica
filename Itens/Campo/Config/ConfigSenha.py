import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.Campo.CampoFormularioSenha import CampoFormularioSenha
from Itens.components.buttons.ActionButton import ActionButton
from Itens.components.buttons.IconButton import IconButton
from  Itens.Painel.PopUp import PopUp
from bd.funcao.usuario import selectUsuario,selectSenha,updateUsuarioSenha

class ConfigSenha(ft.UserControl):
    def __init__(self,page):
        self.page = page

        self.login = CampoFormulario("Login",selectUsuario()[0][0])
        self.login.setNaoAlter(True)

        self.senha = CampoFormularioSenha("Senha",selectSenha()[0][0],250)
        self.senha.setNaoAlter(True)

        self.iconBotao = IconButton(ft.icons.VISIBILITY, ft.colors.BLACK54, self.visualizaSenha)
        self.iconBotao.setNaoAlter(True)
        
        self.botaoEditar = ActionButton('Editar',ft.colors.GREY_800,ft.icons.EDIT,self.editar)
        self.botaoCancelar = ActionButton('Cancelar',ft.colors.RED,ft.icons.CANCEL_OUTLINED,self.cancelar)
        self.botaoSalvar = ActionButton('Salvar',ft.colors.GREEN_800,ft.icons.FILE_DOWNLOAD_DONE_ROUNDED,self.salvarLoginSenha)

        self.designerBotao = ft.Row(controls=[self.botaoEditar.build()],alignment=ft.MainAxisAlignment.SPACE_EVENLY,width=300,height=100)

        self.designer = ft.Column(
            controls = [
                ft.Row([ft.Icon(ft.icons.LOCK_PERSON,color=ft.colors.GREEN_800),ft.Text("Login do Usuario",style=ft.TextThemeStyle.HEADLINE_SMALL)]),
                ft.Row([self.login.build()]),
                ft.Row([ft.Icon(ft.icons.KEY,color=ft.colors.GREEN_800),ft.Text("Senha do Usuario",style=ft.TextThemeStyle.HEADLINE_SMALL)]),
                ft.Row([self.senha.build(),self.iconBotao.build()]),
                self.designerBotao
            ],alignment="Center",height=350,width=300
        )

    def build(self):
        return ft.Column([ft.Divider(opacity=0),self.designer],spacing=10,expand=True,horizontal_alignment="Center",alignment="Center",scroll=ft.ScrollMode.ALWAYS)
    
    def openPopUp(self,msg,cor):
        '''Abre o msg informando o resultado da ação, Ex: enviado com Sucesso ou Banco de dados.'''
        self.pop = PopUp(msg,cor).build()    
        self.page.snack_bar = self.pop
        self.page.snack_bar.open = True
        self.page.update()

    def editar(self,e):
        self.login.setNaoAlter()
        self.senha.setNaoAlter()
        self.iconBotao.setNaoAlter()

        self.designerBotao.controls.pop()
        self.designerBotao.controls.append(self.botaoSalvar.build())
        self.designerBotao.controls.append(self.botaoCancelar.build())
        self.page.update()
    
    def cancelar(self,e):
        self.login.setValue(selectUsuario()[0][0])
        self.senha.setValue(selectSenha()[0][0])
        self.login.setNaoAlter(True)
        self.senha.setPassVisual(True)
        self.senha.setNaoAlter(True)
        self.iconBotao.setNaoAlter(True)

        self.designerBotao.controls.pop()
        self.designerBotao.controls.pop()
        self.designerBotao.controls.append(self.botaoEditar.build())
        self.page.update()

    def visualizaSenha(self,e):
        result = self.senha.getPassVisual()
        if(result):
            self.senha.setPassVisual(False)
        else:
            self.senha.setPassVisual(True)

        self.page.update()

    def salvarLoginSenha(self,e):
        lg =self.login.getValue()
        sn =self.senha.getValue()
        updateUsuarioSenha(lg,sn)
        self.cancelar(e)
        self.openPopUp("O Login e Senha foi Salvo com Sucesso",ft.colors.GREEN_700)