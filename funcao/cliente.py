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

def mostrar(resultado):
    for i in range(0, len(resultado)):
        tabela = {
            'id': f'{resultado[i][0]}',
            'nome': f'{resultado[i][1]}',
            'email': f'{resultado[i][2]}',
            'telefone': f'{resultado[i][3]}'
        }
        
        return f"{tabela['id']} | {tabela['nome']} | {tabela['email']} | {tabela['telefone']}"