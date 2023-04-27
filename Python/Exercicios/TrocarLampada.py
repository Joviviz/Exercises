queimada = input("A lâmpada está queimada? (S/N): ")

if queimada == "S" or queimada == "s":
    escada = input("Há escada? (S/N): ")

    if escada == "S" or escada ==  "s":
        lampadanova = input("Há uma lâmpada substituta? (S/N): ")

        if lampadanova == "S" or lampadanova == "s":
            print("\nPegar a escada e a lâmpada nova \nSubir degraus até conseguir encostar na lâmpada")
            print("Girar a lâmpada no sentido de remover até removê-la \nColocar a lâmpada nova girando no sentido contrário de remover ")
            print("Descer a escada.\nFim de Programa.")

        elif lampadanova == "N" or lampadanova == "n":
            print("Não há lâmpada reserva, compre uma. Fim de programa.")
        else:
            print("Opção inválida")

    elif escada == "N" or escada == "n":
        print("Não há escada, compre uma. Fim de programa.")
    else:
        print("Opção inválida")


elif queimada == "N" or queimada == "n":
    print("A lâmpada não esta queimada. Fim de programa.")
else:
    print("Opção inválida")