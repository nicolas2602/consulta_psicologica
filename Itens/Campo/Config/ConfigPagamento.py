import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.Campo.CampoLista import CampoLista
from Itens.components.buttons.ActionButton import ActionButton
from  Itens.Painel.PopUp import PopUp
from bd.funcao.pagamento import listaFormaPg
from bd.funcao.usuario import valorFixo,updateValorFixo

class ConfigPagamento(ft.UserControl):

    def __init__(self,page):
        self.page = page

        self.valorDaConsulta = CampoFormulario("Valor",valorFixo()[0][0])
        self.valorDaConsulta.setNaoAlter(True)

        self.AddFormaPagamento = CampoFormulario("Forma")
        self.AddFormaPagamento.setNaoAlter(True)

        self.listaFormaPagamento = CampoLista(listaFormaPg(),300,120,print)
        self.listaFormaPagamento.addOpcoes()
        self.listaFormaPagamento.setNaoAlter(True)

        self.botaoEditarValor = ActionButton('Editar',ft.colors.GREY_800,ft.icons.EDIT,self.editarValor)
        self.botaoEditarFormaPg = ActionButton('Editar',ft.colors.GREY_800,ft.icons.EDIT,self.editarFormaPg)

        self.botaoCancelarValor = ActionButton('Cancelar',ft.colors.RED,ft.icons.CANCEL_OUTLINED,self.cancelarValor)
        self.botaoCancelarFormaPG = ActionButton('Cancelar',ft.colors.RED,ft.icons.CANCEL_OUTLINED,self.cancelarFormaPg)

        self.botaoSalvarValor = ActionButton('Salvar',ft.colors.GREEN_800,ft.icons.FILE_DOWNLOAD_DONE_ROUNDED,self.salvarValor)
        self.botaoSalvarFormaPG = ActionButton('Salvar',ft.colors.GREEN_800,ft.icons.FILE_DOWNLOAD_DONE_ROUNDED,self.cancelarFormaPg)
        
        self.designerBotaoValor = ft.Row(controls=[self.botaoEditarValor.build()],alignment=ft.MainAxisAlignment.SPACE_EVENLY,width=300)
        self.designerBotaoFormaPag = ft.Row(controls=[self.botaoEditarFormaPg.build()],alignment=ft.MainAxisAlignment.SPACE_EVENLY,width=300)

        self.designer = ft.Column(
            controls = [
                ft.Row([ft.Icon(ft.icons.MONEY_ROUNDED,color=ft.colors.GREEN_800),ft.Text("Valor da Consulta",style=ft.TextThemeStyle.HEADLINE_SMALL)]),
                ft.Row([self.valorDaConsulta.build()]),
                self.designerBotaoValor,
                ft.Row([ft.Icon(ft.icons.CREDIT_CARD,color=ft.colors.GREEN_800),ft.Text("Formas de pagamento",style=ft.TextThemeStyle.HEADLINE_SMALL)]),
                ft.Row([self.AddFormaPagamento.build()]),
                ft.Row([self.listaFormaPagamento.build()]),
                self.designerBotaoFormaPag
            ],alignment="Center",width=300,
        )


    def build(self):
        return ft.Column([ft.Divider(opacity=0),self.designer],spacing=10,expand=True,horizontal_alignment="Center",alignment="Center",scroll=ft.ScrollMode.ALWAYS)
    
    
    def openPopUp(self,msg,cor):
        '''Abre o msg informando o resultado da ação, Ex: enviado com Sucesso ou Banco de dados.'''
        self.pop = PopUp(msg,cor).build()    
        self.page.snack_bar = self.pop
        self.page.snack_bar.open = True
        self.page.update()


    def editarValor(self,e):
        self.valorDaConsulta.setNaoAlter()

        self.designerBotaoValor.controls.pop()
        self.designerBotaoValor.controls.append(self.botaoSalvarValor.build())
        self.designerBotaoValor.controls.append(self.botaoCancelarValor.build())
        self.page.update()

    def editarFormaPg(self,e):
        self.AddFormaPagamento.setNaoAlter()
        self.listaFormaPagamento.setNaoAlter()

        self.designerBotaoFormaPag.controls.pop()
        self.designerBotaoFormaPag.controls.append(self.botaoSalvarFormaPG.build())
        self.designerBotaoFormaPag.controls.append(self.botaoCancelarFormaPG.build())
        self.page.update()
    
    def cancelarValor(self,e):
        self.valorDaConsulta.setValue(valorFixo()[0][0])
        self.valorDaConsulta.setNaoAlter(True)

        self.designerBotaoValor.controls.pop()
        self.designerBotaoValor.controls.pop()
        self.designerBotaoValor.controls.append(self.botaoEditarValor.build())
        self.page.update()

    def cancelarFormaPg(self,e):
        self.AddFormaPagamento.setNaoAlter(True)
        self.listaFormaPagamento.setNaoAlter(True)

        self.designerBotaoFormaPag.controls.pop()
        self.designerBotaoFormaPag.controls.pop()
        self.designerBotaoFormaPag.controls.append(self.botaoEditarFormaPg.build())
        self.page.update()
    
    def salvarValor(self,e):
        valor =self.valorDaConsulta.getValue()
        updateValorFixo(valor)
        self.cancelarValor(e)
        self.openPopUp("Valor Salvo com Sucesso",ft.colors.GREEN_700)
        

