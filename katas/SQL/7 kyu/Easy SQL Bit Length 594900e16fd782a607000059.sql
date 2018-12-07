-- https://www.codewars.com/kata/594900e16fd782a607000059
select id, bit_length(name) as name, birthday, bit_length(race) as race
from demographics 