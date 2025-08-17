-- ========================================
-- CRUD completo sobre la tabla productos
-- ========================================

-- 1. Crear tabla productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    stock INT
);

-- 2. Insertar productos de ejemplo
INSERT INTO productos (nombre, precio, stock) VALUES
('Laptop', 1200.50, 10),
('Teclado', 25.99, 50),
('Ratón', 15.75, 80),
('Monitor', 220.00, 20);

-- 3. Actualizar datos (UPDATE)
UPDATE productos
SET precio = 29.99
WHERE nombre = 'Teclado';

UPDATE productos
SET stock = 15
WHERE nombre = 'Monitor';

-- 4. Eliminar datos (DELETE)
DELETE FROM productos
WHERE nombre = 'Ratón';

-- 5. Consultar todo (para verificar)
SELECT * FROM productos;
