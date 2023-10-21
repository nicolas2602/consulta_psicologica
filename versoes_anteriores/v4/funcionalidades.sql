-- Pesquisa
SELECT * FROM cliente
WHERE nomeCliente like '%Nicolas%' 

-- Ordenar
# Agendamento_Consulta
SELECT IdConsulta, DATE_FORMAT(dataConsulta, '%d/%m/%Y') AS dataConsulta,
        TIME_FORMAT(horarioConsulta, '%H:%m') AS horarioConsulta,
        nomeCliente
FROM consulta as cs 
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente
ORDER BY YEAR(dataConsulta), 
         MONTH(dataConsulta), 
         DAY(dataConsulta);

SELECT IdConsulta, DATE_FORMAT(dataConsulta, '%d/%m/%Y') AS dataConsulta,
        TIME_FORMAT(horarioConsulta, '%H:%m') AS horarioConsulta,
        nomeCliente
FROM consulta as cs 
INNER JOIN cliente as cl 
ON cs.fk_IdCliente = cl.IdCliente
ORDER BY YEAR(dataConsulta) DESC, 
         MONTH(dataConsulta) DESC, 
         DAY(dataConsulta) DESC;

-- Início e fim
SELECT IdPagamento, valorPagamento, DATE_FORMAT(dataHoraPag, '%d/%m/%Y') AS dataHora, 
       DATE_FORMAT(dataConsulta, '%d/%m/%Y') AS dataConsulta, 
       TIME_FORMAT(horarioConsulta, '%H:%m') AS horarioConsulta, nomeCliente, descFormaPag, descStatusPag
FROM pagamento AS pg 
INNER JOIN consulta AS cs ON pg.fk_IdConsulta = cs.IdConsulta
INNER JOIN cliente AS cl ON cs.fk_IdCliente = cl.IdCliente
INNER JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag
INNER JOIN status_pagamento AS st ON pg.fk_IdStatusPag = st.IdStatusPag
WHERE YEAR(dataHoraPag) BETWEEN '2021' and '2023' AND 
       MONTH(dataHoraPag) BETWEEN '09' and '10'