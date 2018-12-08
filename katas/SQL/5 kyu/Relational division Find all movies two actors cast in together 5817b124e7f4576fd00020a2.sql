-- https://www.codewars.com/kata/5817b124e7f4576fd00020a2
select title
from film f
  join film_actor fa1
    on fa1.film_id = f.film_id
  join film_actor fa2
    on fa2.film_id = f.film_id
  where fa1.actor_id = 105 and fa2.actor_id = 122
order by title