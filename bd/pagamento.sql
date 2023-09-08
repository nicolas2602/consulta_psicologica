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

INSERT INTO status_pagamento(descStatusPag) VALUES ('Concluído'), ('Em andamento'), ('Pendente');

-- Exibir todos os dados na tabela status de pagamento

SELECT * FROM status_pagamento;

/* Criar a tabela forma de pagamento e seus atributos */
CREATE TABLE forma_pagamento(
    IdFormaPag INT PRIMARY KEY AUTO_INCREMENT,
    descFormaPag VARCHAR(100) 
);

-- Inserir os dados possíveis na tabela forma de pagamento
INSERT INTO forma_pagamento(descFormaPag) VALUES ('Pix'), ('Débito'), ('Crédito'), ('Convênio'), ('Dinheiro');

drop table pagamento;

/* Criar a tabela pagamento e seus atributos */
CREATE TABLE pagamento(
    IdPagamento INT PRIMARY KEY AUTO_INCREMENT,
    valorPagamento DECIMAL(10,2),
    dataPagamento DATE
);

-- Alterar a tabela pagamento adicionando as chaves estrangeiras

ALTER TABLE pagamento
    ADD fk_IdAgendCon INT NOT NULL,
    ADD fk_IdStatusPag INT NOT NULL,
    ADD fk_IdFormaPag INT,
    ADD FOREIGN KEY (fk_IdAgendCon) REFERENCES agendamento_consulta(IdAgendCon),
    ADD FOREIGN KEY (fk_IdStatusPag) REFERENCES status_pagamento(IdStatusPag),
    ADD FOREIGN KEY (fk_IdFormaPag) REFERENCES forma_pagamento(IdFormaPag);

-- Inserir os dados na tabela pagamento
INSERT INTO pagamento(valorPagamento, dataPagamento, fk_IdAgendCon, fk_IdStatusPag, fk_IdFormaPag) VALUES (50.00, '2022-09-22', 1, 2, 1);

-- Inserir no início da consulta
INSERT INTO pagamento(valorPagamento, dataPagamento, fk_IdAgendCon, fk_IdStatusPag, fk_IdFormaPag) VALUES (NULL, NULL, 1, 2, NULL);

-- Exibir os dados na tabela pagamento

SELECT IdPagamento, IFNULL(valorPagamento, 'Em acerto'), IFNULL(DATE_FORMAT(dataPagamento, '%d/%m/%Y'), 'Em acerto') as dataPagamento,
       DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon, 
       TIME_FORMAT(horarioAgendCon, '%H:%m') AS horarioAgendCon, IFNULL(descFormaPag, 'Em acerto') AS descFormaPag, descStatusPag
FROM pagamento AS pg 
LEFT JOIN agendamento_consulta AS cs ON pg.fk_IdAgendCon = cs.IdAgendCon
LEFT JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag
LEFT JOIN status_pagamento AS st ON pg.fk_IdStatusPag = st.IdStatusPag;

-- Atualizar os dados da tabela pagamento

UPDATE pagamento SET valorPagamento=45.00 WHERE IdPagamento=1;

-- Excluir os dados da tabela pagamento

DELETE FROM pagamento WHERE IdPagamento=1;