import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
data = {
    "sales": [100, 200, 150, 300, 250],
    "expenses": [80, 190, 120, 280, 230]
}
df = pd.DataFrame(data)

print("📊 Dataset:")
print(df)

# 1. Descriptive statistics
print("\n🔹 Basic statistics:")
print(df.describe())

# 2. Correlation matrix
print("\n🔹 Correlation matrix:")
print(df.corr())

# 3. Save visualizations
# Histogram
plt.figure(figsize=(6,4))
sns.histplot(df["sales"], bins=5, kde=True, color="blue")
plt.title("Distribution of Sales")
plt.savefig("sales_histogram.png")
plt.close()

# Scatter plot
plt.figure(figsize=(6,4))
sns.scatterplot(x="sales", y="expenses", data=df)
plt.title("Sales vs Expenses")
plt.savefig("sales_vs_expenses.png")
plt.close()

# Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.close()

print("\n✅ EDA completed. Plots saved as PNG files.")
