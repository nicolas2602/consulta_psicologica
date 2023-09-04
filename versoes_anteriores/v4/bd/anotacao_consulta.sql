-- SQLBook: Code

-- Criar o banco de dados
CREATE DATABASE consulta_psicologica;

-- Excluir o banco de dados
DROP DATABASE consulta_psicologica;

-- Usar o banco de dados
USE consulta_psicologica;

CREATE TABLE anotacao_consulta(
    IdAnotCon INT PRIMARY KEY AUTO_INCREMENT,
    descAnotCon VARCHAR(200) NOT NULL
);

-- Alterar a tabela assunto adicionando as chaves estrangeiras

ALTER TABLE anotacao_consulta
    ADD fk_IdConsulta INT NOT NULL,
    ADD FOREIGN KEY (fk_IdConsulta) REFERENCES consulta(IdConsulta);

-- Inserir dados na tabela assunto

INSERT INTO anotacao_consulta(descAnotCon, fk_IdConsulta) VALUES ('Assunto 1', 1);

-- Exibir todos dados na tabela assunto

SELECT IdAnotCon, descAnotCon, DATE_FORMAT(dataConsulta, '%d/%m/%Y') as dataConsulta, 
       TIME_FORMAT(horarioConsulta, '%H:%m') as horarioConsulta
FROM anotacao_consulta AS an
INNER JOIN consulta AS cs
ON an.fk_IdConsulta = cs.IdConsulta

-- Atualizar dados da tabela assunto

UPDATE anotacao_consulta SET descAnotCon='Assunto 2' WHERE IdAnotCon=1;

-- Excluir dados da tabela assunto

DELETE FROM anotacao_consulta WHERE IdAnotCon=1;