import argparse
from src import extract, transform, load

# Configuramos argparse
parser = argparse.ArgumentParser(description="Mini ETL de prueba con CLI")
parser.add_argument(
    "--step",
    type=str,
    required=True,
    choices=["extract", "transform", "load", "all"],
    help="Paso a ejecutar del ETL"
)

args = parser.parse_args()

# Flujo según el argumento recibido
if args.step == "extract":
    data = extract.get_data()
    print(f"Datos extraídos: {data}")

elif args.step == "transform":
    data = [10, 20, 30, 40, 50]  # datos simulados
    clean = transform.clean_data(data)
    print(f"Datos transformados: {clean}")

elif args.step == "load":
    data = [30, 40, 50]  # datos simulados
    load.save_data(data)

elif args.step == "all":
    data = extract.get_data()
    clean = transform.clean_data(data)
    load.save_data(clean)
