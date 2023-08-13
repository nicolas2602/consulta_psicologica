import funcao.conexao as con

def insert(valor, IdAgenda, IdStatus):
    con.cursor.execute(f"INSERT INTO pagamento(valorPagamento, fk_IdAgenda, fk_IdStatus) VALUES ({valor}, {IdAgenda}, {IdStatus})")
    con.conexao.commit()

def update(id, valor, IdAgenda, IdStatus):
    con.cursor.execute(f"UPDATE pagamento SET valorPagamento={valor}, fk_IdAgenda={IdAgenda}, fk_IdStatus={IdStatus} WHERE IdPagamento={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM pagamento WHERE IdPagamento={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    return resultado

def mostrar(resultado):
    for i in range(0, len(resultado)):
        tabela = {
            'idPag': f'{resultado[i][0]}',
            'valor': f'{resultado[i][1]}',
            'dataAgenda': f'{resultado[i][2]}',
            'horarioAgenda': f'{resultado[i][3]}',
            'status': f'{resultado[i][4]}'
        }
        
        return f"{tabela['idPag']} | {tabela['valor']} | {tabela['dataAgenda']} | "\
               f"{tabela['horarioAgenda']} | {tabela['status']}"



