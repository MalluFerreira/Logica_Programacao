genero = str(input("Digite seu sexo: M/F ")).lower().strip()

if genero == "m":
    print("masculino")

elif genero == "f":
    print("feminino")

else:
    print("inválido")