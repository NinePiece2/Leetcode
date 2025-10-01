SELECT w.id
FROM Weather w
JOIN Weather w2 ON w.temperature > w2.temperature AND SUBDATE(w.recordDate, 1) = w2.recordDate

