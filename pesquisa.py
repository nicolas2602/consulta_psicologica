import funcao.conexao as con # conexao
import funcao.cliente as cl # cliente
import funcao.agenda as ag # agenda
import funcao.assunto as at # assunto
import funcao.pagamento as pg # pagamento

nome = input("Digite o campo para pesquisa: ")
email = input("Digite o email: ")
telefone = input("Digite o número de telefone")

sql =f"SELECT * FROM cliente  \
WHERE nomeCliente like '%{nome}%'\
OR emailCliente like '%{email}%'\
OR telefoneCliente like '%{telefone}%';"

r = cl.select(sql)
print(r)

