# ml_modelo.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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

# Train/Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar con los datos de entrenamiento
modelo.fit(X_train, y_train)

# Mostrar coeficientes aprendidos
print("\n📈 Modelo entrenado:")
print(f"Pendiente (m): {modelo.coef_[0]}")
print(f"Intercepto (b): {modelo.intercept_}")

# Usar el modelo para predecir las notas de prueba
y_pred = modelo.predict(X_test)

print("\n🔮 Predicciones sobre el set de prueba:")
print("Valores reales:", list(y_test.values))
print("Predicciones  :", list(y_pred))
