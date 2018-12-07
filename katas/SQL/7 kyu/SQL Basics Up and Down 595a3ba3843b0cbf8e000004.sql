-- https://www.codewars.com/kata/595a3ba3843b0cbf8e000004
select 
  case 
    when mod(sum(number1), 2) = 0 
      then max(number1)
    else min(number1)
  end as number1,
  case 
    when mod(sum(number2), 2) = 0 
      then max(number2)
    else min(number2)
  end as number2
from numbers