#Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int (input("Digite um número"))
n2 = int (input("Digite outro número"))

resultado = n1+n2

print("O resultado da soma é: ", resultado)

print("O resultado da soma é: {}".format(resultado))

print("A soma entre {} e {} vale {}".format(n1,n2,resultado))