#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

núm = (int(input("Dígite um número: ")),
       int(input("Dígite outro número: ")),
       int(input("Dígite mais um número: ")),
       int(input("Dígite o último número: ")))
print(f"Você digitou os valores {núm}")
print(f"O valor 9 apareceu {núm.count(9)} vez.")
if 3 in núm:
    print(f"O valor 3 apareceu na {núm.index(3)+1}º posição")
else:
    print("O valor 3 não apareceu em nenhuma posição.")
print("Os valores pares digitados foram: ", end="")
for n in núm:
    if n % 2 == 0:
        print(f"{n} ", end="")




