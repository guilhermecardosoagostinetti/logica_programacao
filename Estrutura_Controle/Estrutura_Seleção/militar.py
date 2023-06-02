## ALISTAMENTO
# Autor: Guilherme Cardoso Agostinetti

idade = int(input("IDADE: "))

if (idade >=18):
    sobra = idade - 18
    print("VOCÊ DEVE SE ALISTAR. JA PASSARAM:",sobra,"ANOS")
else:
    falta = 18-idade
    print("VOCÊ NÃO PODE SE ALISTAR. FALTA:", falta, "ANOS")

