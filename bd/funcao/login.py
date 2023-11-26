import bd.funcao.conexao as con

def login(usuario):
    sqlLogin = f"SELECT * FROM usuario WHERE nomeUsuario='{usuario}';"
    con.cursor.execute(sqlLogin)
    resultado = con.cursor.fetchall()

    return resultado