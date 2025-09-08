# Titanic ETL — Load to PostgreSQL

## Objective
The cleaned dataset (`titanic_clean.csv`) was loaded into PostgreSQL using SQLAlchemy, ensuring a professional ETL pipeline.

## Database Configuration
- **DBMS:** PostgreSQL 16  
- **Database:** `bootcamp_db`  
- **User:** `bootcamp_1` (project-specific role with password authentication)  
- **Schema:** `public`  
- **Table:** `titanic_clean`  

## Steps (all in one)

# 1. Create dedicated database role
CREATE ROLE bootcamp_1 LOGIN PASSWORD 'your_password';

# 2. Grant privileges
GRANT ALL PRIVILEGES ON DATABASE bootcamp_db TO bootcamp_1;
GRANT ALL PRIVILEGES ON SCHEMA public TO bootcamp_1;

# 3. Configure connection in etl_load.py
from sqlalchemy import create_engine
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../b1/../data/titanic_clean.csv")
print("Dataset loaded:", df.shape)

# PostgreSQL connection details
USER = "bootcamp_1"
PASSWORD = "your_password"
HOST = "localhost"
PORT = "5432"
DBNAME = "bootcamp_db"

engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
)

# Load into database
table_name = "titanic_clean"
df.to_sql(
    table_name,
    engine,
    schema="public",
    if_exists="replace",
    index=False
)

print(f"✅ Dataset successfully loaded into '{table_name}' in database {DBNAME}.")

# 4. Verify table inside PostgreSQL
\dt public.*
\d titanic_clean
SELECT * FROM titanic_clean LIMIT 5;
