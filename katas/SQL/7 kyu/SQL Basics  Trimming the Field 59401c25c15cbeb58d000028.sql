-- https://www.codewars.com/kata/59401c25c15cbeb58d000028
select id, name, split_part(characteristics, ', ', 1) as characteristic
from monsters
order by id