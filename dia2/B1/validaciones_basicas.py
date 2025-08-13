# Simulamos "datos" que llegarían de un formulario o archivo
nombre = input("Nombre (no vacío): ").strip()
edad_txt = input("Edad (entero >= 0): ").strip()
precio_txt = input("Precio (float > 0): ").strip()

# Validación 1: nombre no vacío
if len(nombre) == 0:
    print("❌ Error: el nombre está vacío.")
else:
    print("✔ Nombre OK")

# Validación 2: edad válida (entero y >= 0)
if not edad_txt.isdigit():
    print("❌ Error: la edad debe ser un entero no negativo.")
else:
    edad = int(edad_txt)
    if edad < 0:
        print("❌ Error: la edad no puede ser negativa.")
    else:
        print("✔ Edad OK")

# Validación 3: precio válido (float y > 0)
try:
    precio = float(precio_txt)
    if precio <= 0:
        print("❌ Error: el precio debe ser mayor que cero.")
    else:
        print("✔ Precio OK")
except ValueError:
    print("❌ Error: el precio debe ser un número (float).")
