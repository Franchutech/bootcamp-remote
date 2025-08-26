-- 📌 Consulta 1: Ver el detalle de cada pedido con totales por producto
SELECT p.id_pedido,
       c.nombre AS cliente,
       pr.nombre AS producto,
       dp.cantidad,
       pr.precio AS precio_unitario,
       (dp.cantidad * pr.precio) AS total_linea
FROM detalle_pedidos dp
INNER JOIN pedidos p ON dp.id_pedido = p.id_pedido
INNER JOIN clientes c ON p.id_cliente = c.id_cliente
INNER JOIN productos pr ON dp.id_producto = pr.id_producto
ORDER BY p.id_pedido;

-- 📌 Consulta 2: Calcular cuánto gastó cada cliente en total
SELECT c.nombre AS cliente,
       SUM(dp.cantidad * pr.precio) AS total_gastado
FROM detalle_pedidos dp
INNER JOIN pedidos p ON dp.id_pedido = p.id_pedido
INNER JOIN clientes c ON p.id_cliente = c.id_cliente
INNER JOIN productos pr ON dp.id_producto = pr.id_producto
GROUP BY c.nombre
ORDER BY total_gastado DESC;

-- 📌 Consulta 3: Ver los productos más vendidos (por cantidad total)
SELECT pr.nombre AS producto,
       SUM(dp.cantidad) AS cantidad_vendida
FROM detalle_pedidos dp
INNER JOIN productos pr ON dp.id_producto = pr.id_producto
GROUP BY pr.nombre
ORDER BY cantidad_vendida DESC;
