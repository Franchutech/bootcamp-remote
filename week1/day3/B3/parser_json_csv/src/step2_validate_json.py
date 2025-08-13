from pathlib import Path
import json
import sys
import re

BASE = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE / "data" / "input.json"

REQUIRED_FIELDS = ["id", "name", "email", "age", "registered_at"]

def load_records(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("El JSON debe ser una lista de objetos.")
    return data

def validate_records(records):
    errors = []
    for idx, record in enumerate(records, 1):
        # 1. Revisar campos obligatorios
        for field in REQUIRED_FIELDS:
            if field not in record:
                errors.append(f"Registro {idx}: falta el campo '{field}'.")
        
        # 2. Revisar tipo de datos
        if "id" in record and not isinstance(record["id"], int):
            errors.append(f"Registro {idx}: 'id' debe ser entero.")
        if "age" in record and not isinstance(record["age"], int):
            errors.append(f"Registro {idx}: 'age' debe ser entero.")
        if "name" in record and not isinstance(record["name"], str):
            errors.append(f"Registro {idx}: 'name' debe ser texto.")
        
        # 3. Validar formato de email
        if "email" in record:
            pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if not re.match(pattern, record["email"]):
                errors.append(f"Registro {idx}: email inválido.")
    return errors

if __name__ == "__main__":
    try:
        records = load_records(INPUT_FILE)
        errors = validate_records(records)
        
        if errors:
            print("❌ Errores encontrados:")
            for err in errors:
                print("-", err)
            sys.exit(1)
        else:
            print("✅ Todos los registros son válidos.")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        sys.exit(1)
