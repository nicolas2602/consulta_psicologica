SELECT @@lc_time_names;
SET lc_time_names = 'pt_BR';

select MONTHNAME(dataPagamento) as mes, YEAR(dataPagamento) as ano, sum(valorPagamento) as totalPagMes
from pagamento
where fk_IdStatusPag = 1 and dataPagamento like '%2023%'
group by MONTHNAME(dataPagamento), 
         YEAR(dataPagamento);

select YEAR(dataPagamento) as ano
from pagamento
where fk_IdStatusPag = 1
group by YEAR(dataPagamento)
order by YEAR(dataPagamento) DESC;