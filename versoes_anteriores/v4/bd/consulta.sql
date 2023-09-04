-- SQLBook: Code

-- Criar o banco de dados
CREATE DATABASE consulta_psicologica;

-- Excluir o banco de dados
DROP DATABASE consulta_psicologica;

-- Usar o banco de dados
USE consulta_psicologica;

/* Criar a tabela agenda e seus atributos */
CREATE TABLE consulta(
    IdConsulta INT PRIMARY KEY AUTO_INCREMENT,
    dataConsulta DATE NOT NULL,
    horarioConsulta TIME NOT NULL
);

-- Alterar a tabela agenda adicionando as chaves estrangeiras
ALTER TABLE consulta
    ADD fk_IdCliente INT NOT NULL,
    ADD FOREIGN KEY (fk_IdCliente) REFERENCES cliente(IdCliente);

-- Inserir dados na tabela agenda
INSERT INTO consulta (dataConsulta, horarioConsulta, fk_IdCliente) VALUES ('2023-08-20', '14:00:00', 1);

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