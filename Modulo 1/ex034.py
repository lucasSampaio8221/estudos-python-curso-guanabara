#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("QUal é o salário do funcionário? "))



if salario <= 1250:
    menor = salario + (salario * 15 / 100)
    print("Com o aumento de 15% o seu salário agora será de R${:.2f}".format(menor))
else:
    maior = salario + (salario * 10 / 100)
    print("Com o aumento de 10% o seu salário agora será de R${:.2f}".format(maior))


