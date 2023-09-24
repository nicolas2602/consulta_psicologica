import flet as ft
from Itens.Campo.CampoFormulario import CampoFormulario
from Itens.Campo.CampoFormularioAnotacao import CampoFormularioAnotacao
import bd.funcao.pagamento as pg

class FormularioAnotacao(ft.UserControl):

    '''Cria um conjunto de capos de digitação para o Agendamento.'''

    def __init__(self,page,idBD = None, Titulo = None, Anotacoes=None):
        self.page = page
        
        self.__id = idBD

        self.__titulo = CampoFormulario("Titulo",Titulo)
        self.__anotacoes = CampoFormularioAnotacao("Anotações",Anotacoes,None,self.contCaracteres)
        self.__anotacoes.setMultiline(True,10)
        

        self.qtdInicial = 0
        self.qtdFinal = 200
        self.__qtdCaracteres = ft.Text(value=f"{self.qtdInicial}/{self.qtdFinal}",size=15,color=ft.colors.GREEN_900)

        self.contCaracteres(self)

        self.__desginer = ft.Column(controls=[
            self.__titulo.build(),
            self.__anotacoes.build(),
            self.__qtdCaracteres
        ])

    def build(self):
        return self.__desginer

    def setValue(self, idBD = None, Titulo = None, Anotacoes=None):
        '''Seta os valores do Campo (auto preenchimento).'''
        self.__id = idBD
        self.__titulo.setValue(Titulo)
        self.__anotacoes.setValue(Anotacoes)
        self.contCaracteres(self)

    def getValue(self):
        
        qtdTextoValido = True
        if len(self.__anotacoes.getValue()) > self.qtdFinal:
            qtdTextoValido = False

        return {
            'id':self.__id,
            'titulo':self.__titulo.getValue(),
            'anotacoes':self.__anotacoes.getValue(),
            'qtdTxt':qtdTextoValido
        }
    
    def contCaracteres(self,e):
        txt = self.__anotacoes.getValue()
        self.qtdInicial= len(txt)
        self.__qtdCaracteres.value=f"{self.qtdInicial}/{self.qtdFinal}"

        if (self.qtdInicial > self.qtdFinal):
            self.__qtdCaracteres.color = ft.colors.RED
        else:
            self.__qtdCaracteres.color=ft.colors.GREEN_900

        self.page.update()