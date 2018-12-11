-- https://www.codewars.com/kata/5811010104adbba24b0002fe
create function agecalculator(born_date date) returns int as $$
begin
  return date_part('year', age(now(), born_date));
end; $$
language plpgsql;

