-- https://www.codewars.com/kata/589cf45835f99b2909000115
with tmp as (
  select 
    created_at::date as date, 
    count(*)
  from posts
  group by date
  order by date
)
select 
  *, 
  (
    select count(*)
    from posts
    where created_at::date <= date
  ) as total
from tmp
