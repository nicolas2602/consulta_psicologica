import bd.funcao.grafico as bdDados

class DadosGraficos:
    
    def anos(self):
        return bdDados.selectAno()
    
    def totalAnoConcluido(self,ano):
        meses = self.totalMesesConcluido(ano)
        resultado = 0
        for valor in meses:
            resultado += valor[2]

        return resultado
    
    def totalAnoAndamento(self,ano):
        meses = self.totalMesesAndamento(ano)
        resultado = 0
        for valor in meses:
            resultado += valor[2]

        return resultado
    
    def totalAnoPendente(self,ano):
        meses = self.totalMesesPendente(ano)
        resultado = 0
        for valor in meses:
            resultado += valor[2]

        return resultado

    def totalMesesConcluido(self,ano):
        return bdDados.StatusAnoConcluido(ano)
    
    def totalMesesAndamento(self,ano):
        return bdDados.StatusAnoAndamento(ano)
    
    def totalMesesPendente(self,ano):
        return bdDados.StatusAnoPendente(ano)
    
