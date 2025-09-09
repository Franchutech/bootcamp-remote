-- Consulta de negocio #1: ¿Cuál es la categoría de libros que más ingresos ha generado en total?

SELECT
    cat.name AS category,
    SUM(oi.quantity * b.price) AS total_sales
FROM bs_categories cat
JOIN bs_books b ON cat.id = b.category_id
JOIN bs_order_items oi ON b.id = oi.book_id
GROUP BY cat.name
ORDER BY total_sales DESC
LIMIT 1;

-- Consulta de negocio #2: ¿Cuál es el país con mayores ventas totales?

SELECT c.country AS country_name,
    SUM(oi.quantity * b.price) AS total_sales
FROM bs_customers c
JOIN bs_orders o ON c.id = o.customer_id
JOIN bs_order_items oi ON o.id = oi.order_id
JOIN bs_books b ON oi.book_id = b.id
GROUP BY c.country
ORDER BY total_sales DESC
LIMIT 10;

-- Consulta de negocio #3: ¿Cuál es el gasto promedio por cliente?

SELECT c.first_name || ' ' || c.last_name AS full_name,
    c.country,
    AVG(oi.quantity * b.price) AS avg_spent
FROM bs_customers c
JOIN bs_orders o ON c.id =  o.customer_id
JOIN bs_order_items oi ON o.id = oi.order_id
JOIN bs_books b ON oi.book_id = b.id
GROUP BY c.first_name, c.last_name, c.country
ORDER BY avg_spent DESC
LIMIT 10; 

-- Consulta de negocio #4: Obtener el top 5 de libros más vendidos (por cantidad de unidades),
-- mostrando el título del libro, su categoría y el total de unidades vendidas.

SELECT title AS book_name,
    cat.name AS category,
    SUM(oi.quantity) AS total_units_sold
FROM bs_books b
JOIN bs_categories cat ON b.category_id = cat.id
JOIN bs_order_items oi ON b.id = oi.book_id
GROUP BY b.title, cat.name
ORDER BY total_units_sold DESC
LIMIT 5;

-- Consulta de negocio #5: "Obtener las categorías de libros que hayan vendido más de 500 unidades en total,
-- mostrando el nombre de la categoría y el total de unidades vendidas, ordenadas de mayor a menor."

SELECT cat.name AS category_name,
    SUM(oi.quantity) AS total_units_sold
FROM bs_categories cat
JOIN bs_books b ON cat.id = b.category_id
JOIN bs_order_items oi ON b.id = oi.book_id
GROUP BY cat.name
HAVING SUM(oi.quantity) > 500
ORDER BY total_units_sold DESC;

-- Consulta de negocio #6: "Obtener los clientes cuyo gasto total sea mayor que el gasto promedio de todos
-- los clientes, mostrando el nombre completo, país y total gastado."

SELECT
    c.first_name || ' ' || c.last_name AS full_name,
    c.country,
    SUM(oi.quantity * b.price) AS total_spent_client
FROM bs_customers
JOIN bs_orders o ON c.id = o.customer_id
JOIN bs_order_items oi ON o.id = oi.order_id
JOIN bs_books b ON oi.book_id = b.id
GROUP BY c.first_name, c.last_name, c.country
HAVING SUM(oi.quantity * b.price) > (
    SELECT AVG (sub_total)
    FROM (
        SELECT SUM(oi2.quantity * b2.price) AS total_general
        FROM bs_customers c2
        JOIN bs_orders o2 ON c2.id = o2.customer_id
        JOIN bs_order_items oi2 ON o2.id = oi2.order_id
        JOIN bs_books b2 ON oi2.book_id = b2.id
        GROUP BY c2.id
    ) sub
)
ORDER BY total_spent_client
LIMIT 15;

-- Consulta de negocio #7: "Obtener el top 3 de libros más vendidos en cada país,
-- mostrando país, título del libro y total de unidades vendidas."

WITH ventas_por_libro AS (
    SELECT 
        c.country,
        b.title,
        SUM(oi.quantity) AS total_units,
        RANK() OVER (
            PARTITION BY c.country
            ORDER BY SUM(oi.quantity) DESC
        ) AS ranking
    FROM bs_customers c
    JOIN bs_orders o ON c.id = o.customer_id
    JOIN bs_order_items oi ON o.id = oi.order_id
    JOIN bs_books b ON oi.book_id = b.id
    GROUP BY c.country, b.title
)
SELECT country, title, total_units
FROM ventas_por_libro
WHERE ranking <= 3
ORDER BY country, total_units DESC;

-- Consulta de negocio #8: "Obtener el total de ventas por mes en el último año,
-- mostrando el mes y el total de ventas (cantidad × precio)."

SELECT 
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(oi.quantity * b.price) AS total_sales
FROM bs_orders o
JOIN bs_order_items oi ON o.id = oi.order_id
JOIN bs_books b ON oi.book_id = b.id
WHERE o.order_date >= (CURRENT_DATE - INTERVAL '1 year')
GROUP BY DATE_TRUNC('month', o.order_date)
ORDER BY month;
