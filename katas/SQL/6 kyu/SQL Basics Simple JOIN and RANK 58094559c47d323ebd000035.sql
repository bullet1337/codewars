-- https://www.codewars.com/kata/58094559c47d323ebd000035
select p.*, count(*) as sale_count, rank() over(order by count(*) desc) sale_rank
from people p
join sales
  on people_id = p.id
group by p.id