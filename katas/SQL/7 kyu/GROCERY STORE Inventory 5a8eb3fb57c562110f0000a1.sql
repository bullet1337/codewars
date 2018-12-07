-- https://www.codewars.com/kata/5a8eb3fb57c562110f0000a1
select id, name, stock
from products
where stock <= 2 and producent = 'CompanyA'
order by id