-- https://www.codewars.com/kata/5802e32dd8c944e562000020
select p.*, c.name as company_name 
from products p
join companies c on c.id = p.company_id