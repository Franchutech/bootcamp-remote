import random
from datetime import datetime, timedelta
from faker import Faker
import psycopg2

# Configuration

DB_NAME = "bootcamp_db"
DB_USER = "bootcamp_1"
DB_PASSWORD = "BCP*sfrc08"
DB_HOST = "localhost"
DB_PORT = "5432"

fake = Faker()

# Conection

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

# Insert Clients

loyalty_levels = ["Basic", "Silver", "Gold", "Premium"]

for _ in range(2000):
    first_name = fake.first_name()
    last_name = fake.last_name()
    country = fake.country()
    loyalty = random.choice(loyalty_levels)
    cur.execute("""
        INSERT INTO bs_customers (first_name, last_name, country, loyalty_program)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, country, loyalty))

# Insert Categories

# Insert Categories
categories = [
    "Fiction", "Fantasy", "Horror", "Science", "Education",
    "Children", "History", "Politics", "Comics", "Comedy",
    "Romance", "Religion", "Non-fiction", "Technology"
]

for c in categories:
    cur.execute("INSERT INTO bs_categories (name) VALUES (%s)", (c,))


#Insert Books

base_books = [
    # Harry Potter (J.K. Rowling)
    ("Harry Potter and the Sorcerer's Stone", "Fantasy", 10.00),
    ("Harry Potter and the Chamber of Secrets", "Fantasy", 11.00),
    ("Harry Potter and the Prisoner of Azkaban", "Fantasy", 12.00),
    ("Harry Potter and the Goblet of Fire", "Fantasy", 13.00),
    ("Harry Potter and the Order of the Phoenix", "Fantasy", 14.00),
    ("Harry Potter and the Half-Blood Prince", "Fantasy", 15.00),
    ("Harry Potter and the Deathly Hallows", "Fantasy", 16.00),

    # El Señor de los Anillos (J.R.R. Tolkien)
    ("The Hobbit", "Fantasy", 15.00),
    ("The Fellowship of the Ring", "Fantasy", 18.00),
    ("The Two Towers", "Fantasy", 18.00),
    ("The Return of the King", "Fantasy", 18.00),

    # La Biblia
    ("The Holy Bible", "Religion", 20.00),

    # Stephen King
    ("The Shining", "Horror", 12.00),
    ("It", "Horror", 14.00),
    ("Carrie", "Horror", 11.00),
    ("Misery", "Horror", 13.00),
    ("Pet Sematary", "Horror", 12.00),
    ("The Green Mile", "Horror", 15.00),
    ("Doctor Sleep", "Horror", 14.00),

    # Ciencia y no-ficción
    ("Sapiens: A Brief History of Humankind", "Non-fiction", 20.00),
    ("Educated", "Non-fiction", 18.00),
    ("Brief Answers to the Big Questions", "Science", 22.00),
    ("Astrophysics for People in a Hurry", "Science", 14.00),
    ("A Brief History of Time", "Science", 25.00),

    # Programación / Tecnología
    ("Clean Code", "Technology", 35.00),
    ("The Pragmatic Programmer", "Technology", 32.00),
    ("Learning SQL", "Education", 30.00),
    ("Python Crash Course", "Education", 28.00),

    # Clásicos
    ("The Great Gatsby", "Fiction", 15.99),
    ("1984", "Fiction", 12.50),
    ("Pride and Prejudice", "Romance", 12.00),
    ("War and Peace", "History", 18.00),
]

# Insertar la lista base

cur.execute("SELECT id, name FROM bs_categories")
cat_map = {name: cid for cid, name in cur.fetchall()}

for title, cat, price, in base_books:
    cur.execute("""
        INSERT INTO bs_books (title, category_id, price)
        VALUES (%s, %s, %s)
""", (title, cat_map[cat], price))
    
# Generate additional random books with Faker

for _ in range(500):
    title = fake.sentence(nb_words=3).replace(".", "")
    cat = random.choice(categories)
    price = round(random.uniform(5, 60),2)  #precios entre 5 y 60 aprox
    cur.execute("""
        INSERT INTO bs_books (title, category_id, price)
        VALUES (%s, %s, %s)
    """, (title, cat_map[cat], price))


# Insert Orders + Order Items


cur.execute("SELECT id FROM bs_customers")
customer_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT id, price FROM bs_books")
books_list = cur.fetchall()

purchase_behaviors = ["Frequent", "Occasional", "Promotional"]

for _ in range(2000):  # 2000 órdenes
    customer_id = random.choice(customer_ids)
    order_date = fake.date_between(start_date="-2y", end_date="today")
    behavior = random.choice(purchase_behaviors)


    cur.execute("""
        INSERT INTO bs_orders (customer_id, order_date, purchase_behavior)
        VALUES (%s, %s, %s) RETURNING id
    """, (customer_id, order_date, behavior))

    order_id = cur.fetchone()[0]

 
    for _ in range(random.randint(1, 4)):
        book_id, price = random.choice(books_list)
        qty = random.randint(1, 3)
        cur.execute("""
            INSERT INTO bs_order_items (order_id, book_id, quantity)
            VALUES (%s, %s, %s)
        """, (order_id, book_id, qty))

# Commit & Close

conn.commit()
cur.close()
conn.close()

print("✅ Data generated succesfully")