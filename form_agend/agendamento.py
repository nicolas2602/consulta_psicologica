import funcao.conexao as con

def insert(data, horario, IdCliente):
    con.cursor.execute(f"INSERT INTO agendamento_consulta SET dataAgendCon=STR_TO_DATE('{data}','%d/%m/%Y'), horarioAgendCon='{horario}', fk_IdCliente = {IdCliente}")
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