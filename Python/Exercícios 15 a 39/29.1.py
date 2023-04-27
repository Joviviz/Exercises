caixa = [1, 2, 3, 4, 5, 6, 7]
print(caixa)

substituto = int(input("Substitua o número do meio da lista por um inteiro: "))

caixa[int(len(caixa)/2)] = substituto #Pega o tamanho da lista e o divide por 2 para encontrar o index do meio
print(caixa)                          #É necessário transformar esse valor em int, pois os index não podem ser float

