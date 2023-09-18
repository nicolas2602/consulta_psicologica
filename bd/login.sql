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

SELECT nomeUsuario, senhaUsuario FROM usuario;