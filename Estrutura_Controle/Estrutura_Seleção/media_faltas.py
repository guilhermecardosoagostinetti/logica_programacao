# Autor: Guilherme Cardoso Agostinetti

md = int(input("Digite a média do aluno:"))
falta = int(input("Digite a quantidade de falta:"))

if (md>=60):
  if (falta<=200):
    print("APROVADO")
  else:
    print("REPROVADO")
else:
  print("REPROVADO")