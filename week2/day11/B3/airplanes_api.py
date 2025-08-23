import requests
import json
import csv

# 1. Definir endpoint y API key
url = "http://api.aviationstack.com/v1/flights"
params = {
    "access_key": "1b0eb5ff4e511f20fecb194d518d65ce",
    "limit": 5
}

# 2. Hacer GET
response = requests.get(url, params=params)
print("Código de estado:", response.status_code)

# 3. Convertir a JSON
data = response.json()
flights = data["data"]  # la lista de vuelos está en la clave "data"
print("Cantidad de vuelos recibidos:", len(flights))

# 4. Guardar respaldo en JSON
with open("flights.json", "w", encoding="utf-8") as f:
    json.dump(flights, f, indent=4, ensure_ascii=False)

print("Archivo flights.json guardado correctamente.")

# 4. Guardar respaldo en JSON
with open("flights.json", "w", encoding="utf-8") as f:
    json.dump(flights, f, indent=4, ensure_ascii=False)

print("Archivo flights.json guardado correctamente.")

# 5. Guardar en CSV (campos seleccionados)
with open("flights.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["airline", "flight_number", "departure_airport", "arrival_airport", "status"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for flight in flights:
        writer.writerow({
            "airline": flight["airline"]["name"],
            "flight_number": flight["flight"]["number"],
            "departure_airport": flight["departure"]["airport"],
            "arrival_airport": flight["arrival"]["airport"],
            "status": flight["flight_status"]
        })

print("Archivo flights.csv guardado correctamente.")