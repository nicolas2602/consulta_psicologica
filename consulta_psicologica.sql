-- SQLBook: Code
/* Criar o banco de dados consulta_psicologica */

CREATE DATABASE consulta_psicologica;

-- Usar o banco de dados

USE consulta_psicologica;

/* Criar a tabela cliente e seus atributos */

CREATE TABLE cliente(
    IdCliente INT PRIMARY KEY AUTO_INCREMENT,
    nomeCliente VARCHAR(100) NOT NULL,
    emailCliente VARCHAR(100) UNIQUE,
    telefoneCliente VARCHAR(100) NOT NULL UNIQUE
);

-- Inserir dados na tabela cliente

INSERT INTO cliente(nomeCliente, emailCliente, telefoneCliente) VALUES ('Nicolas', 'nicolas@gmail.com', '11996274706');
INSERT INTO cliente(nomeCliente, emailCliente, telefoneCliente) VALUES ('Gabriel', 'gabriel@gmail.com', '19999553848');

-- Exibir todos os dados da tabela cliente

SELECT * FROM cliente;

-- Atualizar os dados da tabela cliente

UPDATE cliente SET emailCliente='gabriel_ezequiel@gmail.com' WHERE IdCliente=1;

-- Excluir os dados da tabela cliente

DELETE FROM cliente WHERE IdCliente=2;

/* Criar a tabela agenda e seus atributos */

CREATE TABLE agenda(
    IdAgenda INT PRIMARY KEY AUTO_INCREMENT,
    dataAgenda DATE NOT NULL,
    horarioAgenda TIME NOT NULL
);

-- Alterar a tabela agenda adicionando as chaves estrangeiras

ALTER TABLE agenda
    ADD fk_IdCliente INT NOT NULL,
    ADD FOREIGN KEY (fk_IdCliente) REFERENCES cliente(IdCliente);

-- Inserir dados na tabela agenda

INSERT INTO agenda (dataAgenda, horarioAgenda, fk_IdCliente) values ('2023-08-20', '14:00:00', 1);

-- Exibir os dados da tabela agenda com datas e horários formatados para o padrão brasileiro

SELECT IdAgenda, DATE_FORMAT(dataAgenda, '%d/%m/%Y') AS dataAgenda,
        TIME_FORMAT(horarioAgenda, '%H:%m') AS horarioAgenda,
        nomeCliente
FROM agenda as ag 
INNER JOIN cliente as cl 
ON ag.fk_IdCliente = cl.IdCliente;

-- Atualizar os dados da tabela agenda

UPDATE agenda SET dataAgenda='2023-08-22' WHERE IdAgenda=2;

-- Excluir os dados da tabela agenda

DELETE FROM agenda WHERE IdAgenda=2;

/* Criar a tabela assunto e seus atributos */

CREATE TABLE assunto(
    IdAssunto INT PRIMARY KEY AUTO_INCREMENT,
    descAssunto VARCHAR(100) NOT NULL
);

-- Alterar a tabela assunto adicionando as chaves estrangeiras

ALTER TABLE assunto
    ADD fk_IdAgenda INT NOT NULL,
    ADD FOREIGN KEY (fk_IdAgenda) REFERENCES agenda(IdAgenda);

-- Inserir dados na tabela assunto

INSERT INTO assunto(descAssunto, fk_IdAgenda) VALUES ('Assunto 1', 1);

-- Exibir todos dados na tabela assunto

SELECT IdAssunto, descAssunto, dataAgenda, horarioAgenda 
FROM assunto AS an
INNER JOIN agenda AS ag
ON an.fk_IdAgenda = ag.IdAgenda;

-- Atualizar dados da tabela assunto

UPDATE assunto SET descAssunto='Assunto 2' WHERE IdAssunto=1;

-- Excluir dados da tabela assunto

DELETE FROM assunto WHERE IdAssunto=1;

/* Criar a tabela status e seus atributos */

CREATE TABLE status(
    IdStatus INT PRIMARY KEY AUTO_INCREMENT,
    descStatus VARCHAR(100)
);

-- Inserir os dados possíveis na tabela status

INSERT INTO status(descStatus) VALUES ('Concluído'), ('Em andamento'), ('Pendente');

-- Exibir todos os dados na tabela status

SELECT * FROM status;

/* Criar a tabela pagamento e seus atributos */

CREATE TABLE pagamento(
    IdPagamento INT PRIMARY KEY AUTO_INCREMENT,
    valorPagamento DECIMAL(10,2) NOT NULL
);

-- Alterar a tabela pagamento adicionando as chaves estrangeiras

ALTER TABLE pagamento
    ADD fk_IdAgenda INT NOT NULL,
    ADD FOREIGN KEY (fk_IdAgenda) REFERENCES agenda(IdAgenda);
    

ALTER TABLE pagamento
    ADD fk_IdStatus INT NOT NULL,
    ADD FOREIGN KEY (fk_IdStatus) REFERENCES status(IdStatus);

-- Inserir os dados na tabela pagamento

INSERT INTO pagamento(valorPagamento, fk_IdAgenda, fk_IdStatus) VALUES (50.00, 1, 1);

-- Exibir os dados na tabela pagamento

SELECT IdPagamento, valorPagamento, DATE_FORMAT(dataAgenda, '%d/%m/%Y') AS dataAgenda, 
       TIME_FORMAT(horarioAgenda, '%H:%m') AS horarioAgenda, descStatus
FROM pagamento AS pg 
INNER JOIN agenda AS ag ON pg.fk_IdAgenda = ag.IdAgenda
INNER JOIN status AS st ON pg.fk_IdStatus = st.IdStatus;

-- Atualizar os dados da tabela pagamento

UPDATE pagamento SET valorPagamento=45.00 WHERE IdPagamento=1;

-- Excluir os dados da tabela pagamento

DELETE FROM pagamento WHERE IdPagamento=1;

-- Mostrar a tabela no geral
SELECT IdAssunto, DATE_FORMAT(dataAgenda, '%d/%m/%Y') AS dataAgenda,
        TIME_FORMAT(horarioAgenda, '%H:%m') AS horarioAgenda,
        nomeCliente, descAssunto, valorPagamento, descStatus
FROM agenda AS ag
INNER JOIN cliente AS cl 
ON ag.fk_IdCliente = cl.IdCliente
INNER JOIN assunto AS an      
ON ag.IdAgenda = an.fk_IdAgenda
INNER JOIN pagamento AS pg
ON ag.IdAgenda = pg.fk_IdAgenda
INNER JOIN status AS st  
ON pg.fk_IdStatus = st.IdStatus;

-- Campo de pesquisa
# Agenda em order alfabética
SELECT IdAgenda, DATE_FORMAT(dataAgenda, '%d/%m/%Y') AS dataAgenda,
        TIME_FORMAT(horarioAgenda, '%H:%m') AS horarioAgenda,
        nomeCliente
FROM agenda as ag 
INNER JOIN cliente as cl 
ON ag.fk_IdCliente = cl.IdCliente
WHERE dataAgenda like '%%' 
OR horarioAgenda like '%%'
OR nomeCliente like '%%'
ORDER BY nomeCliente ASC;

SELECT IdAgenda, DATE_FORMAT(dataAgenda, '%d/%m/%Y') AS dataAgenda,
        TIME_FORMAT(horarioAgenda, '%H:%m') AS horarioAgenda,
        nomeCliente
FROM agenda as ag 
INNER JOIN cliente as cl 
ON ag.fk_IdCliente = cl.IdCliente
WHERE dataAgenda like '%%' 
OR horarioAgenda like '%%'
OR nomeCliente like '%%'
ORDER BY nomeCliente DESC;

# Pagamento
SELECT IdPagamento, valorPagamento, DATE_FORMAT(dataAgenda, '%d/%m/%Y') AS dataAgenda, 
       TIME_FORMAT(horarioAgenda, '%H:%m') AS horarioAgenda, descStatus
FROM pagamento AS pg 
INNER JOIN agenda AS ag ON pg.fk_IdAgenda = ag.IdAgenda
INNER JOIN status AS st ON pg.fk_IdStatus = st.IdStatus
WHERE descStatus = 'Concluído';

-- Ordenar
SELECT * FROM cliente 
ORDER BY nomeCliente ASC;