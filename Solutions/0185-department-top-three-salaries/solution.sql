SELECT 
    Department.name AS Department, 
    Employee.name AS Employee, 
    Employee.salary AS Salary
FROM Employee, Department
WHERE
    Department.id = Employee.departmentId
    AND(SELECT
            COUNT(DISTINCT salary)
        FROM Employee e
        WHERE e.salary > Employee.salary AND e.departmentId = Employee.departmentId
    ) < 3
