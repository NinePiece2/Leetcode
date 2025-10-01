SELECT name
FROM Employee
JOIN (
    SELECT managerId AS mgrId, COUNT(1) AS cnt
    FROM Employee
    GROUP BY managerId
    HAVING cnt >= 5
) AS j ON id = mgrId

