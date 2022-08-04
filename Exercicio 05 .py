print("--- Inversor de palavras ---")
palavra = input("Digite uma palavra:")
caracteres = []
inverse = ''
for letra in palavra:
    caracteres.append(letra)
tam = len(caracteres) - 1
while tam >= 0:
    inverse += (caracteres[tam])
    tam -= 1
print("Palavra invertida: ")
print(inverse)