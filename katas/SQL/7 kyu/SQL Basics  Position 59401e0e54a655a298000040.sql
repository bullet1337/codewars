-- https://www.codewars.com/kata/59401e0e54a655a298000040
select id, name, position(',' in characteristics) as comma
from monsters 
order by comma