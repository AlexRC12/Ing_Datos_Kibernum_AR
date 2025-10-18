#Importar todas las funciones del módulo
from operaciones import *


#Pide al usuario ingresar 2 números

numero1 = int(input("Ingresa el primer número entero:"))
numero2 = int(input("Ingresa el segundo número entero:"))

#Llama a las funciones

#Sumar
ejemplo_suma = sumar(numero1,numero2)
print("El valor de la suma es",ejemplo_suma)

#Restar
ejemplo_restar = restar(numero1,numero2)
print("El valor de la resta es",ejemplo_restar)

#Multiplicación
ejemplo_multiplicar = multiplicar(numero1,numero2)
print("El valor de la multiplicación es", ejemplo_multiplicar)

#Potencia
ejemplo_potencia = potencia(numero1,numero2)
print("El valor de la potencia es", ejemplo_potencia)

#Factorial
ejemplo_factorial = factorial(numero1)
print("El valor de factorial es", ejemplo_factorial)


#Mostrar_info
ejemplo_info = mostrar_info(nombre="Alex", curso="Fundamentos de Ingeniería de Datos", edad = 30)
