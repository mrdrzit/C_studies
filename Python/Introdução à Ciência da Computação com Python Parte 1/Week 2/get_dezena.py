num = input("Digite um número inteiro: ")
num = int(num)

dezena = (num//10) - (num//100)*10
print("O dígito das dezenas é",dezena)