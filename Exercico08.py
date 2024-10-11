# Entrada das rendas do casal
renda1 = float(input("Digite a renda do cônjuge #1: "))
renda2 = float(input("Digite a renda do cônjuge #2 "))

# Calculo da renda conjuta
renda_conjunta = renda1 + renda2

#Cálculo da alíquota
if renda_conjunta <= 900:
    aliquota = 0
elif 900 < renda_conjunta <= 1500:
    aliquota = 10
elif 1500 < renda_conjunta <= 2500:
    aliquota = 15
else:
    aliquota = 25

# Calculo do imposto de renda líquida
imposto_renda = renda_conjunta * aliquota / 100
reda_liquida = renda_conjunta - imposto_renda

#Exibição dos resultados com F-string
print(f"RENDA CONJUNTA: R$ {renda_conjunta}")
print(f"ALÍQUOTA: {aliquota}%")
print((f"IMPOSTO DE RENDA: R$ {imposto_renda}"))
print(f"RENDA LÍQUIDA: R$ {reda_liquida}")
    
