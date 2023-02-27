string = input("Digite uma palavra ou frase: ")

string_invertida = ""

for letra in string:
    string_invertida = letra + string_invertida

print("A string invertida é:", string_invertida)
