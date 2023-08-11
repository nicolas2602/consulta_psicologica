import funcao.conexao as con

def insert(nome, email, telefone):
    con.cursor.execute(f"INSERT INTO cliente(nomeCliente, emailCliente, telefoneCliente) VALUES ('{nome}', '{email}', '{telefone}')")
    con.conexao.commit()

def update(id, nome, email, telefone):
    con.cursor.execute(f"UPDATE cliente SET nomeCliente='{nome}', emailCliente='{email}', telefoneCliente='{telefone}' WHERE IdCliente={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM cliente WHERE IdCliente={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    return resultado
