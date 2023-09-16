import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.Campo.CampoFormularioSenha import CampoFormularioSenha
from Itens.components.buttons.IconButton import IconButton
from Itens.components.buttons.ActionButton import ActionButton

class Logging(ft.UserControl):

    def __init__(self, page, fLogar):

        self.page = page

        self.campoLog = CampoFormulario("Login")
        self.campoSn = CampoFormularioSenha("Senha",None,None,fLogar)
        self.iconBotao = IconButton(ft.icons.VISIBILITY, ft.colors.BLACK54, self.visualizaSenha)
        self.LogBotao = ActionButton("Login",ft.colors.PRIMARY, None, fLogar)

        self.designer = ft.Container(
            content= ft.Column(
                controls = [
                    ft.Icon(ft.icons.SELF_IMPROVEMENT_OUTLINED,color=ft.colors.GREEN_900,size=40),
                    ft.Text("PsicoTech",style=ft.TextThemeStyle.TITLE_LARGE),
                    self.campoLog.build(),
                    ft.Row([self.campoSn.build(),self.iconBotao.build()]),
                    self.LogBotao.build()
                ],
                expand=True,
                horizontal_alignment= "Center"
            ),
            border_radius=10,
            border=ft.border.all(2, ft.colors.GREEN_900),
            padding=10,
            width = 380,
            height= 300
        )

    def build(self):
        return ft.Row(
            [self.designer],
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER, expand=True)
        
    
    def visualizaSenha(self,e):
        result = self.campoSn.getPassVisual()
        if(result):
            self.campoSn.setPassVisual(False)
        else:
            self.campoSn.setPassVisual(True)

        self.page.update()

    def getValue(self):
        return {
            'login':self.campoLog.getValue(),
            'senha':self.campoSn.getValue()
            }
    
    def limpar(self):
        self.campoLog.setValue()
        self.campoSn.setValue()