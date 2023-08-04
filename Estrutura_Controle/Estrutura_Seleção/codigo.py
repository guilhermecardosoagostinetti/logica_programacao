## Estrutura de Seleção Múltipla 
# Algoritmo para Localizar Código 
#Autor: Guilherme Cardoso Agostinetti

codigo = int(input("DIGITE O CÓDIGO: "))

if codigo == 1:
  print("SUL")
elif codigo == 2:
  print("NORTE")
elif codigo == 3:
  print("LESTE")
elif codigo == 4:
  print("OESTE")
elif codigo == 5 or codigo ==6:
  print("NORDESTE")
elif codigo ==7 or codigo ==8 or codigo ==9:
  print("SUDESTE")
elif codigo>=10 and codigo <=20:
  print("CENTRO-OESTE")
elif codigo>=25 and codigo<=30:
  print("NOROESTE")
else:
  print("IMPORTADO")