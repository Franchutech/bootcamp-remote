# Kata 3

contador = 0

for numero in range (1, 51):
    if numero %5 == 0:
        continue
    if numero %11 ==0:
        break
    print(numero)
    contador +=1
print ("Números impresos:", contador)