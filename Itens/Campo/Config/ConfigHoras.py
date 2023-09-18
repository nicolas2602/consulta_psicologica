import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.Campo.CampoDrop import CampoDrop
from Itens.components.buttons.ActionButton import ActionButton

class ConfigHoras(ft.UserControl):
    def __init__(self,page):
        self.page = page

        self.horaInicio = CampoFormulario("Horário Inicial",'07:00')
        self.horaInicio.setNaoAlter(True)

        self.horaFinal = CampoFormulario("Horário Final","17:00")
        self.horaFinal.setNaoAlter(True)

        self.horaInicioAlmoco = CampoFormulario("Horário Inicial do Intervalo")
        self.horaInicioAlmoco.setNaoAlter(True)

        self.horaFinalAlmoco = CampoFormulario("Horário Final do Intervalo")
        self.horaFinalAlmoco.setNaoAlter(True)

        self.horaDaSessao = CampoDrop("Tempo da Consulta em minutos",['30','35','40','45','50','55','60'],300)
        self.horaDaSessao.setValue('60')
        self.horaDaSessao.setNaoAlter(True)

        self.botaoEditar = ActionButton('Editar',ft.colors.GREY_800,ft.icons.EDIT,self.editar)
        self.botaoCancelar = ActionButton('Cancelar',ft.colors.RED,ft.icons.CANCEL_OUTLINED,self.cancelar)
        self.botaoSalvar = ActionButton('Salvar',ft.colors.GREEN_800,ft.icons.FILE_DOWNLOAD_DONE_ROUNDED,self.cancelar)

        self.designerBotao = ft.Row(controls=[self.botaoEditar.build()],alignment=ft.MainAxisAlignment.SPACE_EVENLY,width=300)

        self.designer = ft.Column(
            controls = [
                ft.Row([ft.Icon(ft.icons.WORK_HISTORY,color=ft.colors.GREEN_800),ft.Text("Horário de Trabalho",style=ft.TextThemeStyle.HEADLINE_SMALL)]),
                ft.Row([self.horaInicio.build(),self.horaFinal.build()]),
                ft.Row([ft.Icon(ft.icons.FREE_BREAKFAST,color=ft.colors.GREEN_800),ft.Text("Horário de Pausa",style=ft.TextThemeStyle.HEADLINE_SMALL)]),
                ft.Row([self.horaInicioAlmoco.build(),self.horaFinalAlmoco.build()]),
                ft.Row([ft.Icon(ft.icons.TIMER,color=ft.colors.GREEN_800),ft.Text("Tempo da Consulta",style=ft.TextThemeStyle.HEADLINE_SMALL)]),
                ft.Row([self.horaDaSessao.build(),self.designerBotao])
            ],alignment="Center",height=350,width=600
        )

    def build(self):
        return ft.Column([ft.Divider(opacity=0),self.designer],spacing=10,expand=True,horizontal_alignment="Center",alignment="Center",scroll=ft.ScrollMode.ALWAYS)
    
    def editar(self,e):
        self.horaInicio.setNaoAlter()
        self.horaFinal.setNaoAlter()
        self.horaInicioAlmoco.setNaoAlter()
        self.horaFinalAlmoco.setNaoAlter()
        self.horaDaSessao.setNaoAlter()

        self.designerBotao.controls.pop()
        self.designerBotao.controls.append(self.botaoSalvar.build())
        self.designerBotao.controls.append(self.botaoCancelar.build())
        self.page.update()
    
    def cancelar(self,e):
        self.horaInicio.setNaoAlter(True)
        self.horaFinal.setNaoAlter(True)
        self.horaInicioAlmoco.setNaoAlter(True)
        self.horaFinalAlmoco.setNaoAlter(True)
        self.horaDaSessao.setNaoAlter(True)

        self.designerBotao.controls.pop()
        self.designerBotao.controls.pop()
        self.designerBotao.controls.append(self.botaoEditar.build())
        self.page.update()