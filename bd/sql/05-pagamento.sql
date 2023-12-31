-- Active: 1691770896943@@0.0.0.0@3306@consulta_psicologica
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
                    VALUES (1, 50.00, '2023-11-22', 10.00, 11.00, 1, 1, 1);


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