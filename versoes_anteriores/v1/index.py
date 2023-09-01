import funcao.conexao as con # conexao
import funcao.cliente as cl # cliente
import funcao.consulta as ag # agenda
import funcao.anotacao_consulta as at # assunto
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
resultado_cliente = cl.select("SELECT * FROM cliente")

print("\nTabela Cliente:")
print("-"*85)
print(resultado_cliente)

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
       FROM agenda AS ag \
       INNER JOIN cliente AS  cl \
       ON ag.fk_IdCliente = cl.IdCliente;"

# Exibir a tabela de agendas
resultado_agenda = ag.select(sql)

print("Tabela Agenda:")
print("-"*85)
print(resultado_agenda)

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

print("\nTabela Assunto:")
print("-"*85)
print(resultado_assunto)

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

print("Tabela Pagamento:")
print("-"*85)
print(pagamento_resultado)

# Fechar a conexão MySQL
con.fechar()