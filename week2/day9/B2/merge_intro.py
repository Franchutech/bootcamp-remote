import pandas as pd
# Crear Tabla 1: empleados
empleados = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "Marta", "Carlos"],
    "departamento_id": [10, 10, 20, 30]
})

# Crear Tabla 2: departamentos
departamentos = pd.DataFrame({
    "departamento_id": [10, 20],
    "departamento": ["Ventas", "IT"]
})
print(empleados)
print(departamentos)

# INNER JOIN (solo coincidencias)
inner = pd.merge(empleados, departamentos, on="departamento_id", how="inner")
print("\nINNER JOIN:")
print(inner)

# LEFT JOIN (todos los empleados, aunque su departamento no exista en la otra tabla)
left = pd.merge(empleados, departamentos, on="departamento_id", how="left")
print("\nLEFT JOIN:")
print(left)

# RIGHT JOIN (todos los departamentos, aunque no tengan empleados)
right = pd.merge(empleados, departamentos, on="departamento_id", how="right")
print("\nRIGHT JOIN:")
print(right)

# OUTER JOIN (todos los empleados y todos los departamentos, aunque no coincidan)
outer = pd.merge(empleados, departamentos, on="departamento_id", how="outer")
print("\nOUTER JOIN:")
print(outer)