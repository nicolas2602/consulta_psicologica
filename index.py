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

### Inserir - Atualizar - Deletar ###
# cl.insert(nome, email, telefone)
# cl.update(idCliente, nome, email, telefone)
# cl.delete(idCliente)

# Exibir a tabela de cliente
resultado_cliente = cl.select("select * from cliente")
mostrar_cliente = cl.mostrar(resultado_cliente)

print("Tabela Cliente:")
print(mostrar_cliente)

############### Tabela agenda #################

idAgenda = 3
data = "2023-08-23" 
horario = "15:00:00"
idCliente = 1

### Inserir - Atualizar - Deletar ###
# ag.insert(data, horario, idCliente)
# ag.update(idAgenda, data, horario, idCliente)
# ag.delete(idAgenda)

sql = "SELECT IdAgenda, DATE_FORMAT(dataAgenda, '%d/%m/%Y') AS dataAgenda, \
       TIME_FORMAT(horarioAgenda, '%H:%m') AS horarioAgenda, \
       nomeCliente \
       FROM agenda as ag \
       INNER JOIN cliente as cl \
       ON ag.fk_IdCliente = cl.IdCliente;"

# Exibir a tabela de agendas
resultado_agenda = ag.select(sql)
mostrar_agenda = ag.mostrar(resultado_agenda)

print("\nTabela Agenda:")
print(mostrar_agenda)

############### Tabela assunto #################

idAssunto = 3
assunto = "Assunto 1"
idAgenda = 1

### Inserir - Atualizar - Deletar ###
# at.insert(assunto, idAgenda)
# at.update(idAssunto, assunto, idAgenda)
# at.delete(idAssunto)

sql = "SELECT IdAssunto, descAssunto, DATE_FORMAT(dataAgenda, '%d/%m/%Y') AS dataAgenda, \
              TIME_FORMAT(horarioAgenda, '%H:%m') AS horarioAgenda \
       FROM assunto AS an \
       INNER JOIN agenda AS ag \
       ON an.fk_IdAgenda = ag.IdAgenda;"

# Exibir a tabela de assuntos
resultado_assunto = at.select(sql)
mostrar_assunto = at.mostrar(resultado_assunto)

print("\nTabela Assunto:")
print(mostrar_assunto)

############### Tabela pagamento ############### 

# Inputs manuais
idPag = 4
valor = 50
idAgenda = 1
idStatus = 1

### Inserir - Atualizar - Deletar ###
# pg.insert(valor, idAgenda, idStatus)
# pg.update(idPag, valor, idAgenda, idStatus)
# pg.delete(idPag)

sql = "SELECT IdPagamento, valorPagamento, \
       DATE_FORMAT(dataAgenda, '%d/%m/%Y') AS dataAgenda, \
       TIME_FORMAT(horarioAgenda, '%H:%m') AS horarioAgenda, descStatus \
       FROM pagamento AS pg \
       INNER JOIN agenda AS ag ON pg.fk_IdAgenda = ag.IdAgenda \
       INNER JOIN status AS st ON pg.fk_IdStatus = st.IdStatus;"

# Exibir a tabela de pagamentos
pagamento_resultado = pg.select(sql)
mostrar_pagamento = pg.mostrar(pagamento_resultado)

print("\nTabela Pagamento:")
print(mostrar_pagamento)

# Fechar a conexão MySQL
con.fechar()