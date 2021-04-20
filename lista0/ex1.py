# 1 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

#Criando suas respectivas listas 
listpar = []
listimpar = []

#Pedindo os números e adicioando nas listas responsáveis
for i in range(10):
   x = int(input(f"Informe o {i+1}º número inteiro:"))

   if x % 2 == 0:
       listpar.append(x)

   else:
      listimpar.append(x)

#Ler lista
qtdpar = len(listpar)
qtdimpar = len(listimpar)

print(f"A quantidade de números pares é {qtdpar},{listpar} e a quantidade de números ímpares é {qtdimpar},{listimpar}.")
