CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct e.Salary from Employee e order by e.Salary desc limit N,1
  );
END