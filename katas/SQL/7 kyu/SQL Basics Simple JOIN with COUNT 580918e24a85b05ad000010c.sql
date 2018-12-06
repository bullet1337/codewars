-- https://www.codewars.com/kata/580918e24a85b05ad000010c
select p.*, count(*) as toy_count
from people p
join toys t on t.people_id = p.id
group by p.id