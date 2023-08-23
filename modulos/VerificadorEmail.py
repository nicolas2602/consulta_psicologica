class VerificadorEmail:
    def __init__(self, email):
        self.email = email

    def verificar(self):
        if self.email.count("@") != 1:
            return "O e-mail deve conter exatamente um '@'."

        parts = self.email.split("@")
        if len(parts) != 2:
            return "Formato de e-mail inválido."

        if not parts[0] or not parts[1]:
            return "O e-mail deve conter um usuário e um domínio."

        domain_parts = parts[1].split(".")
        if len(domain_parts) < 2:
            return "Domínio inválido após o '@'."

        if not domain_parts[-1]:
            return "O domínio deve ter pelo menos um caractere após o '@' e antes do '.'."

        return None

while True:
    email = input("Digite o email: ")
    verificador_email = VerificadorEmail(email)
    erro_email = verificador_email.verificar()

    if erro_email:
        print(erro_email)
    else:
        print("E-mail válido!")
        break
