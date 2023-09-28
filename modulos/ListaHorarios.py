from datetime import timedelta
from bd.funcao.usuario import selectHorarios

class ListaHorarios:
    def __init__(self):
        
        if selectHorarios()!=False:
            self.dados = selectHorarios()[0]
            self.horaInicio = self.dados[1]
            self.horaFim = self.dados[2]
            self.horaParadaInicio = self.dados[3]
            self.horaParadaFim = self.dados[4]
            self.horaPorConsultas = timedelta(minutes=int(self.dados[5]))


    def criarListaHorarios(self):
        horas = self.horaInicio
        lista=[]

        while(horas < self.horaFim):
            if horas < self.horaParadaInicio or horas >= self.horaParadaFim:
                if len(str(horas)) < 8:  
                    lista.append(f"0{str(horas)[:-3]}")
                    
                else:
                    lista.append(str(horas)[:-3])
                    
            horas = horas+self.horaPorConsultas

        return lista
    
# x = ListaHorarios()
# print(x.criarListaHorarios())