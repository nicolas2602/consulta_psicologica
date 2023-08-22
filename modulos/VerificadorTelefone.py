class VerificadorTelefone:
    def __init__(self, telefone):
        self.telefone = telefone

    def verificar(self):
        telefone_numerico = self.telefone.replace(" ", "").replace("-", "")

        if not telefone_numerico.isdigit():
            return "Formato de telefone incorreto, por favor digite novamente."

        if len(telefone_numerico) < 10:
            return "Erro! O telefone deve ter pelo menos 10 dígitos."

        return None

while True:
    telefone = input("Digite o telefone: ")
    verificador_telefone = VerificadorTelefone(telefone)
    erro_telefone = verificador_telefone.verificar()

    if erro_telefone:
        print(erro_telefone)
    else:
        print("Telefone válido!")
        break
