import bd.funcao.cliente as cl
class VerificadorClienteExiste:

    def __init__(self):
        pass

    def clienteExiste(self,nome,sobrenome):
        x = cl.selectClienteNomeSobreNome(nome,sobrenome)
        
        if x == []:
            return False
        else:
            return True