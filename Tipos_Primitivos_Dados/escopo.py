# Escopo de Variáveis

x = 10  # Variável Global ( apresenta o valor em todo código)


def oi():
    x = 5  # Variável local ( apresenta esse valor apenas dentro da função)
    print("O valor local de x é:", x)


print("O valor Global de x é:", x)
oi()
