SELECT @@lc_time_names;

-- Definir para padrão brasileiro
SET lc_time_names = 'pt_BR';

-- Total de pagamento por mês
SELECT MONTHNAME(dataPagamento) AS mes, YEAR(dataPagamento) AS ano, sum(valorPagamento) AS totalPagMes
FROM pagamento
WHERE fk_IdStatusPag = 1 AND dataPagamento LIKE '%2023%'
GROUP BY MONTHNAME(dataPagamento), 
         YEAR(dataPagamento);

-- Quantidade de status por pagamento
SELECT YEAR(dataPagamento) AS ano
FROM pagamento
WHERE fk_IdStatusPag = 1
GROUP BY YEAR(dataPagamento)
ORDER BY YEAR(dataPagamento) DESC;