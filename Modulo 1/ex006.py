# Crie um algoritmo que leia um número e mostre o seu dobro, o triplo e a raiz quadrada.
from time import process_time_ns

n = int(input("Digite um númeo: "))

print("O seu número é {}, o dobro dele é {}, o triplo é {} e a raiz quadrada é {:.2f}".format(n, n*2, n*3, n**(1/2)))