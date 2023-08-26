
from Itens.Painel.Painel import Painel
import flet as ft

class Tabela(ft.UserControl):

    def __init__(self,page):
        self.page = page
        self.painel = Painel(self.page,"Editar Cadastro")


    def build(self):

        self.dados = [(1,'Eduardo','Silva','edu@gmail.com', 1992929292),(2,'Lucas','NãoSei','lucas@gmail.com', 19983553333), (3,'Caio','NãoSei','caio@gmail.com', 1932233228)]

        self.desiner =ft.Column([ ft.DataTable(
            border=ft.border.all(3,ft.colors.BLACK),
            border_radius= 10,
            vertical_lines= ft.border.BorderSide(1,'black'),
            heading_row_color= ft.colors.GREY_300,
            #height=400,
            #expand=True,
            columns=[
                ft.DataColumn(ft.Text('Id',selectable=True)),
                ft.DataColumn(ft.Row([ft.Text('Nome',selectable=True),ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN_ROUNDED,on_click= self.invertTable)])),
                #ft.DataColumn(ft.Text('Sobrenome',selectable=True)),
                ft.DataColumn(ft.Text('E-mail',selectable=True)),
                ft.DataColumn(ft.Text('Telefone',selectable=True),numeric=True),
                ft.DataColumn(ft.Text("Ação",selectable=True)),
            ],
            rows=[],
        )],expand= True, horizontal_alignment= ft.CrossAxisAlignment.CENTER, scroll= ft.ScrollMode.ALWAYS,)
        self.montaTabela()

        return self.desiner
    
    def montaTabela(self):
        for d in self.dados:
            self.tabela(d)
            self.page.update()

    def tabela(self,lista):
        self.desiner.controls[0].rows.append((ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(lista[0],selectable=True)),
                ft.DataCell(ft.Text(value=lista[1]+' '+lista[2],selectable=True)),
                #ft.DataCell(ft.Text(lista[2],selectable=True)),
                ft.DataCell(ft.Text(lista[3],selectable=True)),
                ft.DataCell(ft.Text(lista[4],selectable=True)),
                ft.DataCell(ft.Row([ft.IconButton(icon=ft.icons.EDIT, on_click= lambda e: self.getID(lista[0])),ft.VerticalDivider(),ft.IconButton(icon=ft.icons.DELETE,icon_color="red")])),
                
            ]))
        )
        self.page.update()

    def getID(self,id):
        print(id)
        self.openPainel(id - 1)
        self.page.update()
        

    def openPainel(self, id):
        self.x = self.dados[id]
        print(self.x)
        self.painel.setPaine(self.x[0],self.x[1],self.x[2],self.x[3],self.x[4])

        self.page.dialog = self.painel.build()
        self.painel.build().open = True
        self.page.update()
        

    def invertTable(self,e):
        self.dados.reverse()
        self.desiner.controls[0].rows=[]
        self.montaTabela()
        self.page.update()

    
