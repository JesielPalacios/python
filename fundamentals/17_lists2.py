# Listas
# Lista = [1, 2, 3, 4, 5]

# Puede ser modificada
# Cada elemento esta separado por una coma
# Puede contener todo tipo de datos
# Metodos para listas
# Lista.metodo(indice, elemento) o

# Lista.metodo(elemento)

# Metodos importantes
# .count(elemento) cuenta cuantas veces un elemento esta en una lista

# .extend(lista) permite extender una lista agregándole los elementos de otra lista

# .pop() elimina y retorna el ultimo elemento de la lista

# .reverse() reversa el orden de la lista

# .sort() ordena la lista de manera ascendente o descendente

# Actualizar un valor

# Lista = [1, 2, 3, 4, 5]

# Lista[0] = -8

# Lista = [-8, 2, 3, 4, 5], resultado de la lista luego de actualizar el valor

# Agregar un elemento

# Lista.append(indice, elemento) o

# Lista.append(elemento) en este caso el nuevo elemento se agrega al final de la lista

# Eliminar un elemento

# Lista.remove(indice, elemento)


#
#
#


""" List """
numbers = [28, 12, 73, 4]
print("numbers =", numbers)
print(type(numbers))

tasks = ["washes the dishes", "do my homework", "watch platzi courses"]
print("tasks =", tasks)
print(type(tasks))

things = [39, "theme", False, 48, "fire"]
print("things =", things)
print(type(things))

# indexing slicing
print("-" * 35)
numbers = [-3, 79, 3.18, -0.3, 0]
print("numbers =", numbers)
print("numbers[2] =>", numbers[2])
print("numbers[-1] =>", numbers[-1])
print("numbers[:3] =>", numbers[:3])
print("numbers[2:] =>", numbers[2:])
print("numbers[1:4] =>", numbers[1:4])

# multi
print("-" * 35)
words = ["plates", "homework", "platzi", "python", "history"]
print("words =", words)
print('words[0] = "cat"')
words[0] = "cat"
print("words =", words)

# in
print('"cat" in words =>', "cat" in words)
print('"plates" in words =>', "plates" in words)


#
#
#


# La notación para lista es una secuencia de valores encerrados entre corchetes y separados por comas. Por ejemplo, si representamos a los alumnos mediante su número de padrón, se puede tener una lista de inscritos en la materia como la siguiente: i[78455, 89211, 66540, 45750]. Al abrirse la inscripción, antes de que hubiera inscritos, la lista de inscritos se representará por una lista vacía: [].
# Longitud de la lista. Elementos y segmentos de listas

# Como a las secuencias ya vistas, a las listas también se les puede aplicar la función len() para conocer su longitud.

# # Para acceder a los distintos elementos de la lista se utilizará la misma notación de índices de cadenas y tuplas, con valores que van de 0 a la longitud de la lista −1.

# >> xs = [78455, 89211, 66540, 45750]
# >> > xs[0]
# 78455
# >> > len(xs)
# 4
# >> > xs[4]
# Traceback(most recent call last):
#    File "<stdin>", line 1, in <module >
# IndexError: list index out of range
# >> > xs[3]
# 45750


#
#
#


# Cómo mutar listas

# Dijimos antes que las listas son secuencias mutables. Para lograr la mutabilidad Python provee operaciones que nos permiten cambiarle valores, agregarle valores y quitarle valores.

# Para cambiar una componente de una lista, se selecciona la componente mediante su índice y se le asigna el nuevo valor:

# >> > xs[1] = 79211
# >> > xs
# [78455, 79211, 66540, 45750]


#
#
#


# Listas, probablemente el primer eslabón importante en Python.

# List is a collection which is ordered and changeable. Allows duplicate members.


#
#
#


# LISTAS:

# Acceso a la lista desde el índice de inicio hasta el índice de fin. Ejemplo:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[1])  # salida:2
print(lista[1:6])  # Devuelve: [2, 3, 4, 5, 6]
print(lista[-3])  # salida : [7]
# La lista NO es inmutable, es decir, permite modificar los datos que han sido creados. Ejemplo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista[2] = 3.8  # Ahora 3.8 es el tercer elemento
print(lista)
# Permiten agregar nuevos valores. Ejemplo:
lista.append('Nuevo Dato')
