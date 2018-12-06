-- https://www.codewars.com/kata/590ba881fe13cfdcc20001b4
select *
from travelers 
where country not in ('Canada', 'Mexico', 'USA')