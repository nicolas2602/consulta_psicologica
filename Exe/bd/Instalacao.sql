-- Active: 1693247688030@@localhost@3306@consulta_psicologica


-- Excluir o banco de dados
DROP DATABASE IF EXISTS consulta_psicologica;

-- Criar o Banco de Dados
CREATE DATABASE IF NOT EXISTS consulta_psicologica;

-- Usar o banco de dados
USE consulta_psicologica;

-- ########################################################################
-- Tabela de perfil
CREATE TABLE perfil(
    IdPerfil INT PRIMARY KEY AUTO_INCREMENT,
    tipoPerfil VARCHAR(20) UNIQUE
);
INSERT INTO perfil(tipoPerfil) VALUES ('Administrador'), ('Usuário');

-- Tabela de usuário
CREATE TABLE usuario(
    IdUsuario INT PRIMARY KEY AUTO_INCREMENT,
    nomeUsuario VARCHAR(100) NOT NULL UNIQUE,
    senhaUsuario VARCHAR(100) NOT NULL UNIQUE
);
ALTER TABLE usuario
    ADD fk_IdPerfil INT NOT NULL,
    ADD FOREIGN KEY(fk_IdPerfil) REFERENCES perfil(IdPerfil);

INSERT INTO usuario(nomeUsuario, senhaUsuario, fk_IdPerfil) VALUES ('sistem','m3UR7w==*dm+A6OlUSQXSvo73GJw5Vg==*q0SgTPkfHPy2YHr7bh4ZEw==*nBf3aSzFQPulXSuqMDyZKw==', 1), -- Senha 1234
                                                                   ('user', '5yUP*4blacH66otBdr1w5iMhBPw==*VZuHVPVVAHASmhTGjOef4g==*iFkGzapvX6vQR3MDw0e1jA==', 2);  -- Senha 123

-- Tabela de Horário de Atendimento                                                 
CREATE TABLE horario_atendimento (
    IdHorarioAtend INT PRIMARY KEY AUTO_INCREMENT,
    horarioInicialTrab TIME,
    horarioFinalTrab TIME,
    horarioIntervInicial TIME,
    horarioIntervFinal TIME,
    tempoConsulta VARCHAR(2)
);

ALTER TABLE horario_atendimento
    ADD fk_IdUsuario INT NOT NULL UNIQUE,
    ADD FOREIGN KEY(fk_IdUsuario) REFERENCES usuario(IdUsuario);

INSERT INTO horario_atendimento(horarioInicialTrab, horarioFinalTrab, horarioIntervInicial, 
                                           horarioIntervFinal, tempoConsulta, fk_IdUsuario) 
VALUES ('09:00', '17:00', '12:00', '13:00', '30', 2);

CREATE TABLE valor_fixo (
    IdValor INT PRIMARY KEY AUTO_INCREMENT,
    valorFixo DECIMAL(10,2) NOT NULL
);

ALTER TABLE valor_fixo
    ADD fk_IdUsuario INT,
    ADD FOREIGN KEY(fk_IdUsuario) REFERENCES usuario(IdUsuario);

INSERT INTO valor_fixo(valorFixo, fk_IdUsuario) VALUES ('20.00', 2);

-- ########################################################################

/* Criar a tabela assunto e seus atributos */
CREATE TABLE cliente(
    IdCliente INT PRIMARY KEY AUTO_INCREMENT,
    nomeCliente VARCHAR(100) NOT NULL,
    sobrenomeCliente VARCHAR(100) NOT NULL,
    emailCliente VARCHAR(200) UNIQUE,
    telefoneCliente VARCHAR(100) NOT NULL UNIQUE
);

ALTER TABLE cliente
    ADD fk_IdUsuario INT,
    ADD FOREIGN KEY(fk_IdUsuario) REFERENCES usuario(IdUsuario);

-- ########################################################################

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


-- ########################################################################
/* Criar a tabela anotacao_consulta e seus atributos */
CREATE TABLE anotacao_consulta(
    IdAnotCon INT PRIMARY KEY NOT NULL,
    tituloAnotCon VARCHAR(200) NOT NULL,
    descAnotCon VARCHAR(500) NOT NULL
);

-- Alterar a tabela assunto adicionando as chaves estrangeiras

ALTER TABLE anotacao_consulta
    ADD fk_IdAgendCon INT NOT NULL,
    ADD FOREIGN KEY (fk_IdAgendCon) REFERENCES agendamento_consulta(IdAgendCon);

-- ########################################################################

/* Criar a tabela status de pagamento e seus atributos */
CREATE TABLE status_pagamento(
    IdStatusPag INT PRIMARY KEY AUTO_INCREMENT,
    descStatusPag VARCHAR(50)
);

-- Inserir os dados possíveis na tabela status de pagamento
INSERT INTO status_pagamento(descStatusPag) VALUES ('Concluído'), ('Em andamento'), ('Pendente');

/* Criar a tabela forma de pagamento e seus atributos */
CREATE TABLE forma_pagamento(
    IdFormaPag INT PRIMARY KEY AUTO_INCREMENT,
    descFormaPag VARCHAR(100) 
);

-- Inserir os dados possíveis na tabela forma de pagamento
INSERT INTO forma_pagamento(descFormaPag) VALUES ('Pix'), ('Débito'), ('Crédito'), ('Convênio'), ('Dinheiro');

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