import funcao.conexao as con

def insert(data, horario, IdCliente):
    con.cursor.execute(f"INSERT INTO consulta (dataConsulta, horarioConsulta, fk_IdCliente) VALUES ('{data}', '{horario}', {IdCliente})")
    con.conexao.commit()

def update(id, data, horario, IdCliente):
    con.cursor.execute(f"UPDATE consulta SET dataConsulta='{data}', horarioConsulta='{horario}', fk_IdCliente={IdCliente} WHERE IdAgenda={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM consulta WHERE IdConsulta={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    
    return resultado