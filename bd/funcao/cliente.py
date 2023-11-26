import bd.funcao.conexao as con
import modulos.Criptografia as cp

x = cp.Criptografia()

def insert(nome, sobrenome, email, telefone):
    

    con.cursor.execute(f"INSERT INTO cliente(nomeCliente, sobrenomeCliente, emailCliente, telefoneCliente,fk_IdUsuario) \
                       VALUES ('{nome}', '{sobrenome}','{x.codificar(email)}', '{x.codificar(telefone)}','{2}')")
    con.conexao.commit()

def update(id, nome, sobrenome, email, telefone):
    con.cursor.execute(f"UPDATE cliente SET nomeCliente='{nome}', sobrenomeCliente='{sobrenome}', \
                       emailCliente='{x.codificar(email)}', telefoneCliente='{x.codificar(telefone)}' WHERE IdCliente={id}")
    con.conexao.commit()

def delete(id):
    con.cursor.execute(f"DELETE FROM cliente WHERE IdCliente={id};")
    con.conexao.commit()

def select(sql):
    con.cursor.execute(sql)
    resultado = con.cursor.fetchall()

    return resultado

def selectID(id):
    con.cursor.execute(f"SELECT * FROM cliente WHERE IdCliente = {id}")
    resultado = con.cursor.fetchall()

    return resultado

def PesquisaClienteNome(nome):
    con.cursor.execute(f"SELECT * FROM cliente WHERE nomeCliente LIKE '%{nome}%'")
    resultado = con.cursor.fetchall()

    return resultado

def selectClienteNomeSobreNome(nome,sobrenome):
    con.cursor.execute(f"SELECT * FROM cliente WHERE nomeCliente = '{nome}' AND sobrenomeCliente = '{sobrenome}'")
    resultado = con.cursor.fetchall()

    return resultado