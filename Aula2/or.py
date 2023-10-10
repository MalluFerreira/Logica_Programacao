alternativa = str(input("Você deseja sair? S/N ")).lower().strip()

if alternativa == "s" or alternativa == "n":
    print("Operação válida")
    if alternativa == "s":
        print("Tchau")
    else:
        print("Continue usando o programa!")

else:
    print("Operação inválida")
    


