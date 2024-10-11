# Extraindo partes de uma string
frase = "Python é incrível"
primeira_palavra = frase[0:6] # Aqui irá pegar do índice 0 até 5 pois o 6 não está incluso nesse intervalo
print(primeira_palavra)

# Substituindo partes de uma string
nova_frase = frase.replace("Python","javascript") # replace tem a função de substituir. Aqui será substituído a frase "Python é incrível" por "javascript é incrível"
print(nova_frase)
