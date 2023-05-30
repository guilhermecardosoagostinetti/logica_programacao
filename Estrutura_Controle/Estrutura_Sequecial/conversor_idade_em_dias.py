## CONVERSOR DE IDADE PARA DIAS
## AUTOR: PROF. GUILHERME CARDOSO AGOSTINETTI

# ENTRADA DE DADOS
anos = int(input("Anos: "))
mes = int(input("Meses: "))
dias = int(input("Dias: "))

# PROCESSAMENTO 

total_dias = anos*365 + mes*30 + dias

# SAÍDA DE DADOS
print("VOCÊ JÁ VIVEU, APROXIMADAMENTE ",total_dias," DIAS")
