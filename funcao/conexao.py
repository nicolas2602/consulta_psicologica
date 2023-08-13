import mysql.connector

servidor = "localhost"
usuario = "root"
senha = "admin"
bd = "consulta_psicologica"

conexao = mysql.connector.connect(host=servidor, user=usuario, password=senha, database=bd)

cursor = conexao.cursor()

def fechar():
    cursor.close()
    conexao.close()