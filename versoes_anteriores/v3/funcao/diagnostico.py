import funcao.conexao as con

def insert(descricao, IdConsulta):
    con.cursor.execute(f"INSERT INTO diagnostico(descDiagnostico, fk_IdConsulta) VALUES VALUES ('{descricao}', {IdConsulta})")
    con.conexao.commit()

def update(id, descricao, IdConsulta):
    con.cursor.execute(f"UPDATE diagnostico SET descDiagnostico='{descricao}', fk_IdConsulta={IdConsulta} WHERE IdDiagnostico={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM diagnostico WHERE IdDiagnostico={id}")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    
    return resultado