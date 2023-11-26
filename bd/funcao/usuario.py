import bd.funcao.conexao as con
from modulos.Criptografia import Criptografia

cript = Criptografia()

def valorFixo():
    sql = f"SELECT valorFixo FROM valor_fixo WHERE IdValor='1';"
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()

    return resultado

def updateValorFixo(novoValor):
    sql = f"UPDATE valor_fixo SET valorFixo='{novoValor}' WHERE IdValor='1'"
    con.cursor.execute(sql)
    con.conexao.commit()

def selectUsuario():
    sql = f"SELECT nomeUsuario FROM usuario WHERE IdUsuario='2';"
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()

    return resultado

def selectSenha():
    sql = f"SELECT senhaUsuario FROM usuario WHERE IdUsuario='2';"
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()

    return resultado

def updateUsuarioSenha(novoUsuario,novaSenha):
    sql = f"UPDATE usuario SET nomeUsuario='{novoUsuario}',senhaUsuario='{cript.codificar(novaSenha)}' WHERE IdUsuario='2'"
    con.cursor.execute(sql)
    con.conexao.commit()


def selectHorarios():
    sql = f"SELECT * FROM horario_atendimento;"
    try:
        con.cursor.execute(sql)
        resultado = con.cursor.fetchall()
    except:
        resultado = False
    return resultado

def updateHorarios(horaInicio,horaFim, inicioIntervalo, finalIntervalor, sessao):
    sql = f"UPDATE horario_atendimento SET horarioInicialTrab='{horaInicio}',horarioFinalTrab='{horaFim}',\
            horarioIntervInicial='{inicioIntervalo}',horarioIntervFinal='{finalIntervalor}',tempoConsulta='{sessao}' WHERE  IdHorarioAtend='1'"
    
    con.cursor.execute(sql)
    con.conexao.commit()