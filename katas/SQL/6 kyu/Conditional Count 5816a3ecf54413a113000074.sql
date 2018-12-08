-- https://www.codewars.com/kata/5816a3ecf54413a113000074
select 
  date_part('month', payment_date) as month, 
  count(*) as total_count,
  sum(amount) as total_amount,
  count(*) filter(where staff_id = 1) as mike_count,
  sum(amount) filter(where staff_id = 1) as mike_amount,
  count(*) filter(where staff_id = 2) as jon_count,
  sum(amount) filter(where staff_id = 2) as jon_amount
from payment 
group by month
order by month
  