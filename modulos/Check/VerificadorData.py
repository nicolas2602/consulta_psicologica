from datetime import date

class VerificadorData:
    def __init__(self,data):
        self.data = data # 27/06/2023
        self.axiliar =''

    def verificar(self):
        self.axiliar = self.data.replace(' ','')

        try:    
            # pego separado os valores EX: 2023,06,27
            self.axiliar = date(int(self.axiliar[6:]),int(self.axiliar[3:5]),int(self.axiliar[0:2]))
        except ValueError:
            return [False,"Data Invalida!"]
       
        self.axiliar = self.axiliar.strftime("%d/%m/%Y")

        return [True,self.axiliar]