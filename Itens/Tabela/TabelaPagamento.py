import flet as ft
from Itens.components.Carregamento import Carregamento
from modulos.Check.VerificadorData import VerificadorData
from Itens.Painel.Checagem import Checagem
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
        #self.dados = ag.pesquisaData(data)
        #print(self.dados) # [(7, '08/09/2023', '12:00', 8, 'Teste', 'FinalTeste'), (5, '08/09/2023', '19:00', 2, 'Gabriel', 'Martins')]

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
        #self.montaTabela()

        return self.desiner
    


    def invertTable(self,e):
        pass
        # self.dados.reverse()
        # self.montaTabela()
        # self.page.update()