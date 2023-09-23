import bd.funcao.login as lg

class VerificaLoginESenha:
    
    def __init__(self) -> None:
        pass

    def loginSenhaHeCorreto(self,usuario,senha):
        if (lg.login(usuario,senha) == []):
            return False
        else:
            return True
