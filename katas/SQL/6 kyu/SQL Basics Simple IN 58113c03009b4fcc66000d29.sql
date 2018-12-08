-- https://www.codewars.com/kata/58113c03009b4fcc66000d29
select * 
from departments d 
where id in (
  select department_id
  from sales
  where department_id = d.id and price >= 98
)