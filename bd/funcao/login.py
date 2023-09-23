import bd.funcao.conexao as con

def login(usuario, senha):
    sqlLogin = f"SELECT * FROM usuario WHERE nomeUsuario='{usuario}' AND senhaUsuario='{senha}';"
    con.cursor.execute(sqlLogin)
    resultado = con.cursor.fetchall()

    return resultado