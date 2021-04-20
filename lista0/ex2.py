#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Informe um numero:"))

if (num % 2 == 1) or (num == 400):
    print("O número é primo!")

else:
    print("O número não é primo!")