-- https://www.codewars.com/kata/5820176255c3d23f360000a9
select c.id as category_id, category, title, views, tmp.id as post_id
from categories c
left join lateral (
  select * 
  from posts p
  where category_id = c.id
  order by views desc, p.id asc
  limit 2
) as tmp
on true
order by category, views desc, post_id