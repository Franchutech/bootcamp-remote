import psycopg2
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Países y regiones disponibles
countries_regions = {
    "Spain": ["Madrid", "Catalonia", "Andalusia", "Basque Country"],
    "France": ["Île-de-France", "Provence-Alpes", "Normandy"],
    "Germany": ["Bavaria", "Berlin", "Hamburg"],
    "Italy": ["Lombardy", "Lazio", "Tuscany"],
    "UK": ["England", "Scotland", "Wales"]
}

# Categorías definidas en el modelo
loyalty_programs = ["Premium", "Gold", "Silver", "Basic"]
purchase_behaviors = ["Frequent", "Occasional", "Promotional"]

# Conexión a Postgres
conn = psycopg2.connect(
    dbname="bootcamp_db",
    user="franchutech",
    password="SantanderWYF*pgSQL25",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insertar clientes (primera prueba)
for _ in range(100):
    country = random.choice(list(countries_regions.keys()))
    region = random.choice(countries_regions[country])
    name = fake.name()
    loyalty_program = random.choice(loyalty_programs)
    purchase_behavior = random.choice(purchase_behaviors)

    cur.execute("""
        INSERT INTO customers (name, country, region, loyalty_program, purchase_behavior)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, country, region, loyalty_program, purchase_behavior))

# Guardar cambios y cerrar conexión
conn.commit()
cur.close()
conn.close()

print("✅ customers inserted successfully!")
