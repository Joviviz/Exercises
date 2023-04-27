lista1 = ["Felipe", "Gabriel", "Arthur"]
lista2 = [0, 1, 2]

#lista1 = lista2 // método alternativo

lista1.insert(-1, lista2)
'''for i in range(len(lista1)):
    lista1[i] = lista2[i]'''

print(lista1)