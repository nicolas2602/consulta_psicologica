import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.Campo.CampoDrop import CampoDrop

class FormularioAgendamento(ft.UserControl):
    '''Cria um conjunto de capos de digitação para o Agendamento.'''

    def __init__(self, idBD = None, id_Nome = None, nome = None, data = None, hora = None):

        self.__id = idBD

        self.__idNome = id_Nome
        self.__form_Nome = CampoFormulario("Nome",nome,)
        self.__form_Nome.setNaoAlter(True)

        self.__form_Data = CampoFormulario("Data",data)
        self.__form_Data.setPlaceHolder("Ex: 27/06/1991")

        self.__listaHora = ['06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00']
        self.__form_Hora = CampoDrop("Hora",self.__listaHora)
        

        self.__desiner = ft.Column(controls=[
            self.__form_Nome.build(),
            self.__form_Data.build(),
            self.__form_Hora.build(),
        ])

    def build(self):
        return self.__desiner


    def setValue(self,id=None,id_nome = None,nome=None,data=None,hora = None):
        '''Seta os valores do Campo (auto preenchimento).'''
        self.__id = id
        self.__idNome = id_nome
        self.__form_Nome.setValue(nome)
        self.__form_Data.setValue(data)
        self.__form_Hora.setValue(hora)

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
    