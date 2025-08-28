import psycopg2

DB_CONFIG = {
    "dbname": "postgres",
    "user": "franchutech",
    "password": "SantanderWYF*pgSQL25",
    "host": "localhost",
    "port": "5432"
}

def test_postgres_integration():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Crear tabla temporal
    cur.execute("CREATE TEMP TABLE test_table (id SERIAL PRIMARY KEY, nombre TEXT);")

    # Insertar un valor
    cur.execute("INSERT INTO test_table (nombre) VALUES (%s);", ("Franchu",))

    # Consultar el valor
    cur.execute("SELECT nombre FROM test_table WHERE nombre = %s;", ("Franchu",))
    result = cur.fetchone()

    cur.close()
    conn.close()

    # Verificar resultado
    assert result[0] == "Franchu"


import psycopg2
import pytest

DB_CONFIG = {
    "dbname": "postgres",
    "user": "franchutech",
    "password": "SantanderWYF*pgSQL25",
    "host": "localhost",
    "port": "5432"
}

# 📌 Test 1: conexión + insert + select
def test_postgres_integration():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("CREATE TEMP TABLE test_table (id SERIAL PRIMARY KEY, nombre TEXT);")
    cur.execute("INSERT INTO test_table (nombre) VALUES (%s);", ("Franchu",))
    cur.execute("SELECT nombre FROM test_table WHERE nombre = %s;", ("Franchu",))
    result = cur.fetchone()

    cur.close()
    conn.close()

    assert result[0] == "Franchu"


# 📌 Test 2: insertar múltiples y contar
def test_insert_and_select():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("CREATE TEMP TABLE test_table (id SERIAL PRIMARY KEY, nombre TEXT NOT NULL);")
    cur.execute("INSERT INTO test_table (nombre) VALUES (%s), (%s), (%s);", ("A", "B", "C"))
    cur.execute("SELECT COUNT(*) FROM test_table;")
    result = cur.fetchone()

    cur.close()
    conn.close()

    assert result[0] == 3


# 📌 Test 3: actualizar valor
def test_update_value():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("CREATE TEMP TABLE test_table (id SERIAL PRIMARY KEY, nombre TEXT NOT NULL);")
    cur.execute("INSERT INTO test_table (nombre) VALUES (%s);", ("Viejo",))
    cur.execute("UPDATE test_table SET nombre = %s WHERE nombre = %s;", ("Nuevo", "Viejo"))
    cur.execute("SELECT nombre FROM test_table;")
    result = cur.fetchone()

    cur.close()
    conn.close()

    assert result[0] == "Nuevo"

