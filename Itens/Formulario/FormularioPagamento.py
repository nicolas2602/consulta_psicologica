import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.Campo.CampoDropStatus import CampoDropStatus
import bd.funcao.pagamento as pg

class FormularioPagamento(ft.UserControl):

    '''Cria um conjunto de capos de digitação para o Agendamento.'''

    def __init__(self, idBD = None, desconto = None, acrescimo=None, data = None, formaPg = None , statusPg = None):

        self.__id = idBD

        self.__desconto = CampoFormulario("Desconto",desconto,)
        self.__acrescimo = CampoFormulario("Acrescimo",acrescimo,)
        self.__Data = CampoFormulario("Data",data,)

        self.__dadosFormaPg = pg.listaFormaPg()
        self.__formaPg = CampoDropStatus("Forma de Pagamento",self.__dadosFormaPg)
        self.__formaPg.setValue(formaPg)

        self.__dadosStatusPg = pg.listaStatusPg()
        self.__statusPg = CampoDropStatus("Status do Pagamento",self.__dadosStatusPg)
        self.__statusPg.setValue(statusPg)

        self.__desginer = ft.Column(controls=[
            self.__desconto.build(),
            self.__acrescimo.build(),
            self.__Data.build(),
            self.__formaPg.build(),
            self.__statusPg.build(),
        ])

    def build(self):
        return self.__desginer

    def setValue(self, idBD = None, desconto = None, acrescimo=None, data = None, formaPg = None , statusPg = None):
        '''Seta os valores do Campo (auto preenchimento).'''
        self.__id = idBD
        self.__desconto.setValue(desconto)
        self.__acrescimo.setValue(acrescimo)
        self.__Data.setValue(data)
        self.__formaPg.setValue(formaPg)
        self.__statusPg.setValue(statusPg)

    def getValue(self):
        return {
            'id':self.__id,
            'data':self.__Data.getValue(),
            'desconto':self.__desconto.getValue(),
            'acrescimo':self.__acrescimo.getValue(),
            'formaPagamento': self.__formaPg.getValue(),
            'statusPatamento':self.__statusPg.getValue()
        }