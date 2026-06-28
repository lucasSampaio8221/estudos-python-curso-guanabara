#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

n = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(n))
print("Sò tem espaços?", n.isspace())
print("É um número? ", n.isnumeric())
print("É alfabético?", n.isalpha())
print("É alfanumérico?", n.isalnum())
print("Está em maiusculas?", n.isupper())
print("Está em minusculas?", n.islower())
print("Está capitalizada?", n.istitle())












