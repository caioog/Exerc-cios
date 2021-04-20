#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.


num = int(input("Informe um número primo:"))

while not (num % 2 == 1 or num == 400):
    print("O número digitado não é primo.")
    num = int(input("Informe um número primo:"))

listprimo = []

for i in range(num + 1):
    if (i % 2 == 1) or (i == 400):
       listprimo.append(i)

print(f"Os números primos são: {listprimo}.")
