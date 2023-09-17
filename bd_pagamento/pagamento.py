import bd.funcao.conexao as con

def insert(valor, dataHora, IdAgendCon, IdStatus, IdFormaPag):
    con.cursor.execute(f"INSERT INTO pagamento(valorPagamento, dataPagamento, fk_IdAgendCon, fk_IdStatusPag, fk_IdFormaPag) VALUES \
                                            ({valor}, '{dataHora}', {IdAgendCon}, {IdStatus}, {IdFormaPag})")
    con.conexao.commit()

def insertAgendPg(valor,IdAgendCon, IdStatus):
    con.cursor.execute(f"INSERT INTO pagamento(idPagamento,valorPagamento, fk_IdAgendCon, fk_IdStatusPag) VALUES \
                                            ({IdAgendCon},{valor}, {IdAgendCon}, {IdStatus})")
    con.conexao.commit()

def update(id, valor, dataHora, IdStatus, IdFormaPag):
    sql = f"UPDATE pagamento SET valorPagamento={valor}, dataPagamento='{dataHora}', \
           fk_IdStatusPag={IdStatus}, fk_IdFormaPag={IdFormaPag} WHERE IdPagamento={id}"
    con.cursor.execute(sql)
    con.conexao.commit()

def updateStatus(id,IdStatus):
    sql = f"UPDATE pagamento SET fk_IdStatusPag={IdStatus} WHERE IdPagamento={id}"
    con.cursor.execute(sql)
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM pagamento WHERE IdPagamento={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()

    return resultado

def listaStatusPg():
    resultado = select(f"SELECT * FROM status_pagamento")
    return resultado

def listaFormaPg():
    resultado = select(f"SELECT * FROM forma_pagamento")
    return resultado

def pesquisarComTodasInfo(nome,statusPag,dataInicio,datafim):
    ''' Returna idPagamento, idAgendamento,
        Data e Hora do Agendamento,
        nome e sobrenome do paciente,
        volor pago, idFormaPag, descFormaPag,
        idStatusPag e descStatus
        [(1, 1, datetime.date(2023, 8, 21), datetime.timedelta(seconds=50400), 'Nicolas', 'Yonekawa', Decimal('45.00'), datetime.date(2023, 11, 22), 1, 'Pix', 1, 'Concluído')]
    '''

    sql = f"SELECT IdPagamento, \
        fk_IdAgendCon, \
        dataAgendCon AS dataAgendCon, \
        horarioAgendCon AS horarioAgendCon, \
        nomeCliente, sobrenomeCliente, \
        valorPagamento AS valorPagmento, \
        dataPagamento AS dataPagamento, \
        fk_IdFormaPag, \
        descFormaPag AS descFormaPag, \
        fk_IdStatusPag, \
        descStatusPag \
        FROM pagamento AS pg \
        LEFT JOIN agendamento_consulta AS cs ON pg.fk_IdAgendCon = cs.IdAgendCon \
        LEFT JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente \
        LEFT JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag \
        LEFT JOIN status_pagamento AS st ON pg.fk_IdStatusPag = st.IdStatusPag \
        WHERE nomeCliente like '%{nome}%' AND \
        descStatusPag like '%{statusPag}%' OR \
        dataPagamento BETWEEN '{dataInicio}' AND '{datafim}' \
        ORDER BY dataAgendCon;"

    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()

    return resultado

def pesquisarSemData(nome,statusPag,):
    ''' Returna idPagamento, idAgendamento,
        Data e Hora do Agendamento,
        nome e sobrenome do paciente,
        volor pago, idFormaPag, descFormaPag,
        idStatusPag e descStatus
        [(1, 1, datetime.date(2023, 8, 21), datetime.timedelta(seconds=50400), 'Nicolas', 'Yonekawa', Decimal('45.00'), datetime.date(2023, 11, 22), 1, 'Pix', 1, 'Concluído')]
    '''

    sql = f"SELECT IdPagamento, \
        fk_IdAgendCon, \
        dataAgendCon AS dataAgendCon, \
        horarioAgendCon AS horarioAgendCon, \
        nomeCliente, sobrenomeCliente, \
        valorPagamento AS valorPagmento, \
        dataPagamento AS dataPagamento, \
        fk_IdFormaPag, \
        descFormaPag AS descFormaPag, \
        fk_IdStatusPag, \
        descStatusPag \
        FROM pagamento AS pg \
        LEFT JOIN agendamento_consulta AS cs ON pg.fk_IdAgendCon = cs.IdAgendCon \
        LEFT JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente \
        LEFT JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag \
        LEFT JOIN status_pagamento AS st ON pg.fk_IdStatusPag = st.IdStatusPag \
        WHERE nomeCliente like '%{nome}%' AND \
        descStatusPag like '%{statusPag}%' \
        ORDER BY dataAgendCon;"

    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()

    return resultado

def pesquisarStatusPagamento(statusPag,data):
    ''' Returna idPagamento, idAgendamento,
        Data e Hora do Agendamento,
        nome e sobrenome do paciente,
        volor pago, idFormaPag, descFormaPag,
        idStatusPag e descStatus
        [(1, 1, datetime.date(2023, 8, 21), datetime.timedelta(seconds=50400), 'Nicolas', 'Yonekawa', Decimal('45.00'), datetime.date(2023, 11, 22), 1, 'Pix', 1, 'Concluído')]
    '''

    sql = f"SELECT IdPagamento, \
        fk_IdAgendCon, \
        dataAgendCon AS dataAgendCon, \
        horarioAgendCon AS horarioAgendCon, \
        nomeCliente, sobrenomeCliente, \
        valorPagamento AS valorPagmento, \
        dataPagamento AS dataPagamento, \
        fk_IdFormaPag, \
        descFormaPag AS descFormaPag, \
        fk_IdStatusPag, \
        descStatusPag \
        FROM pagamento AS pg \
        LEFT JOIN agendamento_consulta AS cs ON pg.fk_IdAgendCon = cs.IdAgendCon \
        LEFT JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente \
        LEFT JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag \
        LEFT JOIN status_pagamento AS st ON pg.fk_IdStatusPag = st.IdStatusPag \
        WHERE descStatusPag like '%{statusPag}%' AND\
        dataAgendCon <= '{data}' \
        ORDER BY dataAgendCon;"

    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()

    return resultado
