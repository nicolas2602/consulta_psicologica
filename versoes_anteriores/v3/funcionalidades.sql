# Pesquisa de cliente
SELECT * FROM cliente
WHERE nomeCliente like '%Nicolas%' 
OR sobrenomeCliente like '%%'
OR emailCliente like '%@gmail%'
OR telefoneCliente like '%11%';

# Pagamento
SELECT IdPagamento, valorPagamento, DATE_FORMAT(dataConsulta, '%d/%m/%Y') AS dataConsulya, 
       TIME_FORMAT(horaConsulta, '%H:%m') AS horarioConsulta, descStatusPag
FROM pagamento AS pg 
INNER JOIN consulta AS ag ON pg.fk_IdConsulta = ag.IdConsulta
INNER JOIN status_pagamento AS st ON pg.fk_IdStatusPag = st.IdStatusPag
WHERE descStatusPag = 'Concluído';

-- Ordenar
SELECT * FROM cliente 
ORDER BY nomeCliente ASC;

SELECT * FROM cliente 
ORDER BY nomeCliente DESC;
