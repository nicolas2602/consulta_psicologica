-- SQLBook: Code

-- Criar o banco de dados
CREATE DATABASE IF NOT EXISTS consulta_psicologica;

-- Excluir o banco de dados
DROP DATABASE IF EXISTS consulta_psicologica;

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
INSERT INTO agendamento_consulta SET dataAgendCon=STR_TO_DATE('24/09/2023','%d/%m/%Y'), horarioAgendCon='18:00:00', fk_IdCliente = 2;

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

-- Campo de pesquisa e ordenação por data (crescente)
SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon,
        TIME_FORMAT(horarioAgendCon, '%H:%m') AS horarioAgendCon,
        nomeCliente
FROM agendamento_consulta as cs 
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente
WHERE nomeCliente like '%Nicolas%'
AND dataAgendCon like STR_TO_DATE('21/08/2022','%d/%m/%Y')
ORDER BY YEAR(dataAgendCon) ASC, 
         MONTH(dataAgendCon) ASC, 
         DAY(dataAgendCon) ASC;

-- Campo de pesquisa e ordenação por data (decrescente)
SELECT IdAgendCon, DATE_FORMAT(dataAgendCon, '%d/%m/%Y') AS dataAgendCon,
        TIME_FORMAT(horarioAgendCon, '%H:%m') AS horarioAgendCon,
        nomeCliente
FROM agendamento_consulta as cs 
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente
WHERE nomeCliente like '%Nicolas%'
AND dataAgendCon like STR_TO_DATE('21/08/2022','%d/%m/%Y')
ORDER BY YEAR(dataAgendCon) DESC, 
         MONTH(dataAgendCon) DESC, 
         DAY(dataAgendCon) DESC;
