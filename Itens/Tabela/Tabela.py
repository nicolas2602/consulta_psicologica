
from Itens.Painel.Painel import Painel
from Itens.Painel.Checagem import Checagem
from bd.funcao.cliente import *
from time import sleep
import flet as ft

class Tabela(ft.UserControl):
    ''' Criar a Tabela com os dados do banco.
        Funções atribuidas: Editar Cadastro e Excluir Cadastro
    '''

    def __init__(self,page):
        self.page = page
        self.painel = Painel(self.page,"Editar Cadastro", self.Salvar) # painel para Editar cadastro

    def build(self):
        #Pegando dados Iniciais do Banco
        self.dados = select(f"SELECT * FROM cliente") 

        self.desiner =ft.Column([ ft.DataTable(
            border=ft.border.all(3,ft.colors.BLACK),
            border_radius= 10,
            vertical_lines= ft.border.BorderSide(1,'black'),
            heading_row_color= ft.colors.GREY_300,
            columns=[
                ft.DataColumn(ft.Text('Id',selectable=True)),
                ft.DataColumn(ft.Row([ft.Text('Nome',selectable=True),ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN_ROUNDED,on_click= self.invertTable)])),
                ft.DataColumn(ft.Text('E-mail',selectable=True)),
                ft.DataColumn(ft.Text('Telefone',selectable=True),numeric=True),
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
        self.desiner.controls[0].rows.append((ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(lista[0],selectable=True)),
                ft.DataCell(ft.Text(value=lista[1]+' '+lista[2],selectable=True)),
                ft.DataCell(ft.Text(lista[3],selectable=True)),
                ft.DataCell(ft.Text(lista[4],selectable=True)),
                ft.DataCell(ft.Row([ft.IconButton(icon=ft.icons.EDIT, on_click= lambda e: self.openPainel(lista[0])),ft.VerticalDivider(),ft.IconButton(icon=ft.icons.DELETE,icon_color="red",on_click= lambda e: self.deletar(lista[0]))])),
                
            ]))
        )
        self.page.update()
        

    def openPainel(self, id):
        '''Abre o Campo de Editar com os dados pré preenchidos'''

        self.x = select(f"SELECT * FROM cliente WHERE IdCliente = {id}")
        self.painel.setPaine(self.x[0][0],self.x[0][1],self.x[0][2],self.x[0][3],self.x[0][4])
        #### Abretura do painel de Edição ####
        self.page.dialog = self.painel.build()
        self.painel.build().open = True
        self.page.update()
    

    def invertTable(self,e):
        self.dados.reverse()
        self.montaTabela()
        self.page.update()


    def Salvar(self,e):
        '''Função dedicada a enviar dados editados ao banco.'''

        #### Enviar dados ao Banco ####
        x = self.painel.getValue()
        update(x['id'],x['nome'],x['sobrenome'],x['email'],x['telefone'])
        self.painel.Cancelar(e)

        #### Mostra msg ao usuario ####
        self.painel.openPopUp("Cadastro Atualizado com Sucesso", ft.colors.GREEN_700)

        #### Atualiza a tabela ####
        self.dados = select(f"SELECT * FROM cliente")
        self.montaTabela()


    def deletar(self,id):
        '''Deleta o dado da Tabela'''
        #### pesquisa o ID no banco ####
        self.x = select(f"SELECT * FROM cliente WHERE IdCliente = {id}")

        #### Checa se vai excluir (sim ou não / True or False)
        self.checa = Checagem(self.page,f"Deseja deletar o cadastro do {self.x[0][1]} {self.x[0][2]}?")
        resultado = self.checa.checar()

        #### Se True => Ele Excluirá
        if(resultado):
            delete(id)
            sleep(1)
            self.painel.openPopUp("Cadastro deletado com Sucesso!", ft.colors.GREEN_700)
            #### Atualiza a Tabela ####
            self.dados = select(f"SELECT * FROM cliente")
            self.montaTabela()
        