-- https://www.codewars.com/kata/5811501c2d35672d4f000146
with special_sales as (
  select department_id
  from sales 
  where price > 90
)
select * 
from departments
where id in (select * from special_sales)