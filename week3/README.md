## 📅 Resumen Semana 3 (Días 15 a 21)

- **Día 15 (Lunes):**  
  Introducción a **PostgreSQL**: instalación en Ubuntu WSL, creación de usuario y base de datos `bootcamp_db`.  
  Modelado ER y normalización (3FN) con tablas `estudiantes`, `cursos` e `inscripciones`.  
  Consultas con `INNER JOIN`, uso de alias en tablas y columnas.  
  **Practice (mini-proyecto e-commerce):** tablas `clientes`, `productos`, `pedidos`, `detalle_pedidos`; inserción de datos ficticios y consultas con totales por cliente y productos más vendidos.

- **Día 16 (Martes):**  
  Consultas avanzadas en **PostgreSQL** con la tabla `empleados`: subconsultas, expresiones comunes de tabla (CTEs) y funciones de ventana para cálculos por departamento.  
  Creación de índices e interpretación de planes de ejecución con `EXPLAIN` y `EXPLAIN ANALYZE` para comparar rendimiento con y sin índice en un dataset masivo (10k filas).  
  Ejercicios prácticos de SQL incluyendo agregaciones (`AVG`, `SUM`, `MIN`, `MAX`), filtros (`WHERE`), ordenamientos (`ORDER BY`), límites (`LIMIT`), subconsultas y ranking de empleados por salario.  

  - **Día 17 (Miércoles):**  
  **Python intermedio**: módulos y paquetes, diferencia entre import absoluto y relativo, organización profesional de proyectos con `main.py` y submódulos (`operations`, `utils`).  
  **Manejo de errores** con `try/except`, captura de excepciones específicas y genéricas.  
  **Logging**: uso del módulo `logging` para registrar eventos con distintos niveles (`INFO`, `WARNING`, `ERROR`, `CRITICAL`) y personalización de formato con `basicConfig`.  
  **Argparse (CLI)**: creación de scripts ejecutables desde la terminal con parámetros dinámicos (`--a`, `--b`, `--op`).  
  **Bloque práctico (ETL refactorizado)**: separación en `src/` con módulos `extract.py`, `transform.py`, `load.py` y un `main.py` con argparse que permite ejecutar pasos individuales (`extract`, `transform`, `load`) o el flujo completo (`all`).  

