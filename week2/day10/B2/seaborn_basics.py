import seaborn as sns
import matplotlib.pyplot as plt

# Dataset de ejemplo integrado en Seaborn
tips = sns.load_dataset("tips")

# Gráfico categórico: total de la cuenta por día
sns.catplot(data=tips, x="day", y="total_bill", kind="strip", jitter=True)

plt.savefig("seaborn_catplot.png")

# Distribución de propinas

sns.histplot(data=tips, x="tip", kde=True, color="orange")

plt.title("Distribución de propinas")
plt.xlabel("Monto de la propina")
plt.ylabel("Frecuencia")

plt.savefig("seaborn_histplot.png")

# Heatmap de correlaciones
# -------------------------

# Matriz de correlación del dataset tips
corr = tips.corr(numeric_only=True)

# Crear mapa de calor
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)

plt.title("Mapa de calor de correlaciones")
plt.savefig("seaborn_heatmap.png")