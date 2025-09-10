# ml_metricas.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Dataset de ejemplo
data = {
    "HorasEstudio": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Nota": [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5]
}
df = pd.DataFrame(data)

# Features (X) y Target (y)
X = df[["HorasEstudio"]]
y = df["Nota"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)

# Métricas
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("📊 Evaluación del modelo:")
print(f"MAE (Error Absoluto Medio): {mae:.4f}")
print(f"RMSE (Error Cuadrático Medio): {rmse:.4f}")
print(f"R² (Coeficiente de determinación): {r2:.4f}")
