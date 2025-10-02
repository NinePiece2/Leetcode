WITH T AS(
        SELECT requester_id, accepter_id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id, requester_id FROM RequestAccepted
    )
SELECT requester_id AS id, COUNT(1) AS num
FROM T
GROUP BY requester_id
ORDER BY num DESC
LIMIT 1
