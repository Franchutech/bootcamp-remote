-- Consulta #1 (SELECT, FROM, JOIN)

SELECT first_name ||' '|| last_name AS full_name,
    c.country,
    o.order_date,
    b.title,
    cat.name,
    oi.quantity
FROM bs_customers c
JOIN bs_orders o ON c.id = o.customer_id
JOIN bs_order_items oi ON o.id = oi.order_id
JOIN bs_books b ON oi.book_id = b.id
JOIN bs_categories cat ON b.category_id = cat.id;

-- Consulta #2 (GROUP BY)

SELECT first_name ||' '|| last_name AS full_name,
    c.country,
    SUM(oi.quantity) AS total_books
FROM bs_customers c
JOIN bs_orders o ON c.id = o.customer_id
JOIN bs_order_items oi ON o.id = oi.order_id
GROUP BY c.first_name, c.last_name, c.country
ORDER BY total_books DESC;

-- Consulta #3 (HAVING, ORDER BY)

SELECT first_name ||' '|| last_name AS full_name,
    c.country,
    SUM(oi.quantity) AS total_books
FROM bs_customers c
JOIN bs_orders o ON c.id = o.customer_id
JOIN bs_order_items oi ON o.id = oi.order_id
GROUP BY c.first_name, c.last_name, c.country
HAVING SUM(oi.quantity) > 30
ORDER BY total_books DESC;

-- Consulta #4 (SUBCONSULTAS)
--¿Qué clientes han gastado más que el promedio de gasto total de todos los clientes?

SELECT first_name ||' '|| last_name AS full_name,
    c.country,
    (SUM(oi.quantity * b.price)) AS total_spent,
FROM bs_customers c
JOIN bs_orders o ON c.id = o.customer_id
JOIN bs_order_items oi ON o.id = oi.order_id
JOIN bs_books b ON oi.book_id = b.id
GROUP BY c.first_name, c.last_name, c.country
HAVING total_spent > MEDIA

-- ¿Qué clientes han gastado más que el promedio?

SELECT 
    c.first_name || ' ' || c.last_name AS full_name,
    c.country,
    SUM(oi.quantity * b.price) AS total_spent
FROM bs_customers c
JOIN bs_orders o ON c.id = o.customer_id
JOIN bs_order_items oi ON o.id = oi.order_id
JOIN bs_books b ON oi.book_id = b.id
GROUP BY c.first_name, c.last_name, c.country
HAVING SUM(oi.quantity * b.price) > (
    SELECT AVG(sub.total)
    FROM (
        SELECT SUM(oi2.quantity * b2.price) AS total
        FROM bs_customers c2
        JOIN bs_orders o2 ON c2.id = o2.customer_id
        JOIN bs_order_items oi2 ON o2.id = oi2.order_id
        JOIN bs_books b2 ON oi2.book_id = b2.id
        GROUP BY c2.id
    ) sub
)
ORDER BY total_spent DESC
LIMIT 10;








    
