-- ========================================
-- Bootcamp Remote · Semana 3 · Day16 · B2
-- Tema: Índices + EXPLAIN / ANALYZE
-- ========================================

-- 🔄 1. Crear índice en la columna "departamento"
CREATE INDEX idx_empleados_departamento 
ON empleados(departamento);

-- 📊 2. Ver plan de ejecución con EXPLAIN
EXPLAIN 
SELECT * 
FROM empleados 
WHERE departamento = 'IT';

-- 📊 3. Ver plan con tiempos reales usando EXPLAIN ANALYZE
EXPLAIN ANALYZE 
SELECT * 
FROM empleados 
WHERE departamento = 'IT';

-- 📥 4. Insertar datos masivos para pruebas de rendimiento (10,000 empleados)
INSERT INTO empleados (nombre, departamento, salario)
SELECT 
    'Empleado' || g, 
    CASE WHEN g % 3 = 0 THEN 'Ventas'
         WHEN g % 3 = 1 THEN 'Marketing'
         ELSE 'IT' END,
    (RANDOM() * 2000 + 2000)::INT
FROM generate_series(1, 10000) g;

-- 📊 5. EXPLAIN ANALYZE después de los datos masivos
EXPLAIN ANALYZE 
SELECT * 
FROM empleados 
WHERE departamento = 'IT';

-- 📌 6. Desactivar uso de índices para forzar un "Seq Scan"
SET enable_indexscan = off;
SET enable_bitmapscan = off;

EXPLAIN ANALYZE 
SELECT * 
FROM empleados 
WHERE departamento = 'IT';

-- ✅ 7. Volver a activar el uso de índices
SET enable_indexscan = on;
SET enable_bitmapscan = on;

-- 📊 8. Comparativa esperada:
-- Con índice: Bitmap Index Scan + Execution Time ~0.8–0.9 ms
-- Sin índice: Seq Scan + Execution Time ~1.1–1.2 ms
-- En tablas reales con millones de filas la diferencia es mucho mayor.
