## DISTÂNCIA DE DOIS PONTOS
## AUTOR: PROF. GUILHERME CARDOSO AGOSTINETTI

# ENTRADA DE DADOS
P1x = float(input("x ponto 1: "))
P1y = float(input("y ponto 1: "))
P2x = float(input("x ponto 2: "))
P2y = float(input("y ponto 2: "))

# PROCESSAMENTO 

d = ((P2x-P1x)**2+(P2y-P1y)**2)**0.5

# SAÍDA DE DADOS
print("A Distância entre os dois pontos é:  ", d )