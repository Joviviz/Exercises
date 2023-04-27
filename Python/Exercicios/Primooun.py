import math

nmr = int(input("Coloque o número: "))
variavel = 0

for i in range (2, int(math.sqrt(nmr)+1)):
    if (nmr % i == 0):
        variavel += 1

if variavel == 0:
    print|("primo")
else:
    print("Não primo")