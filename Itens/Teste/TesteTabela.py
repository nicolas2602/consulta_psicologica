
from Itens.Painel.Painel import Painel
import flet as ft

class Teste(ft.UserControl):

    def build(self):
        
        self.dados = [(1,'Eduardo','edu@gmail.com', 1992929292),(2,'Lucas','lucas@gmail.com', 19983553333), (3,'Caio','caio@gmail.com', 1932233228)]

        self.desiner = self.montaTabela()

        return self.desiner



    def montaTabela(self):

        tabela = ft.DataTable(
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
        
        itens = []
        for dados in self.dados:

            #teste obj pega ID
            x = Painel()

            itens.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(dados[0])),
                    ft.DataCell(ft.Text(dados[1])),
                    ft.DataCell(ft.Text(dados[2])),
                    ft.DataCell(ft.Text(dados[3])),
                    ft.DataCell(ft.Row([ft.IconButton(icon=ft.icons.EDIT, on_click= x.openPainel),ft.VerticalDivider(),ft.IconButton(icon=ft.icons.DELETE,icon_color="red")])),
                    
                ]
            )
            )

        tabela.rows = itens

        return tabela
    

        def openPainel(self,e):
            self.page.dialog = self.addCadastro.build()
            self.addCadastro.build().open = True
            self.page.update()