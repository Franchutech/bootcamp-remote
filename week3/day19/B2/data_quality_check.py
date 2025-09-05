import psycopg2

# CONECTAR
conn = psycopg2.connect(
    dbname="bootcamp_db",
    user="franchutech",
    password="SantanderWYF*pgSQL25",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# CREAR TABLA PARA PRUEBAS
cur.execute("""
DROP TABLE IF EXISTS empleados_calidad;
            
CREATE TABLE empleados_calidad (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    salario NUMERIC
);
""")
print("✅Tabla 'empleados_calidad' creada.")

# INSERTAR DATASET PARA PRUEBAS (INCLUYE ERRORES INTENCIONALES)
empleados = [
    ("Ana", 3000),
    ("Luis", 2500),
    ("Franchu", 4000),
    (None, 3500),   # Nulo intencional
    ("Pedro", -500), # Salario negativo intencional
    ("Laura", 999999)  #Salario fuera de rango intencional
]

for emp in empleados:
    cur.execute("INSERT INTO empleados_calidad (nombre, salario) VALUES (%s, %s)", emp)

conn.commit()
print("✅ Datos insertados en 'empleados_calidad'.")

# VALIDACIONES DE CALIDAD
# CONTEO TOTAL

cur.execute("SELECT COUNT(*) FROM empleados_calidad;")
total = cur.fetchone()[0]
print(f"📊 Total de registros: {total}")

# DETECTAR NULLS
cur.execute("SELECT COUNT(*) FROM empleados_calidad WHERE nombre IS NULL OR salario IS NULL;")
nulls = cur.fetchone()[0]
print(f"⚠️ Registros con valores nulos: {nulls}")
cur.execute("SELECT * FROM empleados_calidad WHERE nombre IS NULL OR salario IS NULL;")
print("   → Filas con nulls:", cur.fetchall())

# DETECTAR SALARIOS NEGATIVOS
cur.execute("SELECT COUNT(*) FROM empleados_calidad WHERE salario < 0;")
negativos = cur.fetchone()[0]
print(f"⚠️ Registros con salario negativo: {negativos}")
cur.execute("SELECT * FROM empleados_calidad WHERE salario < 0;")
print("   → Filas con salario negativo:", cur.fetchall())

# DETECTAR SALARIOS FUERA DE RANGO
cur.execute("SELECT COUNT(*) FROM empleados_calidad WHERE salario < 1500 OR salario > 6000;")
fuera_rango = cur.fetchone()[0]
print(f"🚫 Registros fuera del rango (1500-6000): {fuera_rango}")
cur.execute("SELECT * FROM empleados_calidad WHERE salario < 1500 OR salario > 6000;")
print("   → Filas fuera de rango:", cur.fetchall())


# CERRAR
cur.close()
conn.close()