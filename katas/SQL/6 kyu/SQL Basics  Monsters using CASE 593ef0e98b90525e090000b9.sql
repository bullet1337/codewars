-- https://www.codewars.com/kata/593ef0e98b90525e090000b9
select *, 
  case 
    when heads > arms or tails > legs
      then 'BEAST'
      else 'WEIRDO'
  end as species
from top_half 
natural join bottom_half
order by species