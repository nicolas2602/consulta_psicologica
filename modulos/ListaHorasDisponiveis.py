import bd.funcao.agendamento as ag
from modulos.ListaHorarios import ListaHorarios
from modulos.Check.VerificadorData import VerificadorData
from datetime import timedelta

class ListaHorasDisponiveis:
    '''Classe de returna os horarios disponiveis que não estão sendo usados...'''
    def __init__(self,hora = None):

        self.lista = ListaHorarios().criarListaHorarios()
        self.addHora = hora
        

    def listaHorasDisponiveis(self, data):
        return self.__montarLista(data,self.addHora)

    def __montarLista(self,data,hora):
        xdata = VerificadorData(data).verificar()

        if (xdata[0]):

            bd = ag.selectHora(data)
            lista = self.lista

            for horas in bd:
                x = horas[0]
                x = str(x)
                if len(x) < 8:
                    x = f"0{x}"
                    print(x)
                x = x[:-3]

                if x in lista and x != hora:
                    lista.remove(x)
        
            return lista
        else:
            return []
        
    def addHoras(self,hora = None):
        self.addHora = hora

# x = ListaHorasDisponiveis()

# print(x.listaHorasDisponiveis('2023-09-27'))