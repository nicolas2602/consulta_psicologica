-- SQLBook: Code

-- Criar o banco de dados
CREATE DATABASE consulta_psicologica;

-- Excluir o banco de dados
DROP DATABASE consulta_psicologica;

-- Usar o banco de dados
USE consulta_psicologica;

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