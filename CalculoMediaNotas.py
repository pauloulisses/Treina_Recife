# Cálculo da média de várias notas

notas = [8, 7, 9 , 10, 6]

soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)

print("A média das notas é:", media)