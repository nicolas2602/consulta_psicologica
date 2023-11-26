import flet as ft
from  Itens.Formulario.VisualAnotacao import VisualAnotacao
from  Itens.Formulario.NomeDataAnotação import NomeDataAnotação
from  Itens.components.buttons.ActionButton import ActionButton
from  Itens.Painel.PopUp import PopUp


class PainelVisualizacaoAnotacoes(ft.UserControl):

    '''Abre o Formulario de Edição para o Pagamento com botões de comfimação'''

    def __init__(self,page,titulo = None):

        self.page = page
        self.__titulo = titulo

        self.__formAnotacao = VisualAnotacao(self.page)
 
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
            ],width=600)
        )

    def build(self):
        return self.__designer

    def setPaine(self, Nome=None, SobreNome=None, data=None, hora=None, titulo = None, anotacao=None):
        '''Envia as informações para o formulario, normalmente usado como auto preenchimento da função editar.'''
        self.__NomeDataAnota.setValue(Nome,SobreNome,data,hora)
        self.__formAnotacao.setValue(titulo,anotacao)
        self.__designer = self.__designer
        self.page.update()
 
    def openPainel(self):
        self.page.dialog = self.__designer
        self.__designer.open = True
        self.page.update()
