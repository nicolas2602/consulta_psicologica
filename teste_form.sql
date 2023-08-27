CREATE TABLE cliente(
    IdCliente INT PRIMARY KEY AUTO_INCREMENT,
    nomeCliente VARCHAR(100) NOT NULL,
    sobrenomeCliente VARCHAR(100) NOT NULL,
    emailCliente VARCHAR(100) UNIQUE,
    telefoneCliente VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO cliente(nomeCliente, sobrenomeCliente, emailCliente, telefoneCliente) VALUES ('Nicolas', 'Yonekawa', 'nicolas@gmail.com', '11996274706');
INSERT INTO cliente(nomeCliente, sobrenomeCliente, emailCliente, telefoneCliente) VALUES ('Gabriel', 'Martins', 'gabriel@gmail.com', '19999553848');

SELECT * FROM cliente;