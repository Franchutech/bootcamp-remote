USER = "bootcamp_1"
PASSWORD = "BCP*sfrc08" 
HOST = "localhost"
PORT = "5432"
DBNAME = "bootcamp_db"

import pandas as pd
from sqlalchemy import create_engine

# --- 1. Leer dataset limpio ---
df = pd.read_csv("../b1/../data/titanic_clean.csv")
print("Dataset cargado:", df.shape)

# --- 2. Configurar conexión a PostgreSQL ---
engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
)

# --- 3. Cargar DataFrame a SQL ---
table_name = "titanic_clean"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"✅ Dataset cargado en la tabla '{table_name}' de la base de datos {DBNAME}.")
