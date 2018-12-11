-- https://www.codewars.com/kata/5982020284a83baf2f00001c
with pivot as (
  select 
    product_id,
    count(*) filter (where detail = 'good') as good,
    count(*) filter (where detail = 'ok') as ok,
    count(*) filter (where detail = 'bad') as bad
  from details
  group by product_id
)

select name, good, ok, bad
from products
join pivot 
  on id = product_id
order by name