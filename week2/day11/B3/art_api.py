import requests
import json
import csv

# 1. Endpoint base para obtener lista de IDs
url_ids = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

# 2. Hacer GET para obtener todos los IDs
response = requests.get(url_ids)
print("Código de estado (IDs):", response.status_code)

data_ids = response.json()
object_ids = data_ids["objectIDs"][:5]  # tomar solo los 5 primeros para la prueba
print("Cantidad de obras seleccionadas:", len(object_ids))

# 3. Para cada ID, pedir la info detallada
artworks = []
for obj_id in object_ids:
    url_obj = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}"
    resp = requests.get(url_obj)
    if resp.status_code == 200:
        artwork = resp.json()
        artworks.append(artwork)

# 4. Guardar todas las obras en JSON
with open("art.json", "w", encoding="utf-8") as f:
    json.dump(artworks, f, indent=4, ensure_ascii=False)

print("Archivo art.json guardado correctamente.")

# 5. Guardar las obras en CSV (columnas seleccionadas)
with open("art.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["objectID", "title", "artistDisplayName", "objectDate", "primaryImageSmall"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for art in artworks:
        writer.writerow({
            "objectID": art.get("objectID", ""),
            "title": art.get("title", ""),
            "artistDisplayName": art.get("artistDisplayName", ""),
            "objectDate": art.get("objectDate", ""),
            "primaryImageSmall": art.get("primaryImageSmall", "")
        })

print("Archivo art.csv guardado correctamente.")
