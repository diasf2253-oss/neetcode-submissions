-- Write your query below
SELECT c.name
FROM customers c
WHERE NOT EXISTS (
  SELECT o.customer_id FROM orders o WHERE c.id = o.customer_id
)