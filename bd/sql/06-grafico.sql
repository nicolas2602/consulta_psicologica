-- Active: 1693247688030@@localhost@3306@consulta_psicologica
-- Verificar o idioma
SELECT @@lc_time_names;

-- Definir para padrão brasileiro
SET lc_time_names = 'pt_BR';

USE consulta_psicologica;

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



-- pega dados com a data de agendamento --
SELECT MONTHNAME(dataAgendCon) AS mes, YEAR(dataAgendCon) AS ano, sum(valorPagamento + valorAcrescimo - valorDesconto) AS totalPagMes
FROM pagamento as pg
INNER JOIN agendamento_consulta as ac
ON pg.fk_IdAgendCon = ac.IdAgendCon
WHERE fk_IdStatusPag = 1 AND dataAgendCon LIKE '%2023%'
GROUP BY MONTHNAME(dataAgendCon), 
         YEAR(dataAgendCon);