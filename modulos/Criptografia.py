import cryptocode

class Criptografia:
    
    def __init__(self):
        self.__key = "Brasil"

    def codificar(self, msg):
        return cryptocode.encrypt(msg,self.__key)
    
    def decodificar(self,codigo):
        return cryptocode.decrypt(codigo,self.__key)
    