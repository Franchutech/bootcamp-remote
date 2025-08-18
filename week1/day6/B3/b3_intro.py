import pandas as pd

def main():
    # 1. EXTRAER: leer datos desde un diccionario (simulando un CSV)
    data = {
        "Producto": ["Laptop", "Teclado", "Ratón", "Monitor"],
        "Precio": [1200, 30, 15, 200],
        "Stock": [10, 50, 150, 20]
    }
    df = pd.DataFrame(data)
    print("Datos cargados:")
    print(df)

    # 2. TRANSFORMAR: ejemplo de limpieza
    df_limpio = df[df["Stock"] > 20]  # Filtrar solo productos con stock mayor a 20
    print("\nDatos después de limpieza:")
    print(df_limpio)

    # 3. CARGAR: guardar resultado en un nuevo CSV
    df_limpio.to_csv("productos_limpios.csv", index=False)
    print("\nArchivo 'productos_limpios.csv' guardado con éxito ✅")

if __name__ == "__main__":
    main()
