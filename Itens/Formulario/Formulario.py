import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario

class Formulario(ft.UserControl):

    def __init__(self, idBD = None, nome = None, email = None, telefone = None):

        self.__id = idBD

        self.__form_Nome = CampoFormulario("Nome",nome)
        self.__form_Email = CampoFormulario("E-mail",email)
        self.__form_Telefone = CampoFormulario("Telefone",telefone)


        self.__desiner = ft.Column(controls=[
            self.__form_Nome.build(),
            self.__form_Email.build(),
            self.__form_Telefone.build()
        ])

    def build(self):
        return self.__desiner


    # def __setValue(self,e):
    #     self.__form_Nome.setValue(self.__nome)
    #     self.__form_Email.setValue(self.__email)
    #     self.__form_Telefone.setValue(self.__telefone)

    def get_value(self,e):
        return {
            'id':self.__id,
            'nome': self.__nome,
            'email': self.__email,
            'telefone':self.__telefone,
        }
    