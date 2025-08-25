import requests

# Endpoint de la API de paradas TUS (Transporte Urbano de Santander)
url = "http://datos.santander.es/api/rest/datasets/paradas_bus.json"

# Llamada a la API
response = requests.get(url)

# Comprobamos que la API responde correctamente
if response.status_code == 200:
    print("✅ Conexión exitosa a la API de TUS")
    data = response.json()
    print("Tipo de datos recibido:", type(data))
    # Mostramos solo las claves principales
    print("Claves principales del JSON:", data.keys())
else:
    print("❌ Error en la conexión:", response.status_code)

# Exploramos los primeros registros de resources
resources = data["resources"]

print("\nCantidad total de registros:", len(resources))
print("\nPrimer registro (estructura completa):")
print(resources[0])

import pandas as pd

# Extraemos la lista de paradas
resources = data["resources"]

# Creamos un DataFrame con los campos más relevantes
df = pd.DataFrame(resources)[[
    "dc:identifier",
    "ayto:parada",
    "ayto:sentido",
    "vivo:address1",
    "wgs84_pos:lat",
    "wgs84_pos:long"
]]

# Renombramos las columnas para que sean más legibles
df = df.rename(columns={
    "dc:identifier": "id",
    "ayto:parada": "parada",
    "ayto:sentido": "sentido",
    "vivo:address1": "direccion",
    "wgs84_pos:lat": "latitud",
    "wgs84_pos:long": "longitud"
})

print("\nVista previa del DataFrame:")
print(df.head())

# 🔎 Revisión rápida del DataFrame antes de exportar
print("\n🔎 Revisión rápida del DataFrame:")
print("Duplicados:", df.duplicated().sum())
print("Nulos por columna:\n", df.isnull().sum())
print("Tipos de datos:\n", df.dtypes)

# Convertimos latitud y longitud a números (float) con precisión
df["latitud"] = pd.to_numeric(df["latitud"], errors="coerce")
df["longitud"] = pd.to_numeric(df["longitud"], errors="coerce")

print("\n✅ Conversión de tipos realizada (latitud/longitud → float)")
print("Tipos de datos tras conversión:\n", df.dtypes)

# Guardamos el DataFrame limpio en CSV usando coma como separador decimal
df.to_csv("paradas_tus.csv", index=False, encoding="utf-8", sep=",", decimal=",")
print("\n✅ Archivo 'paradas_tus.csv' guardado correctamente en B1/ con decimales en coma")

# Guardamos copia completa de todos los campos como respaldo
df_full = pd.DataFrame(resources)
df_full.to_csv("paradas_tus_full.csv", index=False, encoding="utf-8")
print("✅ Archivo 'paradas_tus_full.csv' guardado con todos los campos.")
