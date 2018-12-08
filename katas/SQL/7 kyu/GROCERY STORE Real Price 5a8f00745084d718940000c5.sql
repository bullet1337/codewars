-- https://www.codewars.com/kata/5a8f00745084d718940000c5
select name, weight, price, round((price / (weight / 1000))::numeric, 2)::double precision as price_per_kg
from products
order by price_per_kg, name