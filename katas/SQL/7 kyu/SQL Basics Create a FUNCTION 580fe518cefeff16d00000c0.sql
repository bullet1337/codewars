-- https://www.codewars.com/kata/580fe518cefeff16d00000c0
create function increment(arg integer) returns integer as $$
  begin
    return arg + 1;
  end; 
$$ LANGUAGE plpgsql;