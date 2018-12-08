-- https://www.codewars.com/kata/5811315e04adbbdb5000050e
select 
  id,
  coalesce(nullif(name, ''), '[product name not found]') as name,
  price,
  coalesce(nullif(card_name , ''), '[card name not found]') as card_name,
  card_number,
  transaction_date
from eusales
where price > 50