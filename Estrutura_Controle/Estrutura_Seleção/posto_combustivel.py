## POSTO DE COMBUSTÍVEL 
#AUTOR: Guilherme Cardoso Agostinetti

#Entradade de dados

litros = float(input("LITROS: "))
tipos = str(input("A - Alcool ou G - Gasolina: "))

if (tipos == 'A'):
    valor = litros*1.90
    print("O Valor é: ", valor)

if (tipos == 'G'):
    valor = litros*2.70
    print("O Valor é: ", valor)