lista = []
while True:
    num = int(input("Coloque um número na lista: "))
    lista.append(num)

    print(f"{lista} é a composição da lista atual")

    cond = input("Deseja adicionar mais números (s/n)? ")

    if cond == "s" or cond == "S":
        continue
    else:
        print("A média dos números da lista é:", (sum(lista) / len(lista)))
        break