-- https://www.codewars.com/kata/58126aa90ea99769e7000119
create extension tablefunc;

select name, good, ok, bad
from products
join (
  select * from crosstab('
    select product_id as id, detail, count(*)
    from details
    group by product_id, detail
    order by product_id, detail
  ') as ct(product_id int, bad bigint, good bigint, ok bigint)
) ct
  on id = product_id
order by name