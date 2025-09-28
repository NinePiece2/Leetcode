SELECT fromEmp.name AS Employee
FROM Employee fromEmp
JOIN Employee e on fromEmp.managerId = e.id
WHERE fromEmp.salary > e.salary
