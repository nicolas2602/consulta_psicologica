-- Active: 1691770896943@@0.0.0.0@3306@consulta_psicologica
-- Verificar o idioma
SELECT @@lc_time_names;

-- Definir para padrão brasileiro
SET lc_time_names = 'pt_BR';

-- Total de pagamento por mês
SELECT MONTHNAME(dataPagamento) AS mes, YEAR(dataPagamento) AS ano, sum(valorPagamento) AS totalPagMes
FROM pagamento
WHERE fk_IdStatusPag = 1 AND dataPagamento LIKE '%2023%'
GROUP BY MONTHNAME(dataPagamento), 
         YEAR(dataPagamento);

-- Quantidade de status de pagamento por ano
SELECT COUNT(fk_IdStatusPag) AS qtdStatusPag, descStatusPag, 
       SUM(valorPagamento) AS totalPagamento
FROM pagamento AS pg
LEFT JOIN status_pagamento AS st 
ON pg.fk_IdStatusPag = st.IdStatusPag
WHERE YEAR(dataPagamento) = '2023'
GROUP BY IdStatusPag;

-- Total de Pagamento mensal por ano
SELECT YEAR(dataPagamento), MONTHNAME(dataPagamento) AS mes, 
       SUM(valorPagamento) AS totalPagamento
FROM pagamento AS pg
LEFT JOIN status_pagamento AS st 
ON pg.fk_IdStatusPag = st.IdStatusPag
GROUP BY YEAR(dataPagamento), MONTHNAME(dataPagamento);

-- Total de ganhos
SELECT valorPagamento, valorAcrescimo, valorDesconto
FROM pagamento WHERE YEAR(dataPagamento) = '2023' AND fk_IdStatusPag=1;

-- Total de ganhos futuros
SELECT valorPagamento, valorAcrescimo, valorDesconto
FROM pagamento WHERE YEAR(dataPagamento) = '2023' AND fk_IdStatusPag=2;

-- Média por mês
SELECT SUM(valorPagamento) / 12 AS mediaPorMes
FROM pagamento
WHERE YEAR(dataPagamento) = '2023';

-- Valor em Débitos
SELECT valorPagamento, valorAcrescimo, valorDesconto
FROM pagamento 
WHERE YEAR(dataPagamento) = '2023' AND fk_IdStatusPag=3

-- As Formas de Pagamentos mais utilizados
SELECT descFormaPag, COUNT(fk_IdFormaPag) as qtdFormPag
FROM pagamento AS pg 
INNER JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag
GROUP BY IdFormaPag
ORDER BY qtdFormPag DESC;

-- Melhor mês do ano
SELECT MONTHNAME(dataPagamento), SUM(valorPagamento) AS totalPagamentoMensal
FROM pagamento AS pg 
INNER JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag
WHERE YEAR(dataPagamento) = '2023'
GROUP BY YEAR(dataPagamento), MONTHNAME(dataPagamento)
ORDER BY totalPagamentoMensal DESC LIMIT 1;

-- Pior mês do ano
SELECT MONTHNAME(dataPagamento), SUM(valorPagamento) AS totalPagamentoMensal
FROM pagamento AS pg 
INNER JOIN forma_pagamento AS fm ON pg.fk_IdFormaPag = fm.IdFormaPag
WHERE YEAR(dataPagamento) = '2023'
GROUP BY YEAR(dataPagamento), MONTHNAME(dataPagamento)
ORDER BY totalPagamentoMensal ASC LIMIT 1;