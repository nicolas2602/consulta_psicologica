import funcao.conexao as con # conexao
import funcao.cliente as cl # cliente
import funcao.agendamento as cs # agenda
import funcao.anotacao_consulta as at # assunto
import funcao.pagamento as pg # pagamento
import funcao.login as lg
import datetime

sql_teste = "SELECT IdAnotCon, descAnotCon, dataConsulta, horarioConsulta as horarioConsulta \
FROM anotacao_consulta AS an \
INNER JOIN consulta AS cs \
ON an.fk_IdConsulta = cs.IdConsulta"

sql = "SELECT IdAnotCon, descAnotCon, DATE_FORMAT(dataConsulta, '%d/%m/%Y'), TIME_FORMAT(horarioConsulta, '%H:%m') as horarioConsulta \
FROM anotacao_consulta AS an \
INNER JOIN consulta AS cs \
ON an.fk_IdConsulta = cs.IdConsulta"

teste = at.select(sql_teste )
r = at.select(sql)

print("Sem função do MySQL")
print(teste)
print()
print("Com algumas funções do MySQL")
print(r)

r = lg.logar('admin', 'admin12')
print(r)

# Fechar a conexão MySQL
con.fechar()