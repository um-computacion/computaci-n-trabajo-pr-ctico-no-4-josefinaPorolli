def fibonacci_iterativo(n):
    sum = 0
    a = 1
    while a <= n:
        sum += a
        a += 1
    return sum