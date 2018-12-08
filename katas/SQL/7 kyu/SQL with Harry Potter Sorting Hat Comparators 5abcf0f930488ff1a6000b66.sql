-- https://www.codewars.com/kata/5abcf0f930488ff1a6000b66
select *
from students
where (quality1 = 'evil' and quality2 = 'cunning')
  or (quality1 = 'brave' and quality2 <> 'evil')
  or (quality1 = 'studious' or quality2 = 'intelligent')
  or (quality1 = 'hufflepuff' or quality2 = 'hufflepuff')
order by id