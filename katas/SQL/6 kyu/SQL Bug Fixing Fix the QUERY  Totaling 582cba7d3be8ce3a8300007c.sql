-- https://www.codewars.com/kata/582cba7d3be8ce3a8300007c
select 
  transaction_date::date as day,
  name as department ,
  count(*) sale_count 
from department d
join sale
  on department_id = d.id
group by day, name
order by day asc