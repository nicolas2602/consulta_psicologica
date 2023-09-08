import funcao.conexao as con

def insert(valor, dataHora, IdAgendCon, IdStatus, IdFormaPag):
    con.cursor.execute(f"INSERT INTO pagamento(valorPagamento, dataPagamento, fk_IdAgendCon, fk_IdStatusPag, fk_IdFormaPag) VALUES \
                                            ({valor}, '{dataHora}', {IdAgendCon}, {IdStatus}, {IdFormaPag})")
    con.conexao.commit()

def update(id, valor, dataHora, IdAgendCon, IdStatus, IdFormaPag):
    sql = f"UPDATE pagamento SET valorPagamento={valor}, dataHoraPag='{dataHora}', fk_IdAgendCon={IdAgendCon}, \
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


