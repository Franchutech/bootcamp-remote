import numpy as np

print("=== FUNCIONES MATEMÁTICAS AVANZADAS ===")

# Crear un array de ejemplo
data = np.array([1, 4, 9, 16, 25])

print("\nArray original:", data)

# Raíz cuadrada
print("Raíz cuadrada:", np.sqrt(data))

# Funciones trigonométricas
angles = np.array([0, np.pi/2, np.pi])  # 0, 90 y 180 grados en radianes
print("\nÁngulos en radianes:", angles)
print("Seno:", np.sin(angles))
print("Coseno:", np.cos(angles))
print("Tangente:", np.tan(angles))

# Exponenciales y logaritmos
print("\nExponencial (e^x):", np.exp(data))
print("Logaritmo natural (ln):", np.log(data))

# Estadísticas
print("\nPromedio:", np.mean(data))
print("Desviación estándar:", np.std(data))

#Corrección de perfecciones

import numpy as np

# Ángulos en grados
angles_deg = np.array([0, 90, 180])

# Conversión a radianes
angles_rad = np.deg2rad(angles_deg)

# Mostrar de forma más amigable
print("Ángulos en grados:", angles_deg.tolist())
print("Convertidos a radianes:", np.round(angles_rad, 2).tolist())

print("Seno:", np.round(np.sin(angles_rad), 2).tolist())
print("Coseno:", np.round(np.cos(angles_rad), 2).tolist())
print("Tangente:", np.round(np.tan(angles_rad), 2).tolist())

print("\n=== EJERCICIO APLICADO: VENTAS ===")

# Simulamos ventas de 12 meses (en miles de euros)
ventas = np.array([35, 42, 50, 47, 60, 55, 70, 65, 58, 62, 75, 80])

print("\nVentas por mes:", ventas.tolist())

# KPI 1: total anual
print("Total anual de ventas:", ventas.sum())

# KPI 2: promedio mensual
print("Promedio mensual:", round(np.mean(ventas), 2))

# KPI 3: mejor y peor mes
print("Máximo:", ventas.max())
print("Mínimo:", ventas.min())

# KPI 4: desviación estándar (variabilidad)
print("Desviación estándar:", round(np.std(ventas), 2))

# KPI 5: crecimiento entre primer y último mes
crecimiento = ((ventas[-1] - ventas[0]) / ventas[0]) * 100
print("Crecimiento de enero a diciembre:", round(crecimiento, 2), "%")

