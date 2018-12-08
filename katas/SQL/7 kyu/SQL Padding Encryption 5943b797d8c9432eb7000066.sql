-- https://www.codewars.com/kata/5943b797d8c9432eb7000066
select rpad(md5, length(sha256), '1') as md5, lpad(sha1, length(sha256), '0') as sha1, sha256
from encryption