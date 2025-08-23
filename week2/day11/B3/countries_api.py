import requests
import json
import csv

# 1. Definir endpoint
url = "https://restcountries.com/v3.1/all"

# 2. Parámetros: qué campos queremos
params = {
    "fields": "name,capital,population,flags"
}

# 3. Hacer GET
response = requests.get(url, params=params)
print("Código de estado:", response.status_code)

# 4. Convertir a JSON
data = response.json()
print("Cantidad de países recibidos:", len(data))

# 5. Guardar en JSON (respaldo completo)
with open("countries.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Archivo countries.json guardado correctamente.")

# 6. Guardar en CSV (solo columnas seleccionadas)
with open("countries.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "capital", "population", "flag"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for country in data:
        writer.writerow({
            "name": country["name"]["common"],
            "capital": country.get("capital", [""])[0] if country.get("capital") else "",
            "population": country.get("population", ""),
            "flag": country["flags"]["png"]
        })

print("Archivo countries.csv guardado correctamente.")

