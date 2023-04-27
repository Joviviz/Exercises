dict_cadastro_candidatos = []

def cadastrar():
    nome_candidato = input('Digite o nome do candidato: ')
    nmr_candidato =  input('Digite o número do candidato: ')
#def votar():
#def resultado():


while True:
    print('1 - Cadastrar candidato\n2 - Votar\n3 - Resultado\n4 - Sair')
    option = int(input('Digite a opção desejada: '))
    if option == 1:
        cadastrar()
    if option == 2:
        cadastrar()
    if option == 3:
        cadastrar()
    else:
        print('Sair')
        break
