# ml_basico.py
import pandas as pd
from sklearn.model_selection import train_test_split

# Dataset de ejemplo
data = {
    "HorasEstudio": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Nota": [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5]
}
df = pd.DataFrame(data)

print("📊 Dataset completo:")
print(df)

# Features (X) y Target (y)
X = df[["HorasEstudio"]]   # variable independiente
y = df["Nota"]             # variable dependiente

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n🟢 Entrenamiento:")
print(X_train, y_train)

print("\n🔵 Prueba:")
print(X_test, y_test)
