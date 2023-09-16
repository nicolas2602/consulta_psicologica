import flet as ft
from Itens.components.Carregamento import Carregamento
from Itens.Painel.PainelAgendamento import PainelAgendamento
from modulos.Check.VerificadorData import VerificadorData
from Itens.Painel.Checagem import Checagem
import bd_agend.agendamento as ag
import bd_pagamento.pagamento as pg
from time import sleep,strftime

class TabelaAgendamento(ft.UserControl):
    ''' Criar a Tabela com os dados do banco.
        Funções atribuidas: Editar Agendamento e Excluir Agendamento
    '''

    def __init__(self,page):
        self.page = page
        self.painelEditar = PainelAgendamento(self.page,"Editar Cadastro", self.Salvar) # painel para Editar cadastro
        self.carregamentoEditar = Carregamento(self.page,"Salvando Alterações...")
        self.carregamentoExcluir = Carregamento(self.page,"Excluindo Dados...")


    def build(self):
        #Pegando dados Iniciais do Banco
        data = strftime('%Y-%m-%d')
        self.dados = ag.pesquisaData(data)
        #print(self.dados) # [(7, '08/09/2023', '12:00', 8, 'Teste', 'FinalTeste'), (5, '08/09/2023', '19:00', 2, 'Gabriel', 'Martins')]

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


    def __tabela(self,lista):
        
        self.desiner.controls[0].rows.append((ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(lista[0],selectable=True)),
                ft.DataCell(ft.Text(lista[1],selectable=True)),
                ft.DataCell(ft.Text(str(lista[2])[0:5],selectable=True)),
                ft.DataCell(ft.Text(value=f"{lista[4]} {lista[5]}",selectable=True)),
                ft.DataCell(ft.Row([ft.IconButton(icon=ft.icons.EDIT, on_click= lambda e: self.openPainelEditar(lista)),ft.VerticalDivider(),ft.IconButton(icon=ft.icons.DELETE,icon_color="red",on_click= lambda e: self.deletar(lista[0]))])),
            ]))
        )


    def invertTable(self,e):
        self.dados.reverse()
        self.montaTabela()
        self.page.update()

    def openPainelEditar(self, lista):
        '''Abre o Campo de Editar com os dados pré preenchidos'''
        nome = f"{lista[4]} {lista[5]}"
        self.painelEditar.setPaine(lista[0],lista[3],nome,lista[1],lista[2])

        #### Abretura do painel de Edição ####
        self.painelEditar.openPainelEditar()


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
        msg = "Consulta agendada com Sucesso"
        cor = ft.colors.GREEN_700


        while Carregando:

            héValido = VerificadorData(x['data']).verificar()

            if(héValido[0]):
                if(x['hora'] != ''):
                    data = héValido[1]
                    ag.update(x['id'],data,x['hora'],int(x['idNome']))
                    self.dados = ag.pesquisaData(héValido[1])
                    self.montaTabela()
                    self.painelEditar.resetValue()
                else:
                    msg = "Hora Invalida"
                    cor = ft.colors.RED_700
            else:
                msg = héValido[1] # retorna msg de erro
                cor = ft.colors.RED_700

            sleep(1)
            Carregando = False

        self.carregamentoEditar.closeCarregamento(e)
        #### Fim do Carregamento ####

        self.painelEditar.openPopUp(msg, cor)
        self.page.update()


    def deletar(self,id):
        '''Deleta o dado da Tabela'''

        #### pesquisa o ID no banco ####
        self.x = ag.pesquisaID(id)
        dados = self.x[0]

        #### Checa se vai excluir (sim ou não / True or False)
        self.checa = Checagem(self.page,f"Deseja deletar a consulta agendada do {dados[4]} {dados[5]} do dia {dados[1]} as {dados[2]}?")
        resultado = self.checa.checar()

        #### Se True => Ele Excluirá
        if(resultado):

            self.carregamentoExcluir.openCarregamento(self)
            carregando = True

            while carregando:
                pg.delete(id)
                sleep(0.5)
                ag.delete(id)
                sleep(0.5)
                
                #### Atualiza a Tabela ####
                self.dados = ag.pesquisaData(strftime("%Y-%m-%d"))
                self.montaTabela()
                carregando = False

            self.carregamentoExcluir.closeCarregamento(self)
            self.painelEditar.openPopUp("Cadastro deletado com Sucesso!", ft.colors.GREEN_700)