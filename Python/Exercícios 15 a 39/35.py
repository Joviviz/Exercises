lista = [2, 1, 60, 12, 34, 3, 5]

for i in range(len(lista)): #Passa por todos os index

    for j in range(0, len(lista) -i -1): #

        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)

if __name__ == "__main__":
    print("it worked")