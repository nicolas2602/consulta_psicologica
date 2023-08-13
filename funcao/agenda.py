import funcao.conexao as con

def insert(data, horario, IdCliente):
    con.cursor.execute(f"INSERT INTO agenda(dataAgenda, horarioAgenda, fk_IdCliente) VALUES ('{data}', '{horario}', {IdCliente})")
    con.conexao.commit()

def update(id, data, horario, IdCliente):
    con.cursor.execute(f"UPDATE agenda SET dataAgenda='{data}', horarioAgenda='{horario}', fk_IdCliente={IdCliente} WHERE IdAgenda={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM agenda WHERE IdAgenda={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    return resultado

def mostrar(resultado):
    for i in range(0, len(resultado)):
        tabela = {
            'id': f'{resultado[i][0]}',
            'dataAgenda': f'{resultado[i][1]}',
            'horarioAgenda': f'{resultado[i][2]}',
            'cliente': f'{resultado[i][3]}'
        }
        
        return f"{tabela['id']} | {tabela['dataAgenda']} | {tabela['horarioAgenda']} | {tabela['cliente']}"