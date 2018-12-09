-- https://www.codewars.com/kata/5994dafcbddc2f116d000024
select player_name, games, round(hits::numeric / at_bats, 3)::text as batting_average
from yankees 
where at_bats >= 100
order by batting_average desc