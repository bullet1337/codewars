-- https://www.codewars.com/kata/5ab7a736edbcfc8e62000007
select senshi_name as sailor_senshi, real_name_jpn as real_name, cats.name as cat, school 
from sailorsenshi
left join cats on cats.id = cat_id
left join schools on schools.id = school_id