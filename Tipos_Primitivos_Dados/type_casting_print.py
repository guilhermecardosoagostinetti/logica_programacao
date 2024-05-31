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

# Pelo python ser dinamicamente tipado, o proproi python convertes seus dados pelo interpretador.

# ------------------ Para Int---------------------------
x = 2
y = 2.8
z = '2'

print(x, y, z)
print(type(x), type(y), type(z))

# Convertendo com o casting para int

x = int(x)
y = int(y)
z = int(z)

print(x, y, z)
print(type(x), type(y), type(z))

# perceba que agora só temos variáveis inteiras

# ------------------ Para float---------------------------

a = 2.3
b = 2
c = '2.3'

print(a, b, c)
print(type(a), type(b), type(c))

a = float(a)
b = float(b)
c = float(c)

print(a, b, c)
print(type(a), type(b), type(c))

