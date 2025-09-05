import psycopg2

# Conectar a Postgres
conn = psycopg2.connect(
    dbname="bootcamp_db",
    user="franchutech",
    password="SantanderWYF*pgSQL25",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 1. Eliminar tabla si ya existía y crear una nueva limpia
cur.execute("""
DROP TABLE IF EXISTS empleados_prueba;

CREATE TABLE empleados_prueba (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    salario NUMERIC
);
""")
print("✅ Tabla 'empleados_prueba' creada (limpia).")

# 2. Insertar registros de prueba
cur.execute("INSERT INTO empleados_prueba (nombre, salario) VALUES (%s, %s)", ("Ana", 3000))
cur.execute("INSERT INTO empleados_prueba (nombre, salario) VALUES (%s, %s)", ("Luis", 2500))
print("✅ Registros insertados en 'empleados_prueba'.")

# 3. Confirmar cambios
conn.commit()

# 4. Leer los datos de la tabla de prueba
cur.execute("SELECT * FROM empleados_prueba;")
rows = cur.fetchall()
print("📊 Contenido de la tabla empleados_prueba:")
for row in rows:
    print(row)

# Cerrar conexiones
cur.close()
conn.close()

