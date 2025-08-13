from pathlib import Path
import json
import sys
import csv

BASE = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE / "data" / "input.json"
OUTPUT_FILE = BASE / "output" / "output.csv"

def load_records(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("El JSON debe ser una lista de objetos.")
    return data

def save_to_csv(records, path: Path):
    if not records:
        raise ValueError("No hay registros para guardar.")
    
    # Usamos las claves del primer registro como encabezados
    headers = records[0].keys()
    
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(records)
    
    print(f"✅ CSV guardado en: {path}")

if __name__ == "__main__":
    try:
        records = load_records(INPUT_FILE)
        save_to_csv(records, OUTPUT_FILE)
    except Exception as e:
        print(f"❌ ERROR: {e}")
        sys.exit(1)
