-- ========================================
-- Bootcamp Remote · Semana 3 · Day16 · B1
-- Tema: Subconsultas, CTEs y Ventanas
-- ========================================

-- 🔄 1. Resetear la tabla si existe
DROP TABLE IF EXISTS empleados;

-- 🏗️ 2. Crear tabla empleados
CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    departamento VARCHAR(50),
    salario NUMERIC
);

-- 📥 3. Insertar datos de ejemplo
INSERT INTO empleados (nombre, departamento, salario)
VALUES
('Ana', 'Ventas', 2000),
('Luis', 'Ventas', 2500),
('Marta', 'Marketing', 2200),
('Pedro', 'Marketing', 2100),
('Sofia', 'IT', 3000),
('Francella', 'IT', 3800);

-- 🔍 4. Ver todos los empleados
SELECT * FROM empleados;

-- 📊 5. Subconsulta: empleados con salario mayor al promedio general
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);

-- 📊 6. CTE (WITH): mismo caso pero más legible
WITH promedio AS (
    SELECT AVG(salario) AS salario_promedio
    FROM empleados
)
SELECT nombre, salario
FROM empleados, promedio
WHERE salario > promedio.salario_promedio;

-- 📊 7. Función de ventana: promedio por departamento (manteniendo filas)
SELECT 
    nombre,
    departamento,
    salario,
    AVG(salario) OVER (PARTITION BY departamento) AS promedio_depto
FROM empleados;

-- 📊 8. GROUP BY: promedio por departamento (resumen)
SELECT 
    departamento, 
    AVG(salario) AS promedio_depto
FROM empleados
GROUP BY departamento;

-- 📊 9. GROUP BY con formato: promedio redondeado a 2 decimales
SELECT 
    departamento, 
    ROUND(AVG(salario), 2) AS promedio_depto
FROM empleados
GROUP BY departamento;

-- 📊 10. GROUP BY con formato: promedio redondeado a 3 decimales
SELECT 
    departamento, 
    ROUND(AVG(salario), 3) AS promedio_depto
FROM empleados
GROUP BY departamento;
