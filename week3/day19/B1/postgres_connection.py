import psycopg2

# Configuración de conexión con tus credenciales
conn = psycopg2.connect(
    dbname="bootcamp_db",         # tu base de datos de pruebas
    user="franchutech",           # tu usuario real
    password="SantanderWYF*pgSQL25",  # tu contraseña real
    host="localhost",
    port="5432"
)

# Crear cursor para ejecutar queries
cur = conn.cursor()

# Consulta de prueba: versión de PostgreSQL
cur.execute("SELECT version();")
version = cur.fetchone()
print("✅ Conexión exitosa a PostgreSQL:", version)

# Cerrar conexiones
cur.close()
conn.close()
