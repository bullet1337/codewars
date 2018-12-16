-- https://www.codewars.com/kata/59be9f425227ddd60c00003b
with tmp(x) as (
    select *
    from generate_series(2, 100)
)
select x as prime
from tmp
where not exists(
    select *
    from tmp tmp1
    where tmp1.x < tmp.x and tmp.x % tmp1.x = 0
)
