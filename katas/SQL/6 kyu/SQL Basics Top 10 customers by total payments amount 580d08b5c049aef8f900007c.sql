-- https://www.codewars.com/kata/580d08b5c049aef8f900007c
select customer_id, email, count(*) as payments_count, sum(amount)::float as total_amount 
from customer c
natural join payment
group by c.customer_id
order by total_amount desc
limit 10