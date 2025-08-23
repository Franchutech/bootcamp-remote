import requests

# 1 definir el endpoint:
url = "https://api.nasa.gov/planetary/apod"

params = {
    "api_key": "5DgXtaxi9zKLKAyEbGjew7ccTFbUwWcKsrUDM3gp",
    "date": "2025-08-23"
}

response = requests.get(url, params=params)

print("Código de estado:", response.status_code)

data = response.json()
print(data)

import json
import csv

# Guardar la respuesta de la NASA en un archivo JSON
with open("nasa_apod.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Archivo nasa_apod.json guardado correctamente.")

# Guardar los datos en un archivo CSV (1 fila)
with open("nasa_apod.csv", "w", newline="", encoding="utf-8") as f:
    # Seleccionamos solo ciertas claves relevantes
    fieldnames = ["date", "title", "explanation", "url", "hdurl"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({key: data.get(key, "") for key in fieldnames})

print("Archivo nasa_apod.csv guardado correctamente.")
