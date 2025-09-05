import psycopg2
import pandas as pd

# Conexión
conn = psycopg2.connect(
    dbname="bootcamp_db",
    user="franchutech",
    password="SantanderWYF*pgSQL25",
    host="localhost",
    port="5432"
)

# Tablas a validar
tables = ["customers", "products", "orders", "order_details"]

for table in tables:
    print(f"\n🔎 Validating {table}...")

    # Cargar tabla en DataFrame
    df = pd.read_sql(f"SELECT * FROM {table}", conn)

    # 1. Revisión general
    print(df.info())

    # 2. Nulls por columna
    print("\nNulls by column:")
    print(df.isnull().sum())

    # 3. Duplicados
    print("\nDuplicated rows:", df.duplicated().sum())

    # 4. Rangos básicos
    if table == "products":
        print("\nPrice range:", df["unit_price"].min(), "→", df["unit_price"].max())
    if table == "order_details":
        print("\nDiscount range:", df["discount"].min(), "→", df["discount"].max())
        print("Total sales range:", df["total_sale"].min(), "→", df["total_sale"].max())

conn.close()
