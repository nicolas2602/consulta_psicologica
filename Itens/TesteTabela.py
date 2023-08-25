
from Painel.Painel import Painel
import flet as ft

class Teste(ft.UserControl,ft.Page):
    def __init__(self,page):
        self.page = page

    def build(self):

        self.dados = [(1,'Eduardo','edu@gmail.com', 1992929292),(2,'Lucas','lucas@gmail.com', 19983553333), (3,'Caio','caio@gmail.com', 1932233228)]
        self.idClick =0
        self.desiner = self.montaTabela()
        #self.painel = Painel("Editar Cadastro")
        self.tabela()
        self.page.update()
        return self.desiner



    def montaTabela(self):

        self.t = ft.DataTable(
            border=ft.border.all(3,ft.colors.BLACK),
            border_radius= 10,
            vertical_lines= ft.border.BorderSide(1,'black'),
            heading_row_color= ft.colors.GREY_300,
            columns=[
                ft.DataColumn(ft.Text('Id')),
                ft.DataColumn(ft.Text('Nome')),
                ft.DataColumn(ft.Text('E-mail')),
                ft.DataColumn(ft.Text('Telefone'),numeric=True),
                ft.DataColumn(ft.Text("Ação")),
            ],
            rows=[],
        )

        return self.t
    
    def tabela(self):
        itens = []
        for d in self.dados:
            itens.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(d[0])),
                    ft.DataCell(ft.Text(d[1])),
                    ft.DataCell(ft.Text(d[2])),
                    ft.DataCell(ft.Text(d[3])),
                    ft.DataCell(ft.Row([ft.IconButton(icon=ft.icons.EDIT, on_click= self.criarPainel ),ft.VerticalDivider(),ft.IconButton(icon=ft.icons.DELETE,icon_color="red")])),
                    
                ]
                )
            )
        self.desiner.rows = itens
    


    def criarPainel(self):
        print(self.design.rows[0].cells[0])
        self.design.rows[0].cells[0]
        


    def criar(self,e,id):
        self.page.dialog = None
        self.id = id 
        self.page.dialog = self.id
        self.id.open = True
        self.page.update()