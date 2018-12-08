-- https://www.codewars.com/kata/5809575e166583acfa000083
select 
  rank() over(order by sum(points) desc) as rank,
  coalesce(nullif(clan, ''), '[no clan specified]') as clan,
  sum(points) as total_points, 
  count(*) as total_people
from people
group by clan