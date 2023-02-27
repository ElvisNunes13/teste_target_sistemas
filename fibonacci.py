num = int(input("Digite um número: "))
a, b = 0, 1

while b < num:
    a, b = b, a + b
print(f"{a}, {b}")    

if b == num:
    print(f"O número {num} pertence à sequência de Fibonacci!")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci!")