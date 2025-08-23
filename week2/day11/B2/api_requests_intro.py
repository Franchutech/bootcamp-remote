import requests

# 1. Definir el endpoint:
url = "https://jsonplaceholder.typicode.com/posts"

# 2. Hacer la petición GET
response = requests.get(url)

# 3. Revisar el estado de la respuesta
print("Código de estado:", response.status_code)

# 4. Convertir la respuesta a JSON (lista de diccionarios en Python)
data = response.json()

# 5. Mostrar ejemplos
print("Primer post:", data[0])
print("Segundo post:", data[1])

import json

# Guardar la respuesta completa en un archivo JSON
with open("posts.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Archivo posts.json guardado correctamente.")

import csv

# Guardar los datos en un archivo CSV
with open("posts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("Archivo posts.csv guardado correctamente.")
