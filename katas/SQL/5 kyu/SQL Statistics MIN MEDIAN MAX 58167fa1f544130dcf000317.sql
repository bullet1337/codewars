-- https://www.codewars.com/kata/58167fa1f544130dcf000317
select
  min(score), 
  percentile_cont(0.5) within group (order by score) as median,
  max(score)
from student s
join result
  on student_id = s.id