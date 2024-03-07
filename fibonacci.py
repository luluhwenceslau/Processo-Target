def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

n = int(input("Digite um número: "))

if fibonacci(n):
    print(f"O numero {n} pertence a Sequencia Fibonacci.")
else:
    print(f"O numero {n} não pertence a Sequencia Fibonacci.")