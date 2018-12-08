-- https://www.codewars.com/kata/5811597e9d278beb04000038
select created_at::date as day, description, count(*)
from events
where name = 'trained'
group by day, description