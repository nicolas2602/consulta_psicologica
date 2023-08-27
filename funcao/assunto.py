import funcao.conexao as con

def insert(descricao, IdConsulta):
    con.cursor.execute(f"INSERT INTO assunto(descAssunto, fk_IdConsulta) VALUES ('{descricao}', {IdConsulta})")
    con.conexao.commit()

def update(id, descricao, IdConsulta):
    con.cursor.execute(f"UPDATE assunto SET descAssunto='{descricao}', fk_IdConsulta={IdConsulta} WHERE IdAssunto={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM assunto WHERE IdAssunto={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    
    return resultado