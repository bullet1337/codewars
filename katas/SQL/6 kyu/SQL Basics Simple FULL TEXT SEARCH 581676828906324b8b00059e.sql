-- https://www.codewars.com/kata/581676828906324b8b00059e
select * 
from product
where to_tsvector(name) @@ to_tsquery('Awesome')