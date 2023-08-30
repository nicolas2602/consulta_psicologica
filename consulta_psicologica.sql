-- SQLBook: Code
/* Criar o banco de dados consulta_psicologica */

CREATE DATABASE consulta_psicologica;

DROP DATABASE consulta_psicologica;

-- Usar o banco de dados

USE consulta_psicologica;

/* Criar a tabela cliente e seus atributos */

CREATE TABLE cliente(
    IdCliente INT PRIMARY KEY AUTO_INCREMENT,
    nomeCliente VARCHAR(100) NOT NULL,
    sobrenomeCliente VARCHAR(100) NOT NULL,
    emailCliente VARCHAR(100) UNIQUE,
    telefoneCliente VARCHAR(100) NOT NULL UNIQUE
);

-- Inserir dados na tabela cliente

INSERT INTO cliente(nomeCliente, sobrenomeCliente, emailCliente, telefoneCliente) VALUES ('Nicolas', 'Yonekawa', 'nicolas@gmail.com', '11996274706');
INSERT INTO cliente(nomeCliente, sobrenomeCliente, emailCliente, telefoneCliente) VALUES ('Gabriel', 'Martins', 'gabriel@gmail.com', '19999553848');

-- Exibir todos os dados da tabela cliente

SELECT * FROM cliente;

-- Atualizar os dados da tabela cliente

UPDATE cliente SET emailCliente='gabriel_ezequiel@gmail.com' WHERE IdCliente=1;

-- Excluir os dados da tabela cliente

DELETE FROM cliente WHERE IdCliente=2;

/* Criar a tabela agenda e seus atributos */

CREATE TABLE consulta(
    IdConsulta INT PRIMARY KEY AUTO_INCREMENT,
    dataConsulta DATE NOT NULL,
    horarioConsulta TIME NOT NULL,
    assuntoConsulta VARCHAR(100) NOT NULL
);

-- Alterar a tabela agenda adicionando as chaves estrangeiras

ALTER TABLE consulta
    ADD fk_IdCliente INT NOT NULL,
    ADD FOREIGN KEY (fk_IdCliente) REFERENCES cliente(IdCliente);

-- Inserir dados na tabela agenda

INSERT INTO consulta (dataConsulta, horarioConsulta, assuntoConsulta, fk_IdCliente) VALUES ('2023-08-20', '14:00:00', 'Problemas',1);

-- Exibir os dados da tabela agenda com datas e horários formatados para o padrão brasileiro

SELECT IdConsulta, DATE_FORMAT(dataConsulta, '%d/%m/%Y') AS dataConsulta,
        TIME_FORMAT(horarioConsulta, '%H:%m') AS horarioConsulta,
        nomeCliente
FROM consulta as cs 
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente;

-- Atualizar os dados da tabela agenda

UPDATE consulta SET dataConsulta='2023-08-22' WHERE IdConsulta=2;

-- Excluir os dados da tabela agenda

DELETE FROM consulta WHERE IdConsulta=2;

/* Criar a tabela assunto e seus atributos */

CREATE TABLE diagnostico(
    IdDiagnostico INT PRIMARY KEY AUTO_INCREMENT,
    descDiagnostico VARCHAR(200) NOT NULL
);

-- Alterar a tabela assunto adicionando as chaves estrangeiras

ALTER TABLE diagnostico
    ADD fk_IdConsulta INT NOT NULL,
    ADD FOREIGN KEY (fk_IdConsulta) REFERENCES consulta(IdConsulta);

-- Inserir dados na tabela assunto

INSERT INTO diagnostico(descDiagnostico, fk_IdConsulta) VALUES ('Assunto 1', 1);

-- Exibir todos dados na tabela assunto

SELECT IdDiagnostico, descDiagnostico, dataConsulta, horarioConsulta
FROM diagnostico AS an
INNER JOIN consulta AS cs
ON an.fk_IdConsulta = cs.IdConsulta

-- Atualizar dados da tabela assunto

UPDATE diagnostico SET descDiagnostico='Assunto 2' WHERE IdDiagnostico=1;

-- Excluir dados da tabela assunto

DELETE FROM diagnostico WHERE IdDiagnostico=1;

/* Criar a tabela status de pagamento e seus atributos */

CREATE TABLE status_pagamento(
    IdStatusPag INT PRIMARY KEY AUTO_INCREMENT,
    descStatusPag VARCHAR(50)
);

-- Inserir os dados possíveis na tabela status de pagamento

INSERT INTO status_pagamento(descStatusPag) VALUES ('Concluído'), ('Pendente');

-- Exibir todos os dados na tabela status de pagamento

SELECT * FROM status_pagamento;

/* Criar a tabela forma de pagamento e seus atributos */
CREATE TABLE forma_pagamento(
    IdFormaPag INT PRIMARY KEY AUTO_INCREMENT,
    descFormaPag VARCHAR(100) 
);

-- Inserir os dados possíveis na tabela forma de pagamento
INSERT INTO forma_pagamento(descFormaPag) VALUES ('Pix'), ('Débito'), ('Crédito'), ('Convênio'), ('Dinheiro');

/* Criar a tabela pagamento e seus atributos */

CREATE TABLE pagamento(
    IdPagamento INT PRIMARY KEY AUTO_INCREMENT,
    valorPagamento DECIMAL(10,2) NOT NULL,
    dataHoraPag DATETIME NOT NULL
);

-- Alterar a tabela pagamento adicionando as chaves estrangeiras

ALTER TABLE pagamento
    ADD fk_IdConsulta INT NOT NULL,
    ADD fk_IdStatusPag INT NOT NULL,
    ADD fk_IdFormaPag INT NOT NULL,
    ADD FOREIGN KEY (fk_IdConsulta) REFERENCES consulta(IdConsulta),
    ADD FOREIGN KEY (fk_IdStatusPag) REFERENCES status_pagamento(IdStatusPag),
    ADD FOREIGN KEY (fk_IdFormaPag) REFERENCES forma_pagamento(IdFormaPag);

-- Inserir os dados na tabela pagamento

INSERT INTO pagamento(valorPagamento, dataHoraPag, fk_IdConsulta, fk_IdStatusPag, fk_IdFormaPag) VALUES (50.00, '2023-09-01 10:10:00', 1, 1, 1);

-- Exibir os dados na tabela pagamento

SELECT IdPagamento, valorPagamento, DATE_FORMAT(dataHoraPag, '%d/%m/%Y') AS 'Data do Pagamento', 
       TIME_FORMAT(dataHoraPag, '%H:%m') AS 'Hora do Pagamento',
       DATE_FORMAT(dataConsulta, '%d/%m/%Y') AS dataConsulta, 
       TIME_FORMAT(horarioConsulta, '%H:%m') AS horarioConsulta, descFormaPag, descStatusPag
FROM pagamento AS pg 
INNER JOIN consulta AS cs ON pg.fk_IdConsulta = cs.IdConsulta
INNER JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag
INNER JOIN status_pagamento AS st ON pg.fk_IdStatusPag = st.IdStatusPag;

-- Atualizar os dados da tabela pagamento

UPDATE pagamento SET valorPagamento=45.00 WHERE IdPagamento=1;

-- Excluir os dados da tabela pagamento

DELETE FROM pagamento WHERE IdPagamento=1;