# Crie um programa que leia um número REAL qualquer pelo teclado e mostre na tela a sua porção INTEIRA.

from math import trunc

valor = float(input('Digite um valor: '))

print('O valor digitado foi {} e sua porção inteira é {}'.format(valor, trunc(valor)))

