# Verificação de aprovação de um aluno por nota e frequencia

nota = float(input("Digite a nota do aluno: "))
frequencia = float(input("Digite a frequência do aluno em porcentagem: "))

'''
Verifica se a nota é maior ou igaul a 7
e se a frequência é maior ou igual a 70%
'''

if nota >= 7 and frequencia >= 70: # Aqui que dizer se nota for >= a 7 and ="E" frequencia >=70
    print("Aprovado")
else:
    print("Reprovado")