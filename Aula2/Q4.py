letra = str(input("Digite uma letra: ")).lower()

if len(letra) == 1:
    if letra in "aeiou":
        print("vogal")
    elif letra in "bcdfghjklmnpqrstvwxz":
        print("consoante") 
    else: 
        print("inválido")
else:
    print("digite apenas uma letra")

