from pathlib import Path
import json
import sys

# Carpeta base del mini-proyecto (parser_json_csv)
BASE = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE / "data" / "input.json"

def load_records(path: Path):
    """Carga y devuelve los registros desde un archivo JSON."""
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("El JSON debe ser una lista de objetos (registros).")
    return data

def preview(records, n=3):
    """Muestra un resumen de los primeros registros."""
    print(f"Total de registros: {len(records)}")
    print("Primeros registros:")
    for i, record in enumerate(records[:n], 1):
        print(f"{i:>2}. {record}")

if __name__ == "__main__":
    try:
        records = load_records(INPUT_FILE)
        preview(records)
        print("✅ OK: JSON cargado correctamente.")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        sys.exit(1)
