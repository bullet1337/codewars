-- https://www.codewars.com/kata/5a8ec692b17101bfc70001ba
select count(name) as unique_products, producer
from products
group by producer
order by unique_products desc, producer asc