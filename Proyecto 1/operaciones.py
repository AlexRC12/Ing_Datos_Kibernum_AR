"""
Este archivo "operaciones.py" contendrá las funciones matemáticas de sumar,
restar, multiplicar, mostrar_info, potencia, recursiva.

"""

def sumar(a,b):
    """
    La función sumar toma 2 valores dados por el usuario y devuelve la suma como resultado
    """
    return a+b

def restar(a,b=5):
    """
    La función resta toma 2 valores dados por el usuario y devuelve la resta como resultado, si no se 
    ingresa el segundo valor "b" este toma como defecto el valor 5
    """
    return a-b

def multiplicar(*numeros):
    """
    La función toma una cantidad variable de números y devuelve la multiplicación de ellos.
    Toma todos los valores y a través del proceso iterativo for los multiplica, la variable "resultado"
    almacena cada iteración.
    
    """
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

def mostrar_info(**datos):
    """
    Esta función nuestra la información ingresada como argumentos de tipo clave-valor,
    para el ejemplo concreto se pasa nombre, edad y curso
    """
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

def potencia(base, exponente):
    """
    Esta función calcula la potencia de una base elevada a su exponente usando para el cálculo
    una función lambda
    """
    resultado = lambda base, exponente: base**exponente
    return resultado(base, exponente)


def factorial(n):
    """
    La función calcula el factorial de un número de forma recursiva,
    cuando el valor ingresado es 0 o 1 devuelve el valor 1, si el valor ingresado es diferente de 0 o 1
    entonces ingresa al else y calcula el factorial.
    """

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
