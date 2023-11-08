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