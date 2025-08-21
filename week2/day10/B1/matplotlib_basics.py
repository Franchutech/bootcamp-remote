# Gráfico base :

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.savefig("line_plot.png")

# Gráfico #2:

# Datos básicos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear el gráfico de línea con personalización
plt.plot(x, y, color="red", linestyle="--", marker="o")

# Títulos y etiquetas
plt.title("Relación entre X e Y")
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")

# Guardar el gráfico como imagen
plt.savefig("line_plot_custom.png")


# Gráfico de Barras:

# Categorías (ejemplo: productos)
productos = ["A", "B", "C", "D", "E"]
ventas = [50, 80, 30, 100, 60]

plt.bar(productos, ventas, color="skyblue")

plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Unidades vendidas")

plt.savefig("bar_plot.png")

# Histograma:

# Ejemplo: notas de estudiantes
notas = [5, 7, 8, 6, 9, 10, 6, 7, 8, 7, 6, 5, 8, 9, 10, 7, 6, 8, 9, 10]

plt.hist(notas, bins=5, color="green", edgecolor="black")

plt.title("Distribución de notas")
plt.xlabel("Rango de notas")
plt.ylabel("Cantidad de estudiantes")

plt.savefig("hist_plot.png")

# Subplots: varios gráficos en la misma figura
# -------------------------

import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)  # 100 puntos de 0 a 10
y1 = np.sin(x)               # curva seno
y2 = np.cos(x)               # curva coseno

# Crear figura con 2 gráficos (1 fila, 2 columnas)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Primer gráfico: seno
axs[0].plot(x, y1, color="blue")
axs[0].set_title("Función Seno")
axs[0].set_xlabel("x")
axs[0].set_ylabel("sin(x)")

# Segundo gráfico: coseno
axs[1].plot(x, y2, color="red")
axs[1].set_title("Función Coseno")
axs[1].set_xlabel("x")
axs[1].set_ylabel("cos(x)")

# Ajustar y guardar
plt.tight_layout()
plt.savefig("subplots.png")