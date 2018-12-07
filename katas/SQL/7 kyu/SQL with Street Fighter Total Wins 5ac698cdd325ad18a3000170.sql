-- https://www.codewars.com/kata/5ac698cdd325ad18a3000170
select name, sum(won) as won, sum(lost) as lost
from fighters
join winning_moves on move_id = winning_moves.id
where move not in ('Hadoken', 'Shouoken', 'Kikoken')
group by name
order by won desc
limit 6