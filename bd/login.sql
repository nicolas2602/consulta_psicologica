CREATE DATABASE login;

DROP DATABASE login;

USE login;

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

INSERT INTO usuario(nomeUsuario, senhaUsuario, fk_IdPerfil) VALUES ('admin', 'admin12', 1), 
                                                                   ('psico_renata23', 'psico@123', 2);

-- Logar a conta usuária
SELECT * FROM usuario
WHERE nomeUsuario='admin' AND senhaUsuario='admin12';

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
    valorFixo VARCHAR(12) NOT NULL
);

drop table valor_fixo;

ALTER TABLE valor_fixo
ADD fk_IdUsuario INT,
ADD FOREIGN KEY(fk_IdUsuario) REFERENCES usuario(IdUsuario);

SELECT * FROM valor_fixo;

UPDATE valor_fixo SET valorFixo='20.00' WHERE IdValor=1;