-- https://www.codewars.com/kata/581fb63e70ca28d92500000d
with tmp(id, department_name, factor) as (
  select *, 1 + pctIncrease(department_id)
  from departments
)
select
  employee_id, first_name, last_name, department_name, 
  salary as old_salary,
  salary * factor as new_salary
from employees
join tmp on department_id = tmp.id
order by employee_id