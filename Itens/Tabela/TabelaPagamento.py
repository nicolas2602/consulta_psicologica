import flet as ft
from Itens.components.Carregamento import Carregamento
from modulos.Check.VerificadorData import VerificadorData
import bd.funcao.pagamento as pg
from Itens.Painel.PainelPagamento import PainelPagamento
from time import sleep,strftime

class TabelaPagamento(ft.UserControl):
    ''' Criar a Tabela com os dados do banco.
        Funções atribuidas: Editar Agendamento
    '''

    def __init__(self,page):
        self.page = page
        self.carregamentoEditar = Carregamento(self.page,"Salvando Alterações...")
        self.carregamentoExcluir = Carregamento(self.page,"Excluindo Dados...")
        self.painelEditar = PainelPagamento(self.page,"Editar Pagamento", self.Salvar)

    def build(self):
        #Pegando dados Iniciais do Banco
        #data = strftime('%Y-%m-%d')
        self.dados = pg.pesquisarSemData('','')
        print(self.dados)
        # [(1, 2, datetime.date(2022, 9, 22), datetime.timedelta(seconds=64800), 'Ze', 'Buscape', Decimal('50.00'), Decimal('10.00'), Decimal('11.00'), datetime.date(2023, 11, 22), 1, 'Pix', 1, 'Concluído')],

        self.desiner =ft.Column([ ft.DataTable(
            border=ft.border.all(3,ft.colors.BLACK),
            border_radius= 10,
            vertical_lines= ft.border.BorderSide(1,'black'),
            heading_row_color= ft.colors.GREY_300,
            column_spacing=23,
            columns=[
                #ft.DataColumn(ft.Text('Id',selectable=True)),
                ft.DataColumn(ft.Row([ft.Text('Data_Hora',selectable=True),ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN_ROUNDED,on_click= self.invertTable)])),
                ft.DataColumn(ft.Text('Nome_Paciente',selectable=True)),
                ft.DataColumn(ft.Text("Valor",selectable=True)),
                ft.DataColumn(ft.Text("Desconto",selectable=True)),
                ft.DataColumn(ft.Text("Acréscimo",selectable=True)),
                ft.DataColumn(ft.Text("Total",selectable=True)),
                ft.DataColumn(ft.Text("Data_Pagamento",selectable=True)),
                ft.DataColumn(ft.Text("Tipo",selectable=True)),
                ft.DataColumn(ft.Text("Status",selectable=True)),
                ft.DataColumn(ft.Text("Ação",selectable=True)),
            ],
            rows=[],
        )],expand= True,width=1400, horizontal_alignment= ft.CrossAxisAlignment.CENTER, scroll= ft.ScrollMode.ALWAYS,)
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

        data2 = VerificadorData(lista[9]).verificar()
        if (data2[0]):
            data2 = data2[1].strftime('%d/%m/%Y')
        else:
            data2 = None

        total = (float(lista[6]) - float(lista[7]) + float(lista[8]))

        self.desiner.controls[0].rows.append((ft.DataRow(
            cells=[
                #ft.DataCell(ft.Text(lista[0],selectable=True)),                             # id
                ft.DataCell(ft.Text(value=data+' as '+str(lista[3])[0:5],selectable=True)), # Data e Hora
                ft.DataCell(ft.Text(value=lista[4]+' '+lista[5],selectable=True)),          # Nome e Sobrenome
                ft.DataCell(ft.Text(lista[6],selectable=True)),                             # Valor
                ft.DataCell(ft.Text(lista[7],selectable=True)),                             # Desconto
                ft.DataCell(ft.Text(lista[8],selectable=True)),                             # Acrescimo
                ft.DataCell(ft.Text((f'{total:.2f}'),selectable=True)),                     # Total
                ft.DataCell(ft.Text(value=data2,selectable=True)),                          # Data Pg
                ft.DataCell(ft.Text(lista[11],selectable=True)),                            # Forma pg
                ft.DataCell(ft.Text(lista[13],selectable=True)),                            # Status pg
                ft.DataCell(ft.IconButton(icon=ft.icons.EDIT, on_click= lambda e: self.openPainelEditar(lista))),
            ]))
        )    

    def invertTable(self,e):
        self.dados.reverse()
        self.montaTabela()

    def openPainelEditar(self, lista):
        data = VerificadorData(lista[9]).verificar()
        print(lista[9])
        if (data[0] == True):
            data = data[1]
            data = data.strftime('%d/%m/%Y')
        else:
            data = ''

        '''Abre o Campo de Editar com os dados pré preenchidos'''
        self.painelEditar.setPaine(lista[0],lista[7],lista[8],data,lista[11],lista[13])
        #### Abretura do painel de Edição ####
        self.painelEditar.openPainel()

    def Salvar(self,e):
        # Dedicado ao Novo Cadastro
        '''Função e pega as informações do campo Novo cadastro e envia ao banco de dados.'''

        x = self.painelEditar.getValue()
        print(x)
        self.painelEditar.fechar(e)
        sleep(0.3)

        #### Tela de carregamento ####
        self.carregamentoEditar.openCarregamento(e)

        #### Variavel de Controle ####

        Carregando = True
        msg = "Pagamento editado com Sucesso"
        cor = ft.colors.GREEN_700

        #'id':'data':'desconto':'acrescimo':'formaPagamento':'statusPatamento':
        while Carregando:
            print(x['data'])
            héValido = VerificadorData(x['data']).verificar()

            if(héValido[0]):
                
                data = héValido[1]
                pg.update(x['id'],x['desconto'],x['acrescimo'],data,x['statusPatamento'][0],x['formaPagamento'][0])
                self.dados = pg.pesquisarSemData('','')
                self.montaTabela()
                self.painelEditar.resetValue()
                
            else:
                msg = héValido[1] # retorna msg de erro
                cor = ft.colors.RED_700

            sleep(1)
            Carregando = False

        self.carregamentoEditar.closeCarregamento(e)
        #### Fim do Carregamento ####

        self.painelEditar.openPopUp(msg, cor)
        self.page.update()

        