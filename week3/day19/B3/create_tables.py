import psycopg2

# CONNECT TO POSTGRES
conn = psycopg2.connect(
    dbname = "bootcamp_db",
    user = "franchutech",
    password = "SantanderWYF*pgSQL25",
    host = "localhost",
    port = "5432"
)
# CURSOR

cur = conn.cursor()

# DROP IF EXISTS AND CREATE TABLE CUSTOMERS
# TABLE 1 CUSTOMERS

cur.execute("""
DROP TABLE IF EXISTS customers CASCADE;

CREATE TABLE customers(
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(50),
    region VARCHAR(50),
    loyalty_program VARCHAR(20),      -- Premium, Gold, Silver, Basic
    purchase_behavior VARCHAR(20)     -- Frequent, Occasional, Promotional
);
""")
# TABLE 2 PRODUCTS
cur.execute("""
DROP TABLE IF EXISTS products CASCADE;

CREATE TABLE products(
    product_id SERIAL PRIMARY KEY,
    pdt_name VARCHAR (100),
    pdt_category VARCHAR(50),
    pdt_subcategory VARCHAR(50),
    unit_price NUMERIC, --in €
    unit_cost NUMERIC, --in €
    rating NUMERIC
);
""")
# TABLE 3 ORDERS
cur.execute("""
DROP TABLE IF EXISTS orders CASCADE;

CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    channel VARCHAR(50),  --online, modern, store, wholesaler, institutional
    customer_id INT REFERENCES customers(customer_id)
);
""")
# TABLE 4 ORDER DETAIL
cur.execute("""
DROP TABLE IF EXISTS order_details CASCADE;

CREATE TABLE order_details(
    detail_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    discount NUMERIC,
    total_sale NUMERIC  -- in €
);
""")

conn.commit()
print("✅Tablas creadas de manera satisfactoria")

cur.close()
conn.close()