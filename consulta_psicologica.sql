-- Active: 1691770896943@@0.0.0.0@3306@consulta_psicologica
CREATE DATABASE consulta_psicologica;

USE consulta_psicologica;

CREATE TABLE cliente(
    IdCliente INT PRIMARY KEY AUTO_INCREMENT,
    nomeCliente VARCHAR(100) NOT NULL,
    emailCliente VARCHAR(100) UNIQUE,
    telefoneCliente VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE agenda(
    IdAgenda INT PRIMARY KEY AUTO_INCREMENT,
    dataAgenda DATE NOT NULL,
    horarioAgenda TIME NOT NULL
);

ALTER TABLE agenda
    ADD fk_IdCliente INT NOT NULL,
    ADD FOREIGN KEY (fk_IdCliente) REFERENCES cliente(IdCliente);

CREATE TABLE assunto(
    IdAssunto INT PRIMARY KEY AUTO_INCREMENT,
    descAssunto VARCHAR(100) NOT NULL
);

ALTER TABLE assunto
    ADD fk_IdAgenda INT NOT NULL,
    ADD FOREIGN KEY (fk_IdAgenda) REFERENCES agenda(IdAgenda);

CREATE TABLE status(
    IdStatus INT PRIMARY KEY AUTO_INCREMENT,
    descStatus VARCHAR(100)
);

CREATE TABLE pagamento(
    IdPagamento INT PRIMARY KEY AUTO_INCREMENT,
    valorPagamento DECIMAL(10,2) NOT NULL
);

ALTER TABLE pagamento
    ADD fk_IdAgenda INT NOT NULL,
    ADD FOREIGN KEY (fk_IdAgenda) REFERENCES agenda(IdAgenda);
    

ALTER TABLE pagamento
    ADD fk_IdStatus INT NOT NULL,
    ADD FOREIGN KEY (fk_IdStatus) REFERENCES status(IdStatus);