import flet as ft
from Itens.components.Carregamento import Carregamento
from Itens.Painel.PainelAnotacoes import PainelAnotacoes
from Itens.Painel.PainelVisualizacaoAnotacoes import PainelVisualizacaoAnotacoes
from modulos.Criptografia import Criptografia
import bd.funcao.anotacao_consulta as ac
from time import sleep,strftime

class TabelaAnotacoes(ft.UserControl):
    ''' Criar a Tabela com os dados do banco.
        Funções atribuidas: Editar Anotações
    '''

    def __init__(self,page):
        self.page = page
        self.painelEditar = PainelAnotacoes(self.page,"Anotações",self.Salvar) # painel para Editar cadastro 
        self.visualisacao = PainelVisualizacaoAnotacoes(self.page,"Anotações") 
        self.carregamentoEditar = Carregamento(self.page,"Salvando Alterações...")

    def build(self):
        #Pegando dados Iniciais do Banco
        data = strftime('%Y-%m-%d')

        self.dados = ac.pesquisaAnotacoesData(data)
        # [(1, datetime.date(2022, 9, 22), datetime.timedelta(seconds=61200), 'Ze', 'Buscape', 'Titulo', 'Assunto 2')]

        self.desiner =ft.Column([ ft.DataTable(
            border=ft.border.all(3,ft.colors.BLACK),
            border_radius= 10,
            vertical_lines= ft.border.BorderSide(1,'black'),
            heading_row_color= ft.colors.GREY_300,
            columns=[
                ft.DataColumn(ft.Text('Id',selectable=True)),
                ft.DataColumn(ft.Row([ft.Text('Data e Hora',selectable=True),ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN_ROUNDED,on_click= self.invertTable)])),
                ft.DataColumn(ft.Text('Nome_Paciente',selectable=True)),
                ft.DataColumn(ft.Text("Titulo",selectable=True)),
                ft.DataColumn(ft.Text("Anotação",selectable=True)),
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
        data = lista[1].strftime('%d/%m/%Y')
        cript= Criptografia()
        
        self.desiner.controls[0].rows.append((ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(lista[0],selectable=True)),
                ft.DataCell(ft.Text(data+' as '+str(lista[2])[:-3],selectable=True)),
                ft.DataCell(ft.Text(value=f"{lista[3]} {lista[4]}",selectable=True)),
                ft.DataCell(ft.Text(value = cript.decodificar(lista[5]),selectable=True)),
                ft.DataCell(ft.Row([ft.IconButton(icon=ft.icons.EDIT_DOCUMENT,on_click= lambda e: self.openPainelEditar(lista)),
                                    ft.VerticalDivider(),
                                    ft.IconButton(icon=ft.icons.VISIBILITY,on_click= lambda e: self.openPainelVisualizar(lista)),]))
            ]))
        )


    def invertTable(self,e):
        self.dados.reverse()
        self.montaTabela()
        self.page.update()

    def openPainelEditar(self, lista):
        '''Abre o Campo de Editar com os dados pré preenchidos'''
        cript= Criptografia()
        self.painelEditar.setPaine(lista[0],lista[3],lista[4],lista[1],lista[2],cript.decodificar(lista[5]),cript.decodificar(lista[6]))

        #### Abretura do painel de Edição ####
        self.painelEditar.openPainel()

    def openPainelVisualizar(self, lista):
        '''Abre o Campo de Editar com os dados pré preenchidos'''
        cript= Criptografia()
        self.visualisacao.setPaine(lista[3],lista[4],lista[1],lista[2],cript.decodificar(lista[5]),cript.decodificar(lista[6]))

        #### Abretura do painel de Edição ####
        self.visualisacao.openPainel()

    def Salvar(self,e):
        # Dedicado ao Novo Cadastro
        '''Função e pega as informações do campo Novo cadastro e envia ao banco de dados.'''
        #### Variavel de Controle ####

        Carregando = True
        msg = "Consulta agendada com Sucesso"
        cor = ft.colors.GREEN_700

        x = self.painelEditar.getValue()
        if(x['qtdTxt']):
                
            self.painelEditar.fechar(e)
            sleep(0.3)

            #### Tela de carregamento ####
            self.carregamentoEditar.openCarregamento(e)

            #'id','titulo','anotacoes','qtdTxt'

            while Carregando:

                if(x['titulo'] != '' and x['anotacoes'] != ''):
                    ac.updateAnotacao(x['id'],x['anotacoes'],x['titulo'])
                    self.dados = ac.selectAnotacoesId(x['id'])
                    self.montaTabela()
                    self.painelEditar.resetValue()
                else:
                    msg = "Campo Titulo e Anotações, não podem estar vazios."
                    cor = ft.colors.RED_700
            

                sleep(1)
                Carregando = False

            self.carregamentoEditar.closeCarregamento(e)
            #### Fim do Carregamento ####

        else:
            msg = "Campo Anotações com quantidade de caracteres acima do permitito."  # retorna msg de erro
            cor = ft.colors.RED_700

        self.painelEditar.openPopUp(msg, cor)
        self.page.update()

