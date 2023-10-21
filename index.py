import funcao.conexao as con # conexao
import funcao.cliente as cl # cliente
import funcao.agendamento as cs # agenda
import funcao.anotacao_consulta as at # assunto
import funcao.pagamento as pg # pagamento
import funcao.login as lg
import datetime
import cryptocode

sql_teste = "SELECT IdAnotCon, descAnotCon, dataConsulta, horarioConsulta as horarioConsulta \
FROM anotacao_consulta AS an \
INNER JOIN consulta AS cs \
ON an.fk_IdConsulta = cs.IdConsulta"

sql = "SELECT IdAnotCon, descAnotCon, DATE_FORMAT(dataConsulta, '%d/%m/%Y'), TIME_FORMAT(horarioConsulta, '%H:%m') as horarioConsulta \
FROM anotacao_consulta AS an \
INNER JOIN consulta AS cs \
ON an.fk_IdConsulta = cs.IdConsulta"

teste = at.select(sql)
print(teste)

# Fechar a conexão MySQL
con.fechar()