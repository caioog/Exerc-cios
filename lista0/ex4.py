#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será 
#digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, 
#o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

numt = int(input("Montar tabuada de:"))
numc = int(input("Começar pelo:"))
numtm = int(input("Terminar pelo:"))

for i in range(numc, numtm + 1):
    conta = numt * i
    print(f"{numt} X {i} = {conta}")