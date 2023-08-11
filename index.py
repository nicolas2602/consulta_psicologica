import funcao.conexao as con # conexao
import funcao.cliente as cl # cliente
import funcao.agenda as ag # agenda
import funcao.assunto as at # assunto
import funcao.pagamento as pg # pagamento

############### Tabela cliente #################
idCliente = 12
nome = "Eduardo"
email = "eduardo_silva@gmail.com"
telefone = "11996274701"

# cl.insert(nome, email, telefone)

# cl.update(id_cliente, nome, email, telefone)

# cl.delete(idCliente)

resultado = cl.select("select * from cliente")

print("Tabela Cliente:")
for i in resultado:
    print(i)

############### Tabela agenda #################

idAgenda = 3
data = "2023-08-23" 
horario = "15:00:00"
idCliente = 1

# ag.insert(data, horario, idCliente)

# ag.update(idAgenda, data, horario, idCliente)

# ag.delete(idAgenda)

sql = "select IdAgenda, DATE_FORMAT(dataAgenda, '%d/%m/%Y') as dataAgenda, \
       TIME_FORMAT(horarioAgenda, '%H:%m') as horarioAgenda, fk_IdCliente \
       from agenda"

resultado = ag.select(sql)

print("\nTabela Agenda:")
for i in resultado:
    print(i)

############### Tabela assunto #################

idAssunto = 3
assunto = "Assunto 1"
idAgenda = 1

# at.insert(assunto, idAgenda)

at.update(idAssunto, assunto, idAgenda)

# at.delete(idAssunto)

sql = "SELECT * FROM assunto"

resultado = at.select(sql)

print("\nTabela Assunto:")
for i in resultado:
    print(i)

############### Tabela pagamento #################

idPag = 4
valor = 50
idAgenda = 1
idStatus = 1

# pg.insert(valor, idAgenda, idstatus)

pg.update(idPag, valor, idAgenda, idStatus)

# pg.delete(idPag)

sql = "SELECT * FROM pagamento"

resultado = pg.select(sql)

print("\nTabela Pagamento:")
for i in resultado:
    print(i)

# Fechar a conexão MySQL
con.cursor.close()
con.conexao.close()