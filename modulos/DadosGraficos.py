import bd.funcao.grafico as bdDados

class DadosGraficos:
    
    def anos(self):
        return bdDados.selectAno()
    
    def totalAnoConcluido(self,ano):
        meses = self._totalMesesConcluido(ano)
        resultado = 0
        for valor in meses:
            resultado += valor[2]

        return resultado
    
    def totalAnoAndamento(self,ano):
        meses = self._totalMesesAndamento(ano)
        resultado = 0
        for valor in meses:
            resultado += valor[2]

        return resultado
    
    def totalAnoPendente(self,ano):
        meses = self._totalMesesPendente(ano)
        resultado = 0
        for valor in meses:
            resultado += valor[2]

        return resultado

    def _totalMesesConcluido(self,ano):
        return bdDados.StatusAnoConcluido(ano)
    
    def _totalMesesAndamento(self,ano):
        return bdDados.StatusAnoAndamento(ano)
    
    def _totalMesesPendente(self,ano):
        return bdDados.StatusAnoPendente(ano)

    def _qntStatusPagamentoAno(self,ano):
        return bdDados.qntStatusPagamento(ano)

    def _statusMes(self,ano):
        melhor = bdDados.melhorMes(ano)
        pior = bdDados.piorMes(ano)
        if len(melhor) != 0:
            melhor = melhor[0][0]
        if len(pior) != 0:
             pior = pior[0][0]

        return [melhor, pior]
    
    def mediaAno(self,ano):
        qntMes = self.valorMesesConcluido(ano)
        total = self.totalAnoConcluido(ano)

        if len(qntMes) == 0 or total <= 0:
            return 0
        else:
            return (total / len(qntMes))

    def valorMesesConcluido(self,ano):
        '''Returna um dicionario [mes]:valor'''
        mesBruto = self._totalMesesConcluido(ano)

        mesTratado = {}

        for dados in mesBruto:
            mesTratado[f'{dados[0]}'] = dados[2]

        return mesTratado

    def porcentagemStatosPagamento(self,ano):
        x = self._qntStatusPagamentoAno(ano)
        total = 0
        resultado = {}

        # define o total
        for qnt in x:
           total+= qnt[0] 

        for item in x:
            
            if item[1] == "Concluído":
                resultado[f'{item[1]}'] = round(float(item[0] / total)*100 , 1)
            elif item[1] == "Pendente":
                resultado[f'{item[1]}'] = round(float(item[0] / total)*100 , 1)
            elif item[1] == "Em andamento":
                resultado[f'{item[1]}'] = round(float(item[0] / total)*100 , 1)
            else:
                pass

        if "Concluído" not in resultado:
            resultado['Concluído'] = float(0)
        if "Pendente" not in resultado:
            resultado['Pendente'] = float(0)
        if "Em andamento" not in resultado:
            resultado['Em andamento'] = float(0)

        return resultado
        # em dev

    def melhorMes(self,ano):
        mes = self._statusMes(ano)

        if mes[0] == []:
            return "----"
        else:
            return mes[0]
    def piorMes(self,ano):
        mes = self._statusMes(ano)

        if mes[1] == []:
            return "----"
        else:
            return mes[1]
