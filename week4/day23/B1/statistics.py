import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    "sales": [100, 200, 150, 300, 250],
    "expenses": [80, 190, 120, 280, 230]
}
df = pd.DataFrame(data)

print("📊 Dataset:")
print(df)

# Mean
print("\nMean of each column:")
print(df.mean())

# Variance
print("\nVariance of each column:")
print(df.var())

# Correlation
print("\nCorrelation between variables:")
print(df.corr())
