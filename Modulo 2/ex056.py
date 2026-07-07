# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idade_homem = 0
nome_velho = ""
tot_mulher_20 = 0

for p in range(1, 5):
    print("-------{}º PESSOA-------".format(p))
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    soma_idade += idade

    if sexo == "M" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo == "F" and idade < 20:
        tot_mulher_20 += 1

media_idade = soma_idade / 4
print("A média de idade do grupo é de {} anos.".format(media_idade))
print("O homem mais velho tem {} anos e se chama {}.".format(maior_idade_homem, nome_velho))
print("São {} mulheres com menos de 20 anos.".format(tot_mulher_20))