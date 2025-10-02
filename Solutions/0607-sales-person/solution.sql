SELECT SalesPerson.name
FROM SalesPerson
LEFT JOIN Orders ON Orders.sales_id = SalesPerson.sales_id
LEFT JOIN Company ON Orders.com_id = Company.com_id
GROUP BY SalesPerson.sales_id
HAVING IFNULL(SUM(Company.name = "RED"), 0) = 0
