## BHASKARA
## AUTOR: PROF. GUILHERME CARDOSO AGOSTINETTI

# ENTRADA DE DADOS
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
# PROCESSAMENTO 

delta = B**2-4*A*C

x1 = (-B+delta**0.5)/(2*A)
x2 = (-B-delta**0.5)/(2*A)

# SAÍDA DE DADOS
print("As raízes da equação são: ", "x1", x1, "e x2= ", x2)