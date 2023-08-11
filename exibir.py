import conexao as con

sql = ""
con.cursor.execute(sql)
resultado = con.cursor.fetchall()
