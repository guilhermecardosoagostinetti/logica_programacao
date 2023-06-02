## PREÇO VIAGEM
# Autor: Guilherme Cardoso Agostinetti

# ENTRADA DE DADOS

km = float(input("Km:"))

if (km>200):
    preco = 0.5*km
    print("A viagem custará: ",preco, "R$")
else:
    preco = 0.45*km
    print("A viagem custará: ",preco, "R$")



