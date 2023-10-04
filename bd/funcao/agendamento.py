import bd.funcao.conexao as con

def insert(data, horario, IdCliente):
    con.cursor.execute(f"INSERT INTO agendamento_consulta(dataAgendCon, horarioAgendCon, fk_IdCliente) VALUES (STR_TO_DATE('{data}','%d/%m/%Y'), '{horario}', '{IdCliente}')")
    con.conexao.commit()

def update(id, data, horario, IdCliente):
    con.cursor.execute(f"UPDATE agendamento_consulta SET dataAgendCon='{data}', horarioAgendCon='{horario}', fk_IdCliente={IdCliente} WHERE IdAgendCon={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM agendamento_consulta WHERE IdAgendCon={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    
    return resultado

def selectHora(data):
    con.cursor.execute(f"SELECT horarioAgendCon FROM agendamento_consulta WHERE dataAgendCon = '{data}'")
    resultado = con.cursor.fetchall()
    
    return resultado

def selectDataHora(data,hora):
    con.cursor.execute(f"SELECT IdAgendCon,dataAgendCon,horarioAgendCon FROM agendamento_consulta \
                       WHERE dataAgendCon = '{data}' AND horarioAgendCon = '{hora}'")
    resultado = con.cursor.fetchall()
    
    return resultado


def pesquisaNome(nome):
    '''IdAgendCon,dataAgendCon,horarioAgendCon,IdCliente,nomeCliente,sobrenomeCliente'''
    con.cursor.execute(f"SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon, TIME_FORMAT(horarioAgendCon, '%H:%i') AS horarioAgendCon,\
                        IdCliente, nomeCliente, sobrenomeCliente FROM agendamento_consulta as cs INNER JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente\
                        WHERE nomeCliente like '%{nome}%' ORDER BY dataAgendCon,horarioAgendCon;")
    resultado = con.cursor.fetchall()
    
    return resultado

def pesquisaData(data):
    '''Data deve ser padrão americano (AAAA-MM-DD) - IdAgendCon,dataAgendCon,horarioAgendCon,IdCliente,nomeCliente,sobrenomeCliente '''
    con.cursor.execute(f"SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon, TIME_FORMAT(horarioAgendCon, '%H:%i') AS horarioAgendCon,\
                        IdCliente, nomeCliente, sobrenomeCliente FROM agendamento_consulta as cs INNER JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente\
                        WHERE dataAgendCon = '{data}' ORDER BY dataAgendCon,horarioAgendCon;")
    resultado = con.cursor.fetchall()
    
    return resultado

def pesquisaNomeData(nome,data):
    '''Data deve ser padrão americano (AAAA-MM-DD) - IdAgendCon,dataAgendCon,horarioAgendCon,IdCliente,nomeCliente,sobrenomeCliente '''
    con.cursor.execute(f"SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon, TIME_FORMAT(horarioAgendCon, '%H:%i') AS horarioAgendCon,\
                        IdCliente, nomeCliente, sobrenomeCliente FROM agendamento_consulta as cs INNER JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente\
                        WHERE dataAgendCon = '{data}' AND nomeCliente like '%{nome}%' ORDER BY dataAgendCon,horarioAgendCon;")
    resultado = con.cursor.fetchall()
    
    return resultado

################################################################
def pesquisaIdNomeDataHora(idNome,data,hora):
    '''Data deve ser padrão americano (AAAA-MM-DD) - IdAgendCon,dataAgendCon,horarioAgendCon,IdCliente,nomeCliente,sobrenomeCliente '''
    con.cursor.execute(f"SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon, TIME_FORMAT(horarioAgendCon, '%H:%i') AS horarioAgendCon,\
                        IdCliente, nomeCliente, sobrenomeCliente FROM agendamento_consulta as cs INNER JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente\
                        WHERE dataAgendCon = '{data}'AND horarioAgendCon = '{hora}' AND IdCliente = {idNome} ORDER BY dataAgendCon,horarioAgendCon;")
    resultado = con.cursor.fetchall()
    
    return resultado

def pesquisaID(id):
    '''IdAgendCon,dataAgendCon,horarioAgendCon,IdCliente,nomeCliente,sobrenomeCliente'''
    con.cursor.execute(f"SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon, TIME_FORMAT(horarioAgendCon, '%H:%i') AS horarioAgendCon,\
                        IdCliente, nomeCliente, sobrenomeCliente FROM agendamento_consulta as cs INNER JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente\
                        WHERE IdAgendCon = '{id}';")
    resultado = con.cursor.fetchall()

    return resultado

def pesquisaTudo():
    '''Data deve ser padrão americano (AAAA-MM-DD) - IdAgendCon,dataAgendCon,horarioAgendCon,IdCliente,nomeCliente,sobrenomeCliente '''
    con.cursor.execute(f"SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon, TIME_FORMAT(horarioAgendCon, '%H:%i') AS horarioAgendCon,\
                        IdCliente, nomeCliente, sobrenomeCliente FROM agendamento_consulta as cs INNER JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente\
                        ORDER BY dataAgendCon,horarioAgendCon;")
    resultado = con.cursor.fetchall()
    
    return resultado

