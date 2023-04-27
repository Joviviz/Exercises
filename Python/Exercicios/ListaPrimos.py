import math

listaUser = [int(x) for x in input("Coloque os números na lista separados por espaço:\n").split()]
listaPrimo = []



variavel = 0

for i in range(0, len(listaUser)):
    print(listaUser[i])

    prime = True

    for x in range(2, int(math.sqrt(listaUser[i]) + 1)):
        if (listaUser[i] % x == 0):
            prime = False

    if prime:
        listaPrimo.append(listaUser[i])

print(listaPrimo)