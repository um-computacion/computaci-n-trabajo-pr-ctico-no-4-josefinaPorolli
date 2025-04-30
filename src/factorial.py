# Creamos las excepciones para las cuales el código deberá mostrar un mensaje de error
def excepciones(n):
    try: # el número es entero positivo o cero
        n = int(n)
    except ValueError:
        raise ValueError("El valor debe ser un número entero.") # el número no es válido
    if n < 0:
        raise ValueError("El número debe ser mayor o igual a 0.") # el número es negativo
    
################### FUNCIONES ###################

def factorial_iterativo(n):
    # llamamos a la función excepciones para validar el número
    excepciones(n)

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    # llamamos a la función excepciones para validar el número
    excepciones(n)

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
