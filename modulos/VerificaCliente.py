from modulos.Check.VerificadorNome import VerificadorNome
from modulos.Check.VerificadorSobrenome import VerificadorSobrenome
from modulos.Check.VerificadorEmail import VerificadorEmail
from modulos.Check.VerificadorTelefone import VerificadorTelefone


class VerificaCliente:
    
    def __init__(self,lista):
        self.dados = lista

    def verificar(self):
        msg = ""

        # Primeira Opção - (1,nome,sobrenome,email,telefone) - Dados para Update
        if(len(self.dados) == 5):

            teste1 = VerificadorNome(self.dados[1])
            teste2 = VerificadorSobrenome(self.dados[2])
            teste3 = VerificadorEmail(self.dados[3])
            teste4 = VerificadorTelefone(self.dados[4])

            t1 = teste1.verificar()
            t2 = teste2.verificar()
            t3 = teste3.verificar()
            t4 = teste4.verificar()

            if(t1 and t2 and t3 and t4):
                return [True]
            
            else:
                if(t1):
                    msg = teste1.mensagem()
                elif(t2):
                    msg = teste2.mensagem()
                elif(t3):
                    msg = teste3.mensagem()
                else:
                    msg = teste4.mensagem()


                return [False, msg]
            
        # Segunda Opção - [nome,sobrenome,email,telefone] - Dados para Novo Cadastro
        else:

            teste1 = VerificadorNome(self.dados[0])
            teste2 = VerificadorSobrenome(self.dados[1])
            teste3 = VerificadorEmail(self.dados[2])
            teste4 = VerificadorTelefone(self.dados[3])

            t1 = teste1.verificar()
            t2 = teste2.verificar()
            t3 = teste3.verificar()
            t4 = teste4.verificar()

            if(t1 and t2 and t3 and t4):
                return [True]
            
            else:
                if(not t1):
                    msg = teste1.mensagem()
                elif(not t2):
                    msg = teste2.mensagem()
                elif(not t3):
                    msg = teste3.mensagem()
                else:
                    msg = teste4.mensagem()


                return [False, msg]


#### TESTE #####

# x = VerificaCliente(['nome','sobrenome','nome@gmail.com','19992399131'])

# print(x.verificar())

# x = VerificaCliente(['1','nome','sobrenome','nome@gmail.com','19992399131'])

# print(x.verificar())