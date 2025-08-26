-- ========================================
-- Bootcamp Remote · Semana 3 · Day16 · B3
-- Tema: Consultas SQL de práctica
-- ========================================

-- 1️⃣ Calcular el salario promedio de todos los empleados
SELECT ROUND(AVG(salario), 2) AS salario_promedio
FROM empleados;

-- 2️⃣ Encontrar el salario máximo y mínimo
SELECT MAX(salario) AS salario_maximo, MIN(salario) AS salario_minimo
FROM empleados;

-- 3️⃣ Listar todos los empleados del departamento de IT
SELECT nombre, salario
FROM empleados
WHERE departamento = 'IT';

-- 4️⃣ Contar cuántos empleados hay en cada departamento
SELECT departamento, COUNT(*) AS total_empleados
FROM empleados
GROUP BY departamento;

-- 5️⃣ Obtener los 3 empleados con mayor salario
SELECT nombre, salario
FROM empleados
ORDER BY salario DESC
LIMIT 3;

-- 6️⃣ Encontrar los empleados cuyo salario está por encima del promedio
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);

-- 7️⃣ Mostrar el salario promedio por departamento
SELECT departamento, ROUND(AVG(salario), 2) AS promedio_depto
FROM empleados
GROUP BY departamento;

-- 8️⃣ Ranking de empleados por salario dentro de cada departamento
SELECT 
    nombre,
    departamento,
    salario,
    RANK() OVER (PARTITION BY departamento ORDER BY salario DESC) AS ranking
FROM empleados;

-- 9️⃣ Mostrar el total de salarios (suma) de todos los empleados
SELECT SUM(salario) AS total_salarios
FROM empleados;

-- 🔟 Encontrar el empleado con el salario más alto de toda la empresa
SELECT nombre, salario
FROM empleados
ORDER BY salario DESC
LIMIT 1;
