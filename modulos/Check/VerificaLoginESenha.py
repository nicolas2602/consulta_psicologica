import bd.funcao.login as lg
from modulos.Criptografia import Criptografia

class VerificaLoginESenha:
    
    def __init__(self) -> None:
        self.cript = Criptografia()
        
    def loginSenhaHeCorreto(self,usuario,senha):
        log = lg.login(usuario)

        if (log == []):
            return False
        else:
            dados  = log[0]

            if dados[1] == usuario and self.cript.decodificar(dados[2]) == str(senha):
                return True
            else:
                return False