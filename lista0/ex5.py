#Faça um programa que leia uma quantidade indeterminada de números positivos e 
#conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deverá terminar quando for lido um número negativo

list025 = []
list2650 = []
list5175 = []
list76100 = []

num = int(input("Informe um número inteiro:"))

while num < 0 or num > 100:
    num = int(input("Informe um número inteiro positivo menor que 100:"))

while num >= 0:
    if num in range(0,26):
        list025.append(num)    
    elif num in range(26,51):
        list2650.append(num)  
    elif num in range(51,76):
        list5175.append(num)
    elif num in range(76,101):
        list76100.append(num)
    print(f"\nO {list025} pertence ao intervalo [0-25].\nO {list2650} pertence ao intervalo [26-50].\nO {list5175} pertence ao intervalo [51-75].\nO {list76100} pertence ao intervalo [76-100].")
    num = int(input("\nInforme um número inteiro:"))
    while num < 0:
        num = int(input("\nInforme um número inteiro positivo menor que 100:"))


        
    









