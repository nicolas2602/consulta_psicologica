
from Itens.Painel.Painel import Painel
import flet as ft

class Tabela(ft.UserControl):

    def __init__(self,page):
        self.page = page
        self.painel = Painel(self.page,"Editar Cadastro")


    def build(self):

        self.dados = [(1,'Eduardo','edu@gmail.com', 1992929292),(2,'Lucas','lucas@gmail.com', 19983553333), (3,'Caio','caio@gmail.com', 1932233228)]

        self.desiner = ft.DataTable(
            border=ft.border.all(3,ft.colors.BLACK),
            border_radius= 10,
            vertical_lines= ft.border.BorderSide(1,'black'),
            heading_row_color= ft.colors.GREY_300,
            #height=400,
            #expand=True,
            columns=[
                ft.DataColumn(ft.Text('Id')),
                ft.DataColumn(ft.Text('Nome')),
                ft.DataColumn(ft.Text('E-mail')),
                ft.DataColumn(ft.Text('Telefone'),numeric=True),
                ft.DataColumn(ft.Text("Ação")),
            ],
            rows=[],
        )
        self.montaTabela()

        return self.desiner
    
    def montaTabela(self):
        for d in self.dados:
            self.tabela(d)
            self.page.update()

    def tabela(self,lista):
        self.desiner.rows.append((ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(lista[0])),
                ft.DataCell(ft.Text(lista[1])),
                ft.DataCell(ft.Text(lista[2])),
                ft.DataCell(ft.Text(lista[3])),
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
        self.painel.setPaine(self.x[0],self.x[1],self.x[2],self.x[3])

        self.page.dialog = self.painel.build()
        self.painel.build().open = True
        self.page.update()
        


