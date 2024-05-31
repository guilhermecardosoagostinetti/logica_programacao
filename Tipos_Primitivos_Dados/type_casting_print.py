# Type

meu_nome = "Guilherme"
minha_idade = 24
meu_peso = 75.5
maior_idade = True

print(type(meu_nome))
print(type(minha_idade))
print(type(meu_peso))
print(type(maior_idade))

# Casting

# Pelo python ser dinamicamente tipado, o proproi python convertes 
# seus dados pelo interpretador.

# ------------------ Para Int---------------------------
x = 2
y = 2.8
z = '2'

print(x, y, z)
print("A variável x é do tip:", type(x))
print("A variável y é do tip:", type(y))
print("A variável z é do tip:", type(z))

# Convertendo com o casting para int

x = int(x)
y = int(y)
z = int(z)

print(x, y, z)
print("A variável x é do tip:", type(x))
print("A variável y é do tip:", type(y))
print("A variável z é do tip:", type(z))
# perceba que agora só temos variáveis inteiras

# ------------------ Para float---------------------------

a = 2.3
b = 2
c = '2.3'

print(a, b, c)
print("A variável a é do tip:", type(a))
print("A variável b é do tip:", type(b))
print("A variável c é do tip:", type(c))

a = float(a)
b = float(b)
c = float(c)

print(a, b, c)
print("A variável a é do tip:", type(a))
print("A variável b é do tip:", type(b))
print("A variável c é do tip:", type(c))

# ------------------ Para String---------------------------

t = 'oi'
s = 1
r = 2.4

print(t, s, r)
print("A variável t é do tip:", type(t))
print("A variável s é do tip:", type(s))
print("A variável r é do tip:", type(r))

t = str(t)
s = str(s)
r = str(r)

print(t, s, r)
print("A variável t é do tip:", type(t))
print("A variável s é do tip:", type(s))
print("A variável r é do tip:", type(r))
