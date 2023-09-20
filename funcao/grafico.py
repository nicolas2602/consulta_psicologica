import funcao.conexao as con

def setLanguange():
    con.cursor.execute("SET lc_time_names = 'pt_BR'")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    
    return resultado