## Estruturas Sequenciais: Quantidade de Latas de Tinta
## AUTOR: PROF. GUILHERME CARDOSO AGOSTINETTI
import math

# Entrada de Dados
r = float(input("RAIO: "))
h = float(input("ALTURA: "))
p = 3.14

# Processamento

AT = 2*p*r**2+2*p*r*h #Área Total de cilindro
Litros = AT/3 # Quantidade de Litros
Qtd = Litros/5 
Qtd = math.ceil(Qtd) # Quantidade de Latas Arredondadas
c = Qtd*50 # Custo

# Saída de Dados
print("A Quantidade de Latas Necessárias é: ", Qtd, ". Portanto nosso custo será de: R$ ", c )