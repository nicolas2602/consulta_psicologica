-- SQLBook: Code

-- Criar o banco de dados
CREATE DATABASE consulta_psicologica;

-- Excluir o banco de dados
DROP DATABASE consulta_psicologica;

-- Usar o banco de dados
USE consulta_psicologica;

/* Criar a tabela agenda e seus atributos */
CREATE TABLE agendamento_consulta(
    IdAgendCon INT PRIMARY KEY AUTO_INCREMENT,
    dataAgendCon DATE NOT NULL,
    horarioAgendCon TIME NOT NULL
);

-- Alterar a tabela agenda adicionando as chaves estrangeiras
ALTER TABLE agendamento_consulta
    ADD fk_IdCliente INT NOT NULL,
    ADD FOREIGN KEY (fk_IdCliente) REFERENCES cliente(IdCliente);

-- Inserir dados na tabela agenda
INSERT INTO agendamento_consulta SET dataAgendCon=STR_TO_DATE('21/08/2023','%d/%m/%Y'), horarioAgendCon='14:00:00', fk_IdCliente = 1;
INSERT INTO agendamento_consulta(dataAgendCon, horarioAgendCon, fk_IdCliente) VALUES (STR_TO_DATE('21/08/2023','%d/%m/%Y'), '14:00:00', 1);

-- Exibir os dados da tabela agenda com datas e horários formatados para o padrão brasileiro
SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon,
        TIME_FORMAT(horarioAgendCon, '%H:%m') AS horarioAgendCon,
        nomeCliente
FROM agendamento_consulta as cs 
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente;

-- Atualizar os dados da tabela agenda
UPDATE agendamento_consulta SET dataAgendCon='2023-08-22' WHERE IdAgendCon=2;

-- Excluir os dados da tabela agenda
DELETE FROM agendamento_consulta WHERE IdAgendCon=2;

-- Campo de pesquisa (antigo)
-- SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon,
--         TIME_FORMAT(horarioAgendCon, '%H:%m') AS horarioAgendCon,
--         nomeCliente
-- FROM agendamento_consulta as cs 
-- INNER JOIN cliente as cl 
-- ON cs.fk_IdCliente = cl.IdCliente
-- WHERE nomeCliente like '%Nicolas%'
-- OR dataAgendCon like '21/08/2023';

-- Campo de pesquisa (novo)
SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon,
        TIME_FORMAT(horarioAgendCon, '%H:%m') AS horarioAgendCon,
        nomeCliente
FROM agendamento_consulta as cs 
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente
WHERE nomeCliente like '%Gabriel%'
AND dataAgendCon like STR_TO_DATE('24/09/2023','%d/%m/%Y');

-- Ordenação crescente da data
SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon,
        TIME_FORMAT(horarioAgendCon, '%H:%m') AS horarioAgendCon,
        nomeCliente
FROM agendamento_consulta as cs 
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente
ORDER BY YEAR(dataAgendCon) ASC, 
         MONTH(dataAgendCon) ASC, 
         DAY(dataAgendCon) ASC,
         horarioAgendCon ASC;

-- Ordenação decrescente da data
SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon,
        TIME_FORMAT(horarioAgendCon, '%H:%m') AS horarioAgendCon,
        nomeCliente
FROM agendamento_consulta as cs 
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente
ORDER BY YEAR(dataAgendCon) DESC, 
         MONTH(dataAgendCon) DESC, 
         DAY(dataAgendCon) DESC,
         horarioAgendCon DESC;

-- Campo de pesquisa com ordenação
SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon,
        TIME_FORMAT(horarioAgendCon, '%H:%m') AS horarioAgendCon,
        nomeCliente
FROM agendamento_consulta as cs 
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente
WHERE nomeCliente like '%Nicolas%'
AND dataAgendCon like STR_TO_DATE('24/09/2023','%d/%m/%Y')
ORDER BY YEAR(dataAgendCon) ASC, 
         MONTH(dataAgendCon) ASC, 
         DAY(dataAgendCon) ASC,
         horarioAgendCon ASC;