-- Active: 1691770896943@@0.0.0.0@3306@consulta_psicologica
-- SQLBook: Code

-- Criar o banco de dados
CREATE DATABASE consulta_psicologica;

-- Excluir o banco de dados
DROP DATABASE consulta_psicologica;

-- Usar o banco de dados
USE consulta_psicologica;

CREATE TABLE IF NOT EXISTS  anotacao_consulta(
    IdAnotCon INT PRIMARY KEY NOT NULL,
    tituloAnotCon VARCHAR(200) NOT NULL,
    descAnotCon VARCHAR(500) NOT NULL
);

-- Alterar a tabela assunto adicionando as chaves estrangeiras

ALTER TABLE anotacao_consulta
    ADD fk_IdAgendCon INT NOT NULL,
    ADD FOREIGN KEY (fk_IdAgendCon) REFERENCES agendamento_consulta(IdAgendCon);

-- Inserir dados na tabela assunto

INSERT INTO anotacao_consulta(IdAnotCon, descAnotCon, tituloAnotCon, fk_IdAgendCon) VALUES (1, 'Assunto 2', 'Titulo', 1);

-- Exibir todos dados na tabela assunto

SELECT IdAnotCon, tituloAnotCon, descAnotCon, dataAgendCon, 
       horarioAgendCon, nomeCliente
FROM anotacao_consulta AS an
INNER JOIN agendamento_consulta AS cs
ON an.fk_IdAgendCon = cs.IdAgendCon
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente;

-- Atualizar dados da tabela assunto

UPDATE anotacao_consulta SET descAnotCon='Assunto 2' WHERE IdAnotCon=1;

-- Excluir dados da tabela assunto

DELETE FROM anotacao_consulta WHERE IdAnotCon=1;

-- Campo de pesquisa com ordenação crescente
SELECT IdAnotCon, tituloAnotCon, descAnotCon, dataAgendCon, 
       horarioAgendCon, nomeCliente
FROM anotacao_consulta AS an
INNER JOIN agendamento_consulta AS cs
ON an.fk_IdAgendCon = cs.IdAgendCon
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente
WHERE nomeCliente like '%Nicolas%' AND
      tituloAnotCon like '%Titulo%'
ORDER BY YEAR(dataAgendCon) ASC, 
         MONTH(dataAgendCon) ASC, 
         DAY(dataAgendCon) ASC;

-- Campo de pesquisa com ordenação decrescente
SELECT IdAnotCon, tituloAnotCon, descAnotCon, dataAgendCon, 
       horarioAgendCon, nomeCliente
FROM anotacao_consulta AS an
INNER JOIN agendamento_consulta AS cs
ON an.fk_IdAgendCon = cs.IdAgendCon
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente
WHERE nomeCliente like '%Nicolas%' AND
      tituloAnotCon like '%Titulo%'
ORDER BY YEAR(dataAgendCon) DESC, 
         MONTH(dataAgendCon) DESC, 
         DAY(dataAgendCon) DESC;
