import bd.funcao.conexao as con

def valorFixo():
    sqlLogin = f"SELECT valorFixo FROM valor_fixo WHERE IdValor='1';"
    con.cursor.execute(sqlLogin)
    resultado = con.cursor.fetchall()

    return resultado

def updateValorFixo(novoValor):
    sql = f"UPDATE valor_fixo SET valorFixo='{novoValor}' WHERE IdValor='1'"
    con.cursor.execute(sql)
    con.conexao.commit()

def selectUsuario():
    sqlLogin = f"SELECT nomeUsuario FROM usuario WHERE IdUsuario='2';"
    con.cursor.execute(sqlLogin)
    resultado = con.cursor.fetchall()

    return resultado

def selectSenha():
    sqlLogin = f"SELECT senhaUsuario FROM usuario WHERE IdUsuario='2';"
    con.cursor.execute(sqlLogin)
    resultado = con.cursor.fetchall()

    return resultado

def updateUsuarioSenha(novoUsuario,novaSenha):
    sql = f"UPDATE usuario SET nomeUsuario='{novoUsuario}',senhaUsuario='{novaSenha}' WHERE IdUsuario='2'"
    con.cursor.execute(sql)
    con.conexao.commit()


def selectHorarios():
    sqlLogin = f"SELECT * FROM horario_atendimento;"
    con.cursor.execute(sqlLogin)
    resultado = con.cursor.fetchall()

    return resultado

def updateHorarios(horaInicio,horaFim, inicioIntervalo, finalIntervalor, sessao):
    sql = f"UPDATE horario_atendimento SET horarioInicialTrab='{horaInicio}',horarioFinalTrab='{horaFim}',\
            horarioIntervInicial='{inicioIntervalo}',horarioIntervFinal='{finalIntervalor}',tempoConsulta='{sessao}' WHERE  IdHorarioAtend='1'"
    
    con.cursor.execute(sql)
    con.conexao.commit()