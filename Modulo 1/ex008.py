#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros

metro = float(input("Digite a quantidade de metros a ser convertida: "))

cm = metro * 100
mili = metro * 1000

print("A quantidade de {}m equivale a {:.0f}cm e {:.0f}mm".format(metro, cm, mili))
