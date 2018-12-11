-- https://www.codewars.com/kata/594257d4db68b6e99200002c
select project, regexp_replace(address, '[^a-z]', '', 'gi')  as letters, regexp_replace(address, '[^\d]', '', 'g') as numbers
from repositories