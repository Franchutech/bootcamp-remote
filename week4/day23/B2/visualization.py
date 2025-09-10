import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    "sales": [100, 200, 150, 300, 250],
    "expenses": [80, 190, 120, 280, 230]
}
df = pd.DataFrame(data)

print("📊 Dataset:")
print(df)

# Histogram of sales
plt.figure(figsize=(6,4))
sns.histplot(df["sales"], bins=5, kde=True, color="blue")
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("sales_histogram.png")   # Save to file
plt.close()

# Scatter plot: sales vs expenses
plt.figure(figsize=(6,4))
sns.scatterplot(x="sales", y="expenses", data=df)
plt.title("Sales vs Expenses")
plt.savefig("sales_vs_expenses.png")   # Save to file
plt.close()

# Heatmap of correlation
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")   # Save to file
plt.close()

