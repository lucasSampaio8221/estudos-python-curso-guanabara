'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''

idade = int(input("Digite sua idade: "))
if idade <= 9:
    print("O atleta é da classificação MIRIM.")
elif idade <= 14:
    print("O atleta é da classificação INFANTIL.")
elif idade <= 19:
    print("O atleta é da classificação JÚNIOR.")
elif idade <= 25:
    print("O atleta é da classificação SÊNIOR.")
else:
    print("O atleta é da classificação MASTER.")