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

    coletar = ""

    for r in resultado:
       coletar += f"ID: {r[0]} | Data da consulta: {r[1]} | Horário da consulta: {r[2]} | "\
                  f"Nome do cliente: {r[3]}"
    return coletar