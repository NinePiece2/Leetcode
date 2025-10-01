# Write your MySQL query statement below
DELETE FROM Person
WHERE id not in (SELECT
                    MIN(id)
                    FROM (SELECT * FROM Person) p
                    GROUP BY email
                )
