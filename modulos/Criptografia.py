import cryptocode
from VerificadorEmail import VerificadorEmail
from VerificadorTelefone import VerificadorTelefone 

def main():
    chave = "Barcelona"

    # Email validado pela classe VerificadorEmail
    email = "exemplo@email.com"  # Substitui pelo email validado

    # Número de telefone validado pela classe VerificadorTelefone
    telefone = "1234567890"  # Substitui pelo telefone validado

    email_criptografado = cryptocode.encrypt(email, chave)
    telefone_criptografado = cryptocode.encrypt(telefone, chave)

    print("Email criptografado:", email_criptografado)
    print("Telefone criptografado:", telefone_criptografado)
    print("Para descriptografar, insira a chave 'Barcelona'.")

if __name__ == "__main__":
    main()
