import psycopg2
import requests

# Conexión a Postgres
conn = psycopg2.connect(
    dbname="bootcamp_db",
    user="franchutech",
    password="SantanderWYF*pgSQL25",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Llamada a la Fake Store API
url = "https://fakestoreapi.com/products"
response = requests.get(url)
products = response.json()

# Insertar productos
for p in products:
    cur.execute("""
        INSERT INTO products (pdt_name, pdt_category, pdt_subcategory, unit_price, unit_cost, rating)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        p["title"],
        p["category"],
        "General",       # La API no trae subcategoría, lo rellenamos
        float(p["price"]),
        round(float(p["price"]) * 0.6, 2),  # Unit cost ~60% del precio
        p["rating"]["rate"]
    ))

conn.commit()
cur.close()
conn.close()

print("✅ products inserted successfully!")
