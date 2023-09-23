
-- Criar o Banco de Dados
CREATE DATABASE consulta_psicologica;

-- Excluir o banco de dados
DROP DATABASE consulta_psicologica;

-- Usar o banco de dados
USE consulta_psicologica;

-- Tabela de perfil
CREATE TABLE perfil(
    IdPerfil INT PRIMARY KEY AUTO_INCREMENT,
    tipoPerfil VARCHAR(20) UNIQUE
);

INSERT INTO perfil(tipoPerfil) VALUES ('Administrador'), ('Usuário');

SELECT * FROM perfil;

-- Tabela de usuário
CREATE TABLE usuario(
    IdUsuario INT PRIMARY KEY AUTO_INCREMENT,
    nomeUsuario VARCHAR(100) NOT NULL UNIQUE,
    senhaUsuario VARCHAR(10) NOT NULL UNIQUE
);

drop table usuario;

ALTER TABLE usuario
    ADD fk_IdPerfil INT NOT NULL,
    ADD FOREIGN KEY(fk_IdPerfil) REFERENCES perfil(IdPerfil);

INSERT INTO usuario(nomeUsuario, senhaUsuario, fk_IdPerfil) VALUES ('sistem', '1234', 1), 
                                                                   ('psico_renata23', 'psico@123', 2);

-- Logar a conta usuária
SELECT * FROM usuario
WHERE nomeUsuario='sistem' AND senhaUsuario='1234';

UPDATE usuario SET nomeUsuario='psico_renata33', senhaUsuario='psico@123' WHERE IdUsuario=2;

DELETE FROM usuario WHERE IdUsuario=2;

-- Tabela de Horário de Atendimento
CREATE TABLE horario_atendimento (
    IdHorarioAtend INT PRIMARY KEY AUTO_INCREMENT,
    horarioInicialTrab TIME,
    horarioFinalTrab TIME,
    horarioIntervInicial TIME,
    horarioIntervFinal TIME,
    tempoConsulta VARCHAR(2)
);

drop table horario_atendimento;

ALTER TABLE horario_atendimento
    ADD fk_IdUsuario INT NOT NULL UNIQUE,
    ADD FOREIGN KEY(fk_IdUsuario) REFERENCES usuario(IdUsuario);

INSERT INTO horario_atendimento(horarioInicialTrab, horarioFinalTrab, horarioIntervInicial, 
                                           horarioIntervFinal, tempoConsulta, fk_IdUsuario) 
VALUES ('09:09', '17:09', '12:00', '13:00', '30', 2);

SELECT horarioInicialTrab, horarioFinalTrab, horarioIntervInicial, 
       horarioIntervFinal, tempoConsulta, nomeUsuario
FROM horario_atendimento AS ha
RIGHT JOIN usuario AS us
ON ha.fk_IdUsuario = us.IdUsuario;

UPDATE horario_atendimento SET horarioInicialTrab='09:09' WHERE IdHorarioAtend=2;

DELETE FROM horario_atendimento WHERE IdHorarioAtend=1;

-- Tabela de Valor fixo
CREATE TABLE valor_fixo (
    IdValor INT PRIMARY KEY AUTO_INCREMENT,
    valorFixo DECIMAL(10,2) NOT NULL
);

drop table valor_fixo;

ALTER TABLE valor_fixo
    ADD fk_IdUsuario INT,
    ADD FOREIGN KEY(fk_IdUsuario) REFERENCES usuario(IdUsuario);

-- Inserir
INSERT INTO valor_fixo(valorFixo, fk_IdUsuario) VALUES ('20.00', 2);

--Exibir
SELECT * FROM valor_fixo;

-- Atualizar
UPDATE valor_fixo SET valorFixo='20.00' WHERE IdValor=1;

-- Deletar
DELETE FROM valor_fixo WHERE IdValor=1;