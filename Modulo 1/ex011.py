#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma áreas de 2m².

largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))

area = largura * altura

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²".format(largura, altura, area))
print("Para pintar essa parede, você precisa de {}l de tinta.".format(area / 2))