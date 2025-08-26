-- Insertar clientes
INSERT INTO clientes (nombre, email) VALUES
('Ana Gómez', 'ana@example.com'),
('Juan Pérez', 'juan@example.com'),
('María López', 'maria@example.com');

-- Insertar productos
INSERT INTO productos (nombre, precio) VALUES
('Laptop', 850.00),
('Teclado', 25.50),
('Ratón', 15.00),
('Monitor', 199.99);

-- Insertar pedidos
INSERT INTO pedidos (id_cliente, fecha) VALUES
(1, '2025-08-20'),
(2, '2025-08-21'),
(1, '2025-08-22');

-- Insertar detalle de pedidos
INSERT INTO detalle_pedidos (id_pedido, id_producto, cantidad) VALUES
(1, 1, 1),  -- Ana compra 1 Laptop
(1, 2, 1),  -- Ana compra 1 Teclado
(2, 4, 2),  -- Juan compra 2 Monitores
(3, 3, 1),  -- Ana compra 1 Ratón
(3, 2, 2);  -- Ana compra 2 Teclados
