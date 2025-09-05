import psycopg2
import random

# Conexión a Postgres
conn = psycopg2.connect(
    dbname="bootcamp_db",
    user="franchutech",
    password="SantanderWYF*pgSQL25",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Obtener órdenes y productos
cur.execute("SELECT order_id FROM orders;")
orders = [row[0] for row in cur.fetchall()]

cur.execute("SELECT product_id, unit_price FROM products;")
products = cur.fetchall()  # [(id, price), (id, price)...]

# Insertar order_details
for order_id in orders:
    for _ in range(random.randint(1, 3)):  # cada orden tiene 1 a 3 productos
        product_id, price = random.choice(products)
        price = float(price)  # Convertir a float
        quantity = random.randint(1, 5)
        discount = random.choice([0, 0.05, 0.1, 0.15])
        total_sale = round(quantity * price * (1 - discount), 2)

        cur.execute("""
            INSERT INTO order_details (order_id, product_id, quantity, discount, total_sale)
            VALUES (%s, %s, %s, %s, %s)
        """, (order_id, product_id, quantity, discount, total_sale))

conn.commit()
cur.close()
conn.close()

print("✅ order_details inserted successfully!")

