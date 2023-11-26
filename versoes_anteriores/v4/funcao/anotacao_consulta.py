import funcao.conexao as con

def insert(descricao, IdConsulta):
    con.cursor.execute(f"INSERT INTO anotacao_consulta(descAnotCon, fk_IdConsulta) VALUES ('{descricao}', {IdConsulta})")
    con.conexao.commit()

def update(id, descricao, IdConsulta):
    con.cursor.execute(f"UPDATE anotacao_consulta SET descAnotCon='{descricao}', fk_IdConsulta={IdConsulta} WHERE IdAnotCon={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM anotacao_consulta WHERE IdAnotCon={id}")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    
    return resultado