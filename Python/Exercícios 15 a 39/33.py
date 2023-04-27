lista = [1, 2, 2, 2, 1, 1, 1]
print(lista)

soma = 0
total = 0

for index in lista: #Para encontrar o total de index sem usar len()
    total += 1

for i in range(total):
    soma += lista[i] #Soma dos valores dos index
print(soma)