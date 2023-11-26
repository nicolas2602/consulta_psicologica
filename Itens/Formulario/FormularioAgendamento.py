import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.Campo.CampoDrop import CampoDrop
from modulos.ListaHorasDisponiveis import ListaHorasDisponiveis
from modulos.ListaHorarios import ListaHorarios
from modulos.Check.VerificadorData import VerificadorData

class FormularioAgendamento(ft.UserControl):
    '''Cria um conjunto de capos de digitação para o Agendamento.'''

    def __init__(self,page, idBD = None, id_Nome = None, nome = None, data = None, hora = None):
        self.page = page
        self.__id = idBD

        self.__idNome = id_Nome
        self.__form_Nome = CampoFormulario("Nome",nome,)
        self.__form_Nome.setNaoAlter(True)

        self.__form_Data = CampoFormulario("Data",data)
        self.__form_Data.setPlaceHolder("Ex: 27/06/1991")
        self.__form_Data.setOnChange(self.criarHoras)

        self.__form_Hora = CampoDrop("Hora",ListaHorarios().criarListaHorarios())
        self.__form_Hora.setNaoAlter(True)
        self.__hora = hora

        self.__desiner = ft.Column(controls=[
            self.__form_Nome.build(),
            self.__form_Data.build(),
            self.__form_Hora.build(),
        ])

    def build(self):
        return self.__desiner
    
    def criarHoras(self,e):
        data = self.__form_Data.getValue()
        hora = self.__form_Hora.getValue()
        print(data,hora)
        dataCk= VerificadorData(data).verificar()

        if dataCk[0]:

            self.__form_Hora.setNaoAlter(False)
            self.__form_Hora.setLista(ListaHorasDisponiveis().listaHorasDisponiveis(dataCk[1]))
            
        else:
            self.__form_Hora.setNaoAlter(True)
                
        self.page.update()

    def setValue(self,id=None,id_nome = None,nome=None,data=None,hora = None):
        '''Seta os valores do Campo (auto preenchimento).'''
        self.__id = id
        self.__idNome = id_nome
        self.__form_Nome.setValue(nome)
        self.__form_Data.setValue(data)
        self.__form_Hora.setValue(hora)
        self.__form_Hora.setLista(ListaHorasDisponiveis(hora).listaHorasDisponiveis((VerificadorData(data).verificar())[1]))
        self.__form_Hora.setNaoAlter(False)

    def getValue(self):
        return {
            'id':self.__id,
            'idNome':self.__idNome,
            'nome': self.__form_Nome.getValue(),
            'data':self.__form_Data.getValue(),
            'hora':self.__form_Hora.getValue(),
        }
    
    def setNome(self,id,nome):
        self.__idNome = id
        self.__form_Nome.setValue(nome)
    