-- https://www.codewars.com/kata/58113a64e10b53ec36000293
select * 
from departments d
where exists (
  select id 
  from sales 
  where department_id = d.id and price > 98
)