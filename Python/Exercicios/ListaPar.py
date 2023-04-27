import math

listaUser = []
listaPar = []

variavel = 0

while True:
    num = int(input("Coloque um número na lista: "))
    listaUser.append(num)

    print(f"{listaUser} é a composição da lista atual")

    cond = input("Deseja adicionar mais números (s/n)? ")

    if cond == "s" or cond == "S":
        continue
    else:
        for i in range(0, len(listaUser)):
            if (listaUser[i] % 2 == 0):
                listaPar.append(listaUser[i])
                print(f"O número {listaUser[i]} foi adicionado na lista par")
        print()

        print(f"{listaPar} é a nova lista formada por números pares")
        break