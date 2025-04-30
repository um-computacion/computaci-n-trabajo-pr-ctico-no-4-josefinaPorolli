
# implementación de excepciones 
def excepciones(n):
    try:
        int(n)
    except ValueError:
        return "Error: El valor introducido no es un número entero."
    if int(n) < 0:
        raise ValueError("Error: El número debe ser mayor o igual a 0.")
        

# Se crean dos funciones para calcular la serie de Fibonacci. Se introduce la posición y se muestra el número correspondiente a esa posición.
def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)