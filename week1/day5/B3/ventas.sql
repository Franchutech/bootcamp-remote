-- Borrar tabla si ya existe
DROP TABLE IF EXISTS ventas;

-- Crear tabla ventas
CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto VARCHAR(100),
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    fecha DATE
);

-- Insertar registros de ejemplo
INSERT INTO ventas (producto, cantidad, precio_unitario, fecha) VALUES
('Laptop', 2, 1200.50, '2025-08-10'),
('Teclado', 5, 25.99, '2025-08-11'),
('Monitor', 1, 220.00, '2025-08-12'),
('Laptop', 1, 1200.50, '2025-08-13'),
('Ratón', 3, 15.75, '2025-08-14');
