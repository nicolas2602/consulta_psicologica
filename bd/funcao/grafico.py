import bd.funcao.conexao as con

# '(Concluído'), ('Em andamento'), ('Pendente')
def setLanguange():
    con.cursor.execute("SET lc_time_names = 'pt_BR'")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    
    return resultado

def selectAno():
    setLanguange()
    con.cursor.execute("SELECT YEAR(dataAgendCon) AS ano \
        FROM pagamento as pg \
        INNER JOIN agendamento_consulta as ac \
        ON pg.fk_IdAgendCon = ac.IdAgendCon \
        GROUP BY YEAR(dataAgendCon) \
        ORDER BY YEAR(dataAgendCon) DESC;")
    
    resultado = con.cursor.fetchall()
    
    return resultado

def StatusAnoConcluido(ano):
    setLanguange()
    con.cursor.execute(f"SELECT MONTHNAME(dataPagamento) AS mes, YEAR(dataPagamento) AS ano, sum(valorPagamento + valorAcrescimo - valorDesconto) AS totalPagMes \
        FROM pagamento \
        WHERE fk_IdStatusPag = 1 AND dataPagamento LIKE '%{ano}%' \
        GROUP BY MONTHNAME(dataPagamento), \
        YEAR(dataPagamento);")
    
    resultado = con.cursor.fetchall()
    
    return resultado

def StatusAnoAndamento(ano):
    setLanguange()
    con.cursor.execute(f"SELECT MONTHNAME(dataAgendCon) AS mes, YEAR(dataAgendCon) AS ano, sum(valorPagamento + valorAcrescimo - valorDesconto) AS totalPagMes \
        FROM pagamento as pg \
        INNER JOIN agendamento_consulta as ac \
        ON pg.fk_IdAgendCon = ac.IdAgendCon \
        WHERE fk_IdStatusPag = 2 AND dataAgendCon LIKE '%{ano}%' \
        GROUP BY MONTHNAME(dataAgendCon), \
        YEAR(dataAgendCon);")
    
    resultado = con.cursor.fetchall()
    
    return resultado

def StatusAnoPendente(ano):
    setLanguange()
    con.cursor.execute(f"SELECT MONTHNAME(dataAgendCon) AS mes, YEAR(dataAgendCon) AS ano, sum(valorPagamento + valorAcrescimo - valorDesconto) AS totalPagMes \
        FROM pagamento as pg \
        INNER JOIN agendamento_consulta as ac \
        ON pg.fk_IdAgendCon = ac.IdAgendCon \
        WHERE fk_IdStatusPag = 3 AND dataAgendCon LIKE '%{ano}%' \
        GROUP BY MONTHNAME(dataAgendCon), \
        YEAR(dataAgendCon);")
    
    resultado = con.cursor.fetchall()
    
    return resultado


def qntStatusPagamento(ano):
    setLanguange()
    con.cursor.execute(f"SELECT COUNT(fk_IdStatusPag) AS qtdStatusPag, descStatusPag, \
        SUM(valorPagamento) AS totalPagamento \
        FROM pagamento AS pg \
        INNER JOIN agendamento_consulta as ac \
        ON pg.fk_IdAgendCon = ac.IdAgendCon \
        LEFT JOIN status_pagamento AS st  \
        ON pg.fk_IdStatusPag = st.IdStatusPag \
        WHERE dataAgendCon LIKE '%{ano}%' \
        GROUP BY fk_IdStatusPag;")
    
    resultado = con.cursor.fetchall()
    
    return resultado