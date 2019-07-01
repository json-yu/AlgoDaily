-- left join
-- 194 ms, faster than 7.32%
select e.name, b.bonus from Employee e
left join Bonus b on e.empId = b.empId
where b.bonus is null or b.bonus < 1000