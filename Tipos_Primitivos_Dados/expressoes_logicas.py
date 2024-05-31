# EXPRESSÕES LÓGICAS
# Autor: Prof. Guilherme Cardoso Agostinetti

A = 2
B = 7
C = 3.5
L = False


A1 = 2 < 5 and 15/3 == 5
print(A1)

B1 = 2 < 5 or 15/3 == 5
print(B1)

C1 = False or 20 // (18/3) != (21/3)//2
print(C1)

D1 = not True or 3**2/3 < 15-35 % 7
print(D1)

E1 = not ((5 != 10/2) or True and 2 - 5 > 5 - 2 or True)
print(E1)

F1 = 2**4 != 4 + 2 or 2+3 * 5/4 % 5 < 0
print(F1)

A2 = B == A*C and (L or True)
print(A2)

B2 = B > A or B == A**A
print(B2)

C2 = L and B // A >= C or not (A <= C)
print(C2)

D2 = not L or True and (A+B)**0.5 >= C
print(D2)

E2 = B/A == C or B/A != C
print(E2)

F2 = L or B**A <= C * 10 + A*B
print(F2)
