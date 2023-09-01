import funcao.conexao as con # conexao
import funcao.cliente as cl # cliente
import funcao.consulta as cs # agenda
import funcao.anotacao_consulta as at # assunto
import funcao.pagamento as pg # pagamento
import datetime


sql = "SELECT IdAnotCon, descAnotCon, DATE_FORMAT(dataConsulta, '%d/%m/%Y'), TIME_FORMAT(horarioConsulta, '%H:%m') as horarioConsulta \
FROM anotacao_consulta AS an \
INNER JOIN consulta AS cs \
ON an.fk_IdConsulta = cs.IdConsulta"


r = at.select(sql)
print(r)

# Fechar a conexão MySQL
con.fechar()