import math as lara

# Equação genérica de segundo grau:
# y = ax^2 + bx + c

# Lembre que a fórmula de bháskara é:
# x = (-b ± √(b² - 4ac)) / (2a)

a = int(input("Digite o número para a constante A: "))
b = int(input("Digite o número para a constante B: "))
c = int(input("Digite o número para a constante C: "))

delta = b**2 - 4 * a * c
if delta < 0:
    print("Essa equação não possui raizes reais")
    exit()

delta = lara.sqrt(delta)
x1 = (-b + delta) / (2 * a)
x2 = (-b - delta) / (2 * a)

print("A raiz x1 = ", x1, "A raiz x2 = ", x2)


if delta == 0:
    print("Essa equação possui 1 raiz real, ", x1)

if delta > 0:
    print("Essa equação possui 2 raizes reais: ")
    print("Raiz 1 = ", x1)
    print("Raiz 2 = ", x2)
