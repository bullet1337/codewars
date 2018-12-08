-- https://www.codewars.com/kata/5ab828bcedbcfc65ea000099
select pokemon_name, str * multiplier as modifiedStrength, element
from pokemon
join multipliers on element_id = multipliers.id
where str * multiplier >= 40
order by modifiedStrength desc