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
    
    coletar = ""

    for r in resultado:
        coletar += f"ID: {r[0]} | Valor: R$ {r[1]} | Data da consulta: {r[2]} | "\
                   f"Horário da consulta: {r[3]} | Status: {r[4]}"
    return coletar


