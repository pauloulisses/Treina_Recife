# Criando Llistas em python

frutas = ["Maçã", "banana","laranja", "uva"]
numeros = [1, 2, 3, 4, 5]
misturado = [1, "maça", 3.14, True]


# Acessando elementos de uma lista
print(frutas[0]) # saída será "maçã"
print(numeros[2]) # saída será "3"
print(misturado[3]) # sáida será "True"

# A diconando novo elemento na lista
frutas.append("Pêra") #append serve para adicona um elemento a lista no final da mesma 
print(frutas)

 # Removendo um elemento da lista 
numeros.remove(3) #remove irá remover o número de da lista números
print(numeros)

#Removendo e obtendo o último elemento da lista 

ultimo_numero = numeros.pop() #pop irá imprimir o último elemento da lista número que será o número 5
print(ultimo_numero)

# Interando sobre uma lista 
for fruta in frutas: # aqui irá imprimir todos os elementos da lista frutas
    print(frutas)

# Comprimento de uma lista
    
    quantidade_frutas = len(frutas) # len = comprimento
    print(quantidade_frutas)