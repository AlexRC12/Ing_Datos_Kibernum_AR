###Bloque 1: Listas y Listas anidadas

#Crea una lista con al menos 5 elementos de diferentes tipos
print("***Bloque 1: Listas y Listas anidadas***\n")
lista = [42, "hola", 3.14, True, ["holi", 2, 7]]
#Agrega y elimina un elemento
lista.append("nuevo")
lista.remove(3.14)
#Accede al primer y último elemento 
print("Primer elemento:", lista[0])
print("Último elemento:", lista[-1])
#Crea una lista anidada matriz 3x3 e imprime su segunda fila
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Segunda fila:", matriz[1])


###Bloque 2: Diccionarios y Diccionarios Anidados
print("\n***Bloque 2: Diccionarios y Diccionarios anidadas***\n")
#Crea un diccionario con datos de un estudiante(nombre, edad, carrera)
estudiante = {
    "nombre": "Alex",
    "edad": 30,
    "carrera": "Fundamentos de Ingeniería de Datos"
}
#Agrega una clave notas con una lista de 3 notas
estudiante["notas"] = [5.5, 6.0, 4.8]
#Imprime la segunda nota y la carrera del estudiante
print("Segunda nota:", estudiante["notas"][1])
print("Carrera:", estudiante["carrera"])

###Bloque 3: Tuplas y Empaquetado/Desempaqueta
print("\n***Bloque 3: Tuplas y Empaquetado/Desempaqueta***\n")
#Crea una tupla con datos de un libro (título, autor, año).
libro = ("Fundamentos de Python", "Alex Riquelme", 2025)
#Desempaqueta la tupla en tres variables.
titulo, autor, anio = libro
#Imprime una frase usando los datos desempaquetados
print(f"El maravilloso libro '{titulo}' fue escrito por {autor} en el año {anio}.")


###Bloque 4 – Sets y Operaciones de Conjunto
print("\n***Bloque4: Sets y Operaciones de Conjunto***\n")
#Crea dos conjuntos con elementos duplicados y elimina los duplicados.
set1 = {1, 2, 2, 3, 4}
set2 = {3, 4, 4, 5, 6}

print("Conjunto 1:", set1)
print("Conjunto 2:", set2)

#Realiza e imprime la intersección y la unión de ambos conjuntos.
print("Intersección:", set1 & set2)
print("Unión:", set1 | set2)

###Bloque 5: Iteraciones
print("\n***Bloque 5: Iteraciones***\n")

#Itera una lista de nombres usando for e imprime un saludo para cada uno.
nombres = ["Alex", "Patricio", "Pedro"]
for nombre in nombres:
    print(f"Hola, {nombre}")

#Usa range para imprimir los números del 1 al 10.
for i in range(1,10):
    print(i)

#Itera un diccionario imprimiendo las claves y los valores.
mi_diccionario = {"a": 1, "b": 2, "c": 3}
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

#Usa un ciclo while para sumar los números del 1 al 5.
i = 1
suma = 0
while i <= 5:
    suma += i
    i += 1
print("Resultado de la suma:", suma)