-- https://www.codewars.com/kata/580fb94e12b34dd1c40001f0
select 
  job_title,
  round(avg(salary)::numeric, 2)::float as average_salary,
  count(*) as total_people,
  round(sum(salary)::numeric, 2)::float as total_salary
from people p
join job
  on people_id = p.id
group by job_title
order by average_salary desc