import mysql.connector

servidor = "localhost"
usuario = "root"
senha = "admin"
bd = "consulta_psicologica"

conexao = mysql.connector.connect(host=servidor, user=usuario, password=senha, database=bd)

cursor = conexao.cursor()

def insertCliente(nome, email, telefone):
    cursor.execute(f"INSERT INTO cliente(nomeCliente, emailCliente, telefoneCliente) VALUES ('{nome}', '{email}', '{telefone}')")
    conexao.commit()
    
