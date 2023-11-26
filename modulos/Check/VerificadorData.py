from datetime import date

class VerificadorData:
    def __init__(self,data):
        self.data = data # 27/06/2023 or 2023-06-27
        self.axiliar =''
        self.checagem1 = True
        self.checagem2 = True

    def verificar(self):
        if self.data != None:
            self.axiliar = str(self.data).replace(' ','')

        if len(self.axiliar) == 10:

            try:    
                # pego separado os valores - Checagem Brasileira
                self.axiliar = date(int(self.axiliar[6:]),int(self.axiliar[3:5]),int(self.axiliar[0:2]))
            except (ValueError,TypeError):
                self.checagem1 = False

            try:    
                # pego separado os valores - Checagem USA
                self.axiliar = date(int(self.axiliar[0:4]),int(self.axiliar[5:7]),int(self.axiliar[8:10]))
            except (ValueError,TypeError):
                self.checagem2 = False
    

            if(self.checagem1 or self.checagem2):
                return [True,self.axiliar]
            else:
                return [False,"Data Invalida!"]
        
        else: 
            return [False,"Data Invalida!"]