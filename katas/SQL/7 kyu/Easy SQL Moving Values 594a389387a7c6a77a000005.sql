-- https://www.codewars.com/kata/594a389387a7c6a77a000005
select length(name) as id, length(legs::text) as name, length(arms::text) as legs, length(characteristics) as arms, length(id::text) as characteristics
from monsters 