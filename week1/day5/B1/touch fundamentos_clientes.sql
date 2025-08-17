-- Crear base de datos
CREATE DATABASE bootcamp_db;

-- Usar la base
USE bootcamp_db;

-- Crear tabla clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

-- Insertar registros
INSERT INTO clientes (nombre, edad, ciudad) VALUES
('Ana', 25, 'Madrid'),
('Juan', 30, 'Barcelona'),
('María', 22, 'Valencia'),
('Pedro', 35, 'Sevilla');

-- Consultas de práctica
SELECT * FROM clientes;
SELECT nombre, ciudad FROM clientes;
SELECT * FROM clientes WHERE edad > 25;
SELECT * FROM clientes WHERE ciudad = 'Madrid';
SELECT * FROM clientes ORDER BY edad ASC;
SELECT * FROM clientes ORDER BY edad DESC;
SELECT * FROM clientes LIMIT 2;
