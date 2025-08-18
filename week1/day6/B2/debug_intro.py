# debug_intro.py

def calcular_total(precios):
    total = 0
    for precio in precios:
        total += precio
    return total

def main():
    productos = [25.5, 15.0, 120.0, 750.0, 35.0]
    print("Lista de productos:", productos)

    total = calcular_total(productos)
    print("El total es:", total)

if __name__ == "__main__":
    main()
