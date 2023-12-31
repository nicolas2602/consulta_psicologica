import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario

class Formulario(ft.UserControl):
    '''Cria um conjunto de capos de digitação para o Cadastro.'''

    def __init__(self, idBD = None, nome = None, sobrenome = None, email = None, telefone = None):

        self.__id = idBD

        self.__form_Nome = CampoFormulario("Nome",nome)
        self.__form_Sobrenome = CampoFormulario("Sobrenome",sobrenome)
        self.__form_Email = CampoFormulario("E-mail",email)
        self.__form_Telefone = CampoFormulario("Telefone",telefone)


        self.__desiner = ft.Column(controls=[
            self.__form_Nome.build(),
            self.__form_Sobrenome.build(),
            self.__form_Email.build(),
            self.__form_Telefone.build()
        ])

    def build(self):
        return self.__desiner


    def setValue(self,id=None,nome=None,sobrenome=None,email=None,tel=None):
        '''Seta os valores do Campo (auto preenchimento).'''
        self.__id = id
        self.__form_Nome.setValue(nome)
        self.__form_Sobrenome.setValue(sobrenome)
        self.__form_Email.setValue(email)
        self.__form_Telefone.setValue(tel)

    def getValue(self):
        return {
            'id':self.__id,
            'nome': self.__form_Nome.getValue(),
            'sobrenome':self.__form_Sobrenome.getValue(),
            'email': self.__form_Email.getValue(),
            'telefone':self.__form_Telefone.getValue(),
        }

    