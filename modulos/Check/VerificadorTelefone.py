class VerificadorTelefone:
    def __init__(self, telefone):
        self.telefone = telefone

    def verificar(self):
        telefone_numerico = self.telefone.replace(" ", "").replace("-", "")

        if not telefone_numerico.isdigit():
            return False

        elif len(telefone_numerico) < 10:
            return False

        else:
            return True

    def mensagem(self):
        return "Telefone válido!"

# while True:
#     telefone = input("Digite o telefone: ")
#     verificador_telefone = VerificadorTelefone(telefone)
#     erro_telefone = verificador_telefone.verificar()

#     if erro_telefone:
#         print(erro_telefone)
#     else:
#         print("Telefone válido!")
#         break
