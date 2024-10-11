bairro = input("Digite o código do bairro (S/I/T): ")
renda = float(input("Digite a renda da família: "))
consumo = float(input("Digite o consumo em reais: "))

if bairro == "S" or bairro == "T" or bairro == "I":
    if renda < 0 or consumo < 0:
        print("RENDA E CONSUMO NÃO PODEM SER NEGATIVOS")
else:
    if bairro == "S":
        if 50 <= renda <= 500:
            desconto = 50
        elif 500 < renda <= 1000:
            desconto = 25
        else:
            desconto = 0
    elif bairro == "I":
        if 240 <= renda <= 1000:
            desconto = 240
        elif 1000 < renda <= 5000:
            desconto = 120
        else:
            desconto = 0
    else:
        if 5000 < renda <= 10000:
            desconto = 720
        elif 10000 < renda <= 20000:
            desconto = 360
        else:
            desconto = 0

    valor_a_pagar = consumo - desconto

    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
