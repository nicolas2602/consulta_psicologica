import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin"
)

cursor = conexao.cursor()