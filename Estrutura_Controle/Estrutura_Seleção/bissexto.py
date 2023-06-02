## VERIFICAR SE ANO É BISSEXTO 
# ENTRADA DE DADOS

#IDÉIA: TODO ANO BISSEXTO É MULTIPLO DE 4

#Entrada de Dados
ano = int(input("ANO: "))

if(ano%4 == 0 ):
    print(ano, "é bissexto.")
else:
    print(ano, "não é bissexto.")