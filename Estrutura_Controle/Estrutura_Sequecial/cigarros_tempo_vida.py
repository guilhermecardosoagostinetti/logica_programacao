## REDUÇÃO DO TEMPO DE VIDA DE UM FUMANTE
## AUTOR: PROF. GUILHERME CARDOSO AGOSTINETTI

# ENTRADA DE DADOS
cigarros_dia= int(input("CIGARROS FUMADOS POR DIA: "))
anos_fumando = float(input("ANOS FUMANDO: "))


# PROCESSAMENTO 
cigarros_fumados = cigarros_dia*(anos_fumando *365)
minutos_perdidos = cigarros_fumados*10
dias_perdidos = minutos_perdidos/1440

# SAÍDA DE DADOS
print("Dias Perdidos: ", dias_perdidos)