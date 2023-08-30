import funcao.conexao as con
import funcao.cliente as cl

sql = "SELECT * FROM cliente"
resultado = cl.select(sql)
print(resultado)
