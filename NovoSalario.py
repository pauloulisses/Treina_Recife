# Calculo do novo salário

salario = float(input("Digite o salário atual: "))

if salario  < 500:
    novo_salario = 1.20 * salario
elif salario <= 1000:
        novo_salario = 1.10 * salario
else:
        novo_salario = 1.5 * salario

print("O novo salário é", novo_salario)            
                    