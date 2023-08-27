import funcao.conexao as con

def insert(valor, dataHora, IdConsulta, IdStatus, IdFormaPag):
    con.cursor.execute(f"INSERT INTO pagamento(valorPagamento, dataHoraPag, fk_IdConsulta, fk_IdStatusPag, fk_IdFormaPag) VALUES \
                                            ({valor}, '{dataHora}', {IdConsulta}, {IdStatus}, {IdFormaPag})")
    con.conexao.commit()

def update(id, valor, dataHora, IdConsulta, IdStatus, IdFormaPag):
    sql = f"UPDATE pagamento SET valorPagamento={valor}, dataHoraPag='{dataHora}', fk_IdAgenda={IdConsulta}, \
           fk_IdStatusPag={IdStatus}, fk_IdFormaPag={IdFormaPag} WHERE IdPagamento={id}"
    con.cursor.execute(sql)
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM pagamento WHERE IdPagamento={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()

    return resultado


