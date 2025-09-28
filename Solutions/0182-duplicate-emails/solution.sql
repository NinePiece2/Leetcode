-- SELECT DISTINCT p.email as Email
-- FROM Person AS p,
--      Person AS p2
-- WHERE p.id != p2.id AND p.email = p2.email

SELECT email
FROM Person
GROUP BY email
HAVING count(email) > 1
