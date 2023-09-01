import funcao.conexao as con # conexao
import funcao.cliente as cl # cliente
import funcao.consulta as cs # agenda
import funcao.anotacao_consulta as at # assunto
import funcao.pagamento as pg # pagamento
import datetime

nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
email = input("Digite o seu e-mail: ")
telefone = input("Digite o seu telefone: ")

cl.insert(nome, sobrenome, email, telefone)

sql = "SELECT * FROM cliente;"
r = cl.select(sql)
print(r)

# Fechar a conexão MySQL
con.fechar()