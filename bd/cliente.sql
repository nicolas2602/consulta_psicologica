-- SQLBook: Code

-- Criar o banco de dados
CREATE DATABASE consulta_psicologica;

-- Excluir o banco de dados
DROP DATABASE consulta_psicologica;

-- Usar o banco de dados
USE consulta_psicologica;

/* Criar a tabela assunto e seus atributos */
CREATE TABLE IF NOT EXISTS  cliente(
    IdCliente INT PRIMARY KEY AUTO_INCREMENT,
    nomeCliente VARCHAR(100) NOT NULL,
    sobrenomeCliente VARCHAR(100) NOT NULL,
    emailCliente VARCHAR(200) UNIQUE,
    telefoneCliente VARCHAR(100) NOT NULL UNIQUE
);

ALTER TABLE cliente
    ADD fk_IdUsuario INT,
    ADD FOREIGN KEY(fk_IdUsuario) REFERENCES usuario(IdUsuario);

-- Inserir dados na tabela cliente

INSERT INTO cliente(nomeCliente, sobrenomeCliente, emailCliente, telefoneCliente, fk_IdUsuario) VALUES ('Nicolas', 'Yonekawa', 'nicolas@gmail.com', '11996274706', 2);
INSERT INTO cliente(nomeCliente, sobrenomeCliente, emailCliente, telefoneCliente, fk_IdUsuario) VALUES ('Gabriel', 'Martins', 'gabriel@gmail.com', '19999553848', 2);

-- Exibir todos os dados da tabela cliente

SELECT * FROM cliente;

-- Atualizar os dados da tabela cliente

UPDATE cliente SET emailCliente='gabriel_ezequiel@gmail.com' WHERE IdCliente=1;

-- Excluir os dados da tabela cliente

DELETE FROM cliente WHERE IdCliente=2;

# Pesquisa o nome do cliente
SELECT * FROM cliente
WHERE nomeCliente like '%Nicolas%' 
OR sobrenomeCliente like '%Yonekawa%'