# Autor: Guilherme Cardoso Agostinetti

a = float(input("Digite a medida do primeiro Lado:"))
b = float(input("Digite a medida do segundo Lado:"))
c = float(input("Digite a medida do terceiro Lado:"))

if (a<b+c and b<a+c and c<a+b):
  if (a==b and b==c):
    print("EQUILÁTERO")
  else:
    if (a==b or b==c):
      print("ISÓSCELES.")
    else:
      print("ESCALENO")
else: 
  print("Não forma um triângulo")