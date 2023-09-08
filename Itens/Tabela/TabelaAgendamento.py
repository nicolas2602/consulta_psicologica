import flet as ft
from Itens.components.Carregamento import Carregamento
import bd.funcao.cliente as cl
#from bd_agend.agendamento import select,update,delete
import bd_agend.agendamento as ag
from time import strftime

class TabelaAgendamento(ft.UserControl):
    ''' Criar a Tabela com os dados do banco.
        Funções atribuidas: Editar Agendamento e Excluir Agendamento
    '''

    def __init__(self,page):
        self.page = page
        #self.painel = Painel(self.page,"Editar Cadastro", self.Salvar) # painel para Editar cadastro
        self.carregamentoEditar = Carregamento(self.page,"Salvando Alterações...")
        self.carregamentoExcluir = Carregamento(self.page,"Excluindo Dados...")


    def build(self):
        #Pegando dados Iniciais do Banco
        self.dados = ag.select("SELECT * from agendamento_consulta ORDER BY dataAgendCon,horarioAgendCon;")
        #print(self.dados[0][2].strftime('%H:%M:%S'))
        #self.dados = [(1,'20/10/2023','10:00',1)]

        self.desiner =ft.Column([ ft.DataTable(
            border=ft.border.all(3,ft.colors.BLACK),
            border_radius= 10,
            vertical_lines= ft.border.BorderSide(1,'black'),
            heading_row_color= ft.colors.GREY_300,
            columns=[
                ft.DataColumn(ft.Text('Id_Agenda',selectable=True)),
                ft.DataColumn(ft.Row([ft.Text('Data',selectable=True),ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN_ROUNDED,on_click= self.invertTable)])),
                ft.DataColumn(ft.Text('Hora',selectable=True)),
                ft.DataColumn(ft.Text('Nome_Paciente',selectable=True)),
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


    def __tabela(self,lista): #(1,'20/10/2023','10:00',1)
        x = cl.select(f"SELECT nomeCliente,sobrenomeCliente FROM cliente WHERE IdCliente ={lista[3]}")
        
        self.desiner.controls[0].rows.append((ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(lista[0],selectable=True)),
                ft.DataCell(ft.Text(lista[1].strftime('%d/%m/%Y'),selectable=True)),
                ft.DataCell(ft.Text(str(lista[2])[0:5],selectable=True)),
                ft.DataCell(ft.Text(value=f"{x[0][0]} {x[0][1]}",selectable=True)),
                ft.DataCell(ft.Row([ft.IconButton(icon=ft.icons.EDIT, on_click= lambda e: print(lista[0])),ft.VerticalDivider(),ft.IconButton(icon=ft.icons.DELETE,icon_color="red",on_click= lambda e: print("deletar"))])),
            ]))
        )


    def invertTable(self,e):
        self.dados.reverse()
        self.montaTabela()
        self.page.update()