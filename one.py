def pertence_fibonacci(num):
    if not isinstance(num, int):
        raise ValueError("Valor deve ser um inteiro")
    if num < 0:
        return False
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

# Exemplo de uso:
while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro.")
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")