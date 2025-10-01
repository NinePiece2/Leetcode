SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee
LEFT JOIN Department ON Department.id = Employee.departmentId
WHERE (Department.id, salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY 1
)
