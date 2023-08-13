import funcao.conexao as con

def insert(descricao, IdAgenda):
    con.cursor.execute(f"INSERT INTO assunto(descAssunto, fk_IdAgenda) VALUES ('{descricao}', {IdAgenda})")
    con.conexao.commit()

def update(id, descricao, IdAgenda):
    con.cursor.execute(f"UPDATE assunto SET descAssunto='{descricao}', fk_IdAgenda={IdAgenda} WHERE IdAssunto={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM assunto WHERE IdAssunto={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    return resultado

def mostrar(resultado):
    for i in range(0, len(resultado)):
        tabela = {
            'id': f'{resultado[i][0]}',
            'desc': f'{resultado[i][1]}',
            'dataAgenda': f'{resultado[i][2]}',
            'horarioAgenda': f'{resultado[i][3]}',
        }
        
        return f"{tabela['id']} | {tabela['desc']} | {tabela['dataAgenda']} | {tabela['horarioAgenda']}"