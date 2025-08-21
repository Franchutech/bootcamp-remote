import pandas as pd
data = {
    "empleado": ["Ana", "Luis", "Marta", "Carlos", "Pedro", "Lucía"],
    "departamento": ["Ventas", "Ventas", "IT", "IT", "IT", "RRHH"],
    "salario": [3000, 3200, 4000, 4200, 4100, 2800]
}
df = pd.DataFrame(data)
print(df)

# Agrupación Salario por Departamento (Agrupation salary by department)
salario_promedio = df.groupby("departamento")["salario"].mean()
print(salario_promedio)

#Suma de Salarios por Departamento (Sum salary by department)
salario_suma = df.groupby("departamento")["salario"].sum()
print(salario_suma)

#Conteo de Empleados por Departamento (Employee count by department)
empleados_by_department = df.groupby("departamento")["empleado"].count()
print(empleados_by_department)

# Salario Máximo por Departamento (Max Salary by Department)
salario_maximo = df.groupby("departamento")["salario"].max()
print(salario_maximo)

# Salario Mínimo por Departamento (Minimum salary by department)
salario_minimo = df.groupby("departamento")["salario"].min()
print(salario_minimo)

# Aggregate varias funciones a la misma vez.
resumen_salarios = df.groupby("departamento")["salario"].agg(["mean", "sum", "max", "min", "count"])
print(resumen_salarios)

