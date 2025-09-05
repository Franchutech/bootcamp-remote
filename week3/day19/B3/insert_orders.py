import psycopg2
import random
from datetime import datetime, timedelta

# Conexión a Postgres
conn = psycopg2.connect(
    dbname="bootcamp_db",
    user="franchutech",
    password="SantanderWYF*pgSQL25",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Obtener lista de customers
cur.execute("SELECT customer_id FROM customers;")
customers = [row[0] for row in cur.fetchall()]

# Canales de venta
channels = ["online", "modern", "store", "wholesaler", "institutional"]

# Insertar 200 órdenes
for _ in range(200):
    customer_id = random.choice(customers)
    order_date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 600))
    channel = random.choice(channels)

    cur.execute("""
        INSERT INTO orders (order_date, channel, customer_id)
        VALUES (%s, %s, %s)
    """, (order_date, channel, customer_id))

conn.commit()
cur.close()
conn.close()

print("✅ orders inserted successfully!")
