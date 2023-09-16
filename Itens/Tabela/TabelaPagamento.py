import flet as ft
from Itens.components.Carregamento import Carregamento
from modulos.Check.VerificadorData import VerificadorData
from Itens.Painel.Checagem import Checagem
import bd_pagamento.pagamento as pg
from time import sleep,strftime

class TabelaPagamento(ft.UserControl):
    ''' Criar a Tabela com os dados do banco.
        Funções atribuidas: Editar Agendamento
    '''

    def __init__(self,page):
        self.page = page
        #self.painelEditar = PainelAgendamento(self.page,"Editar Cadastro", self.Salvar) # painel para Editar cadastro
        self.carregamentoEditar = Carregamento(self.page,"Salvando Alterações...")
        self.carregamentoExcluir = Carregamento(self.page,"Excluindo Dados...")


    def build(self):
        #Pegando dados Iniciais do Banco
        #data = strftime('%Y-%m-%d')
        self.dados = pg.pesquisarSemData('','')
        #print(self.dados) # [(1, 1, datetime.date(2023, 8, 21), datetime.timedelta(seconds=50400), 'Nicolas', 'Yonekawa', Decimal('45.00'), datetime.date(2023, 11, 22), 1, 'Pix', 1, 'Concluído'),

        self.desiner =ft.Column([ ft.DataTable(
            border=ft.border.all(3,ft.colors.BLACK),
            border_radius= 10,
            vertical_lines= ft.border.BorderSide(1,'black'),
            heading_row_color= ft.colors.GREY_300,
            columns=[
                ft.DataColumn(ft.Text('Id',selectable=True)),
                ft.DataColumn(ft.Row([ft.Text('Data_Hora',selectable=True),ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN_ROUNDED,on_click= self.invertTable)])),
                ft.DataColumn(ft.Text('Nome_Paciente',selectable=True)),
                ft.DataColumn(ft.Text("Valor",selectable=True)),
                ft.DataColumn(ft.Text("Data_Pagamento",selectable=True)),
                ft.DataColumn(ft.Text("Tipo",selectable=True)),
                ft.DataColumn(ft.Text("Status",selectable=True)),
                ft.DataColumn(ft.Text("Ação",selectable=True)),
            ],
            rows=[],
        )],expand= True, horizontal_alignment= ft.CrossAxisAlignment.CENTER, scroll= ft.ScrollMode.ALWAYS,)
        self.montaTabela()

        return self.desiner

    def montaTabela(self):
        '''Função responsavel em criar ou atualizar a tabela.'''
        self.desiner.controls[0].rows=[]
        for d in self.dados:
            self.__tabela(d)
            self.page.update()


    def __tabela(self,lista):
        data = lista[2].strftime('%d/%m/%Y')
        self.desiner.controls[0].rows.append((ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(lista[0],selectable=True)),
                ft.DataCell(ft.Text(value=data+' as '+str(lista[3])[0:5],selectable=True)),
                ft.DataCell(ft.Text(value=lista[4]+' '+lista[5],selectable=True)),
                ft.DataCell(ft.Text(lista[6],selectable=True)),
                ft.DataCell(ft.Text(lista[7],selectable=True)),
                ft.DataCell(ft.Text(lista[9],selectable=True)),
                ft.DataCell(ft.Text(lista[11],selectable=True)),
                #ft.DataCell(ft.Row([ft.IconButton(icon=ft.icons.EDIT, on_click= lambda e: self.openPainel(lista[0])),ft.VerticalDivider(),ft.IconButton(icon=ft.icons.DELETE,icon_color="red",on_click= lambda e: self.deletar(lista[0]))])),
                ft.DataCell(ft.Row([ft.IconButton(icon=ft.icons.EDIT,)])),
            ]))
        )    

    def invertTable(self,e):
        self.dados.reverse()
        self.montaTabela()