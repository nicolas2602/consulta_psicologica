class VerificadorNome:
    def __init__(self, nome):
        self.nome = nome

    def verificar(self):
        if not self.nome.replace(" ", "").isalpha():
            return "Formato de nome incorreto, Por favor tente novamente."
        return None

while True:
    nome = input("Digite o nome: ")
    verificador_nome = VerificadorNome(nome)

    erro_nome = verificador_nome.verificar()

    if erro_nome:
        print(erro_nome)
    else:
        print("Nome válido!")
        break
