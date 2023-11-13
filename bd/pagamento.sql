-- Active: 1691770896943@@0.0.0.0@3306@consulta_psicologica
-- SQLBook: Code

/* Criar a tabela status de pagamento e seus atributos */
CREATE TABLE IF NOT EXISTS status_pagamento(
    IdStatusPag INT PRIMARY KEY AUTO_INCREMENT,
    descStatusPag VARCHAR(50)
);

-- Inserir os dados possíveis na tabela status de pagamento

INSERT INTO status_pagamento(descStatusPag) VALUES ('Concluído'), ('Em andamento'), ('Pendente');

-- Exibir todos os dados na tabela status de pagamento

SELECT * FROM status_pagamento;

/* Criar a tabela forma de pagamento e seus atributos */
CREATE TABLE IF NOT EXISTS forma_pagamento(
    IdFormaPag INT PRIMARY KEY AUTO_INCREMENT,
    descFormaPag VARCHAR(100) 
);

-- Inserir os dados possíveis na tabela forma de pagamento
INSERT INTO forma_pagamento(descFormaPag) VALUES ('Pix'), ('Débito'), ('Crédito'), ('Convênio'), ('Dinheiro');

UPDATE forma_pagamento SET descFormaPag='Cheque' WHERE IdFormaPag=2;

DELETE FROM forma_pagamento WHERE IdFormaPag=2;

drop table pagamento;

/* Criar a tabela pagamento e seus atributos */
CREATE TABLE IF NOT EXISTS pagamento(
    IdPagamento INT PRIMARY KEY NOT NULL,
    valorPagamento DECIMAL(10,2),
    dataPagamento DATE,
    valorDesconto DECIMAL(10,2),
    valorAcrescimo DECIMAL(10,2)
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
INSERT INTO pagamento(IdPagamento, valorPagamento, dataPagamento, valorDesconto, valorAcrescimo, fk_IdAgendCon, fk_IdStatusPag, fk_IdFormaPag) 
                                    VALUES (1, 50.00, '2022-01-22', 10.00, 11.00, 1, 1, 5), (2, 50.00, '2022-01-22', 10.00, 11.00, 1, 2, 5),
                                            (3, 50.00, '2022-02-22', 10.00, 11.00, 1, 1, 5), (4, 50.00, '2022-02-22', 10.00, 11.00, 1, 2, 5),
                                            (5, 50.00, '2022-03-22', 10.00, 11.00, 1, 1, 5), (6, 50.00, '2022-03-22', 10.00, 11.00, 1, 2, 5),
                                            (7, 50.00, '2022-04-22', 10.00, 11.00, 1, 1, 5), (8, 50.00, '2022-04-22', 10.00, 11.00, 1, 2, 5),
                                            (9, 50.00, '2022-05-22', 10.00, 11.00, 1, 1, 5), (10, 50.00, '2022-05-22', 10.00, 11.00, 1, 2, 5),
                                            (11, 50.00, '2022-06-22', 10.00, 11.00, 1, 1, 5), (12, 50.00, '2022-06-22', 10.00, 11.00, 1, 2, 5),
                                            (13, 50.00, '2022-07-22', 10.00, 11.00, 1, 1, 5), (14, 50.00, '2022-07-22', 10.00, 11.00, 1, 3, 5),
                                            (15, 50.00, '2022-08-22', 10.00, 11.00, 1, 3, 5), (16, 50.00, '2022-08-22', 10.00, 11.00, 1, 3, 5),
                                            (17, 50.00, '2022-09-22', 10.00, 11.00, 1, 3, 5), (18, 50.00, '2022-09-22', 10.00, 11.00, 1, 3, 5),
                                            (19, 50.00, '2022-10-22', 10.00, 11.00, 1, 3, 5), (20, 50.00, '2022-10-22', 10.00, 11.00, 1, 3, 5),
                                            (21, 50.00, '2022-11-22', 10.00, 11.00, 1, 3, 5), (22, 50.00, '2022-11-22', 10.00, 11.00, 1, 3, 5),
                                            (23, 50.00, '2022-12-22', 10.00, 11.00, 1, 3, 5), (24, 50.00, '2022-12-22', 10.00, 11.00, 1, 3, 5);

-- Exibir os dados na tabela pagamento

SELECT IdPagamento, dataAgendCon AS dataAgendCon, 
       horarioAgendCon AS horarioAgendCon, nomeCliente, IFNULL(valorPagamento, 'Em acerto') as valorPagmento,
       IFNULL(dataPagamento, 'Em acerto') as dataPagamento, IFNULL(descFormaPag, 'Em acerto') AS descFormaPag, descStatusPag
FROM pagamento AS pg 
LEFT JOIN agendamento_consulta AS cs ON pg.fk_IdAgendCon = cs.IdAgendCon
LEFT JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente
LEFT JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag
LEFT JOIN status_pagamento AS st ON pg.fk_IdStatusPag = st.IdStatusPag;

-- Atualizar os dados da tabela pagamento

UPDATE pagamento SET valorPagamento=45.00 WHERE IdPagamento=1;

-- Excluir os dados da tabela pagamento
DELETE FROM pagamento WHERE IdPagamento=1;

select * from pagamento;

--Campo de pesquisa com ordenação crescente
SELECT IdPagamento, dataAgendCon, dataAgendCon, 
       horarioAgendCon AS horarioAgendCon, nomeCliente, IFNULL(valorPagamento, 'Em acerto') as valorPagmento,
       IFNULL(dataPagamento, 'Em acerto') as dataPagamento, IFNULL(descFormaPag, 'Em acerto') AS descFormaPag, descStatusPag
FROM pagamento AS pg 
LEFT JOIN agendamento_consulta AS cs ON pg.fk_IdAgendCon = cs.IdAgendCon
LEFT JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente
LEFT JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag
LEFT JOIN status_pagamento AS st ON pg.fk_IdStatusPag = st.IdStatusPag
WHERE nomeCliente like '%Gabriel%' AND 
      dataPagamento BETWEEN '2022-09-22' AND '2023-09-22' AND
      descStatusPag like '%Concluído%'
ORDER BY YEAR(dataAgendCon) ASC, 
         MONTH(dataAgendCon) ASC, 
         DAY(dataAgendCon) ASC;

--Campo de pesquisa com ordenação decrescente
SELECT IdPagamento, dataAgendCon, dataAgendCon, 
       horarioAgendCon AS horarioAgendCon, nomeCliente, IFNULL(valorPagamento, 'Em acerto') as valorPagmento,
       IFNULL(dataPagamento, 'Em acerto') as dataPagamento, IFNULL(descFormaPag, 'Em acerto') AS descFormaPag, descStatusPag
FROM pagamento AS pg 
LEFT JOIN agendamento_consulta AS cs ON pg.fk_IdAgendCon = cs.IdAgendCon
LEFT JOIN cliente as cl ON cs.fk_IdCliente = cl.IdCliente
LEFT JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag
LEFT JOIN status_pagamento AS st ON pg.fk_IdStatusPag = st.IdStatusPag
WHERE nomeCliente like '%Nicolas%' AND 
      dataPagamento BETWEEN '2022-09-22' AND '2023-09-22' AND
      descStatusPag like '%Concluído%'
ORDER BY YEAR(dataAgendCon) DESC, 
         MONTH(dataAgendCon) DESC, 
         DAY(dataAgendCon) DESC;