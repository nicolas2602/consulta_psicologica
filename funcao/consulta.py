import funcao.conexao as con

def insert(data, horario, assunto, IdCliente):
    con.cursor.execute(f"INSERT INTO consulta (dataConsulta, horarioConsulta, assuntoConsulta, fk_IdCliente) VALUES ('{data}', '{horario}', '{assunto}', {IdCliente})")
    con.conexao.commit()

def update(id, data, horario, assunto, IdCliente):
    con.cursor.execute(f"UPDATE consulta SET dataConsulta='{data}', horarioConsulta='{horario}', assuntoConsulta='{assunto}', fk_IdCliente={IdCliente} WHERE IdAgenda={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM consulta WHERE IdConsulta={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    
    return resultado