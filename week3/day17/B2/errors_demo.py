def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero"
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}"
print(divide(10, 2))
print(divide(10, 0))
print(divide("10", 2))
