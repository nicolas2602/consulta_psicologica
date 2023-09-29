import flet as ft
from time import strftime
class NomeDataAnotação(ft.UserControl):

    def __init__(self,page,nome=None, sobreNome = None, data = None , hora = None):
        
        self.page = page
        self.nome = ft.Text(value=f'{nome} {sobreNome}',size=15,width=100)
        self.data = ft.Text(value=f'{data}',size=15)
        self.hora = ft.Text(value=f'{hora}',size=15)

    def build(self):
        
        return ft.Column([
            ft.Text('Nome do Paciente:',size=15,weight=ft.FontWeight.BOLD),
            ft.Row([ft.Icon(ft.icons.PERSON,color=ft.colors.GREEN_800),self.nome]),
            ft.Divider(),
            ft.Text('Data da Consulta:',size=15,weight=ft.FontWeight.BOLD),
            ft.Row([ft.Icon(ft.icons.CALENDAR_MONTH,color=ft.colors.GREEN_800),self.data]),
            ft.Row([ft.Icon(ft.icons.ACCESS_TIME,color=ft.colors.GREEN_800),self.hora])
        ])

    def setValue(self,nome=None, sobreNome = None, data = None , hora = None):
        '''Seta os valores do Campo (auto preenchimento).'''
        dt = data.strftime('%d/%m/%Y')
        self.nome.value = f'{nome} {sobreNome}'
        self.data.value = f'{dt}'
        self.hora.value = f'{str(hora)[:-3]}'
        self.page.update()