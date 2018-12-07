-- https://www.codewars.com/kata/5943a58f95d5f72cb900006a
select left(project, commits) as project, right(address, contributors) as address
from repositories 