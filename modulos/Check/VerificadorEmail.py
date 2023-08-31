class VerificadorEmail:
    def __init__(self, email):
        self.email = email

    def verificar(self):

        if self.email.count("@") != 1:
            return False
        
        parts = self.email.split("@")
        if len(parts) != 2:
            return False

        elif not parts[0] or not parts[1]:
            return False

        domain_parts = parts[1].split(".")
        if len(domain_parts) < 2:
            return False

        elif not domain_parts[-1]:
            return False
        
        else:
            return True

    def mensagem(self):
        return "Email Invalido"


# while True:
#     email = input("Digite o email: ")
#     verificador_email = VerificadorEmail(email)
#     erro_email = verificador_email.verificar()

#     if erro_email:
#         print(erro_email)
#     else:
#         print("E-mail válido!")
#         break
