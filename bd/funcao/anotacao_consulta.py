import funcao.conexao as con

def insert(descricao, titulo, IdAgendCon):
    con.cursor.execute(f"INSERT INTO anotacao_consulta(descAnotCon, tituloAnotCon, fk_IdAgendCon) VALUES ('{descricao}', '{titulo}', {IdAgendCon})")
    con.conexao.commit()

def update(id, descricao, titulo, IdAgendCon):
    con.cursor.execute(f"UPDATE anotacao_consulta SET descAnotCon='{descricao}', tituloAnotCon='{titulo}', fk_IdAgendCon={IdAgendCon} WHERE IdAnotCon={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM anotacao_consulta WHERE IdAnotCon={id}")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    
    return resultado