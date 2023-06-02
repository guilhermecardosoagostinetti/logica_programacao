## VALOR COMPRAS
# Autor: Guilherme Cardoso Agostinetti

#Entrada de Dados.
sexo = bool(input("Escreva True para Homem ou False para Mulher: "))
compras = float(input("Valor gasto: "))

if (sexo == True):
    valor_final = compras*0.95
    print("Valor Final: ", valor_final)
else: 
    valor_final = compras*0.87
    print("Valor Final: ", valor_final)


