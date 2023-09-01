import funcao.conexao as con # conexao
import funcao.cliente as cl # cliente
import funcao.consulta as ag # agenda
import funcao.anotacao_consulta as at # assunto
import funcao.pagamento as pg # pagamento

nome = input("Digite o nome: ")
telefone = input("Digite o número de telefone: ")

sql = f"SELECT * FROM cliente \
WHERE nomeCliente like '%{nome}%' \
OR telefoneCliente like '%{telefone}%';"

print("-"*6)

r = cl.select(sql) # parte de pesquisa funciona
print(r)

