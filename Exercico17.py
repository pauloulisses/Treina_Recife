# Função de verificação se número é primo ou não
def en_primo(numero):
    if numero <= 1: # Aqui está perguntando se o numero for primo
        return False # Retornará False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Entrada do número de casos de teste
n = int(input("Digite o número de casos de teste: "))

# Verifica se cada número é primo ou não
for _ in range(n): # esse _ é para dizer que a variavél I é inrrelevante
    x = int(input("Digite um número: "))
    if en_primo(x):
        print(f"{x} é primo")
    else:
        print(f"{x} não é primo")    

