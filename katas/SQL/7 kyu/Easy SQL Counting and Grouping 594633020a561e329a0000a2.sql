-- https://www.codewars.com/kata/594633020a561e329a0000a2
select race, count(*)
from demographics 
group by race
order by count desc