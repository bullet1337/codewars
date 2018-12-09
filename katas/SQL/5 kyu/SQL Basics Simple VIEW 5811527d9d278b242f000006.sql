-- https://www.codewars.com/kata/5811527d9d278b242f000006
create view members_approved_for_voucher as
  select m.id, m.name, m.email, sum(price) as total_spending
  from members m
  join sales
    on member_id = m.id
  join products p
    on product_id = p.id
  where department_id in (
    select department_id
    from sales s
    join products p
      on product_id = p.id
    group by department_id
    having sum(p.price) > 10000
  )
  group by m.id
  having sum(price) > 1000
  order by m.id;
  
select * 
from members_approved_for_voucher