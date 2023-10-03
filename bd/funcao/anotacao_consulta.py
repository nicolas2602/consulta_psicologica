import bd.funcao.conexao as con
from modulos.Criptografia import Criptografia

cript = Criptografia()

def insert(descricao, titulo, IdAgendCon):
    con.cursor.execute(f"INSERT INTO anotacao_consulta(descAnotCon, tituloAnotCon, fk_IdAgendCon) VALUES ('{descricao}', '{titulo}', {IdAgendCon})")
    con.conexao.commit()

def insertAnotacao(IdAgendCon):
    titulo = f'Titulo{IdAgendCon}'
    descricao = f'Anotação{IdAgendCon}'

    con.cursor.execute(f"INSERT INTO anotacao_consulta(IdAnotCon, descAnotCon, tituloAnotCon, fk_IdAgendCon) VALUES \
                                                            ({IdAgendCon},'{cript.codificar(descricao)}', '{cript.codificar(titulo)}',{IdAgendCon})")
    con.conexao.commit()

def update(id, descricao, titulo, IdAgendCon):
    con.cursor.execute(f"UPDATE anotacao_consulta SET descAnotCon='{cript.codificar(descricao)}', tituloAnotCon='{cript.codificar(titulo)}', fk_IdAgendCon={IdAgendCon} WHERE IdAnotCon={id}")
    con.conexao.commit()

def updateAnotacao(id, descricao, titulo):
    con.cursor.execute(f"UPDATE anotacao_consulta SET descAnotCon='{cript.codificar(descricao)}', tituloAnotCon='{cript.codificar(titulo)}' WHERE IdAnotCon={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM anotacao_consulta WHERE IdAnotCon={id}")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()
    
    return resultado


def selectAnotacoes():
    con.cursor.execute(f"SELECT IdAnotCon,dataAgendCon,horarioAgendCon,nomeCliente,sobrenomeCliente, tituloAnotCon, descAnotCon \
                        FROM anotacao_consulta AS an \
                        INNER JOIN agendamento_consulta AS cs \
                        ON an.fk_IdAgendCon = cs.IdAgendCon \
                        INNER JOIN cliente as cl \
                        ON cs.fk_IdCliente = cl.IdCliente;")
    resultado = con.cursor.fetchall()
    return resultado

def selectAnotacoesId(id):
    con.cursor.execute(f"SELECT IdAnotCon,dataAgendCon,horarioAgendCon,nomeCliente,sobrenomeCliente, tituloAnotCon, descAnotCon \
                        FROM anotacao_consulta AS an \
                        INNER JOIN agendamento_consulta AS cs \
                        ON an.fk_IdAgendCon = cs.IdAgendCon \
                        INNER JOIN cliente as cl \
                        ON cs.fk_IdCliente = cl.IdCliente WHERE IdAnotCon={id}")
    resultado = con.cursor.fetchall()
    return resultado

def pesquisaAnotacoesNomeData(Nome,data):
    con.cursor.execute(f"SELECT IdAnotCon,dataAgendCon,horarioAgendCon,nomeCliente,sobrenomeCliente, tituloAnotCon, descAnotCon \
                        FROM anotacao_consulta AS an \
                        INNER JOIN agendamento_consulta AS cs \
                        ON an.fk_IdAgendCon = cs.IdAgendCon \
                        INNER JOIN cliente as cl \
                        ON cs.fk_IdCliente = cl.IdCliente \
                        WHERE nomeCliente like '%{Nome}%' AND \
                        dataAgendCon = '{data}' \
                        ORDER BY YEAR(dataAgendCon) ASC, \
                        MONTH(dataAgendCon) ASC, \
                        DAY(dataAgendCon) ASC,\
                        HOUR(horarioAgendCon)ASC;")

    resultado = con.cursor.fetchall()
    
    return resultado

def pesquisaAnotacoesNome(Nome):
    con.cursor.execute(f"SELECT IdAnotCon,dataAgendCon,horarioAgendCon,nomeCliente,sobrenomeCliente, tituloAnotCon, descAnotCon \
                        FROM anotacao_consulta AS an \
                        INNER JOIN agendamento_consulta AS cs \
                        ON an.fk_IdAgendCon = cs.IdAgendCon \
                        INNER JOIN cliente as cl \
                        ON cs.fk_IdCliente = cl.IdCliente \
                        WHERE nomeCliente like '%{Nome}%' \
                        ORDER BY YEAR(dataAgendCon) ASC, \
                        MONTH(dataAgendCon) ASC,\
                        DAY(dataAgendCon) ASC,\
                        HOUR(horarioAgendCon)ASC;")

    resultado = con.cursor.fetchall()
    
    return resultado

def pesquisaAnotacoesData(data):
    con.cursor.execute(f"SELECT IdAnotCon,dataAgendCon,horarioAgendCon,nomeCliente,sobrenomeCliente, tituloAnotCon, descAnotCon \
                        FROM anotacao_consulta AS an \
                        INNER JOIN agendamento_consulta AS cs \
                        ON an.fk_IdAgendCon = cs.IdAgendCon \
                        INNER JOIN cliente as cl \
                        ON cs.fk_IdCliente = cl.IdCliente \
                        WHERE dataAgendCon = '{data}' \
                        ORDER BY YEAR(dataAgendCon) ASC, \
                        MONTH(dataAgendCon) ASC, \
                        DAY(dataAgendCon) ASC,\
                        HOUR(horarioAgendCon)ASC;")

    resultado = con.cursor.fetchall()
    
    return resultado