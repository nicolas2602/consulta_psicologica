import funcao.conexao as con # conexao
import funcao.cliente as cl # cliente
import funcao.agenda as ag # agenda
import funcao.assunto as at # assunto
import funcao.pagamento as pg # pagamento

nome = input("Digite o campo para pesquisa: ")
email = input("Digite o email: ")
telefone = input("Digite o número de telefone")

sql =f"SELECT IdAssunto, DATE_FORMAT(dataAgenda, '%d/%m/%Y') AS dataAgenda, \
        TIME_FORMAT(horarioAgenda, '%H:%m') AS horarioAgenda, \
        nomeCliente, emailCliente, descAssunto, valorPagamento, descStatus \
FROM agenda AS ag \
INNER JOIN cliente AS cl \
ON ag.fk_IdCliente = cl.IdCliente \
INNER JOIN assunto AS an      \
ON ag.IdAgenda = an.fk_IdAgenda\
INNER JOIN pagamento AS pg
ON ag.IdAgenda = pg.fk_IdAgenda
INNER JOIN status AS st  
ON pg.fk_IdStatus = st.IdStatus
WHERE nomeCliente like '%Nicolas%'
    OR emailCliente like '%%'
    OR descAssunto like '%%'
    OR valorPagamento like '%%'
    OR descStatus like '%%'
    OR dataAgenda like '%%'
    OR horarioAgenda like '%%';"

r = cl.select(sql)
print(r)

