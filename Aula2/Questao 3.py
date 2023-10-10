cor = input("Escolha uma cor entre: verde, vermelho e amarelo: ").lower().strip()

match cor:
    case "vermelho":
        print("Pare")
    case "verde":
        print("Siga em frente")
    case "amarelo":
        print("Atenção!")
    case _:
        print("Cor inválida")






# if cor == "verde":
#     print("acelerar")

# elif cor == "vermelho":
#     print("parar")
# elif cor == "amarelo":
#     print("atenção")

# else:
#     print("cor inválida")
