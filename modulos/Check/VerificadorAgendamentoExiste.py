import bd.funcao.agendamento as ag
class VerificadorAgendamentoExiste:

    def __init__(self):
        pass

    def AgendaExiste(self,data,hora):
        x = ag.selectDataHora(data,hora)
        
        if x == []:
            return [False,'sem id']
        else:
            return [True,x[0]]