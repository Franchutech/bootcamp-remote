def dividir_lista(numeros):
    resultados = []
    for n in numeros:
        if n == 0:
            resultados.append("No se puede dividir entre 0")
        else:
            resultado = 100 / n
            resultados.append(resultado)
    return resultados

def main():
    numeros = [10, 5, 0, 2]   # <- la lista contiene un cero
    print("Números:", numeros)

    resultados = dividir_lista(numeros)
    print("Resultados:", resultados)

if __name__ == "__main__":
    main()

