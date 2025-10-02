SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC -- COUNT(order_number)
LIMIT 1
