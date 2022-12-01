# Indexing and slicing

text = "Ella sabe Python"
print(text[0])
print(text[1])
# print(text[999])
size = len(text)
print('size => ', size)
print(text[size - 1])
print(text[-1])

# slicing

print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:-1])
print(text[5:])
print(text[:])
print(text[10:16:1])  # ir desde la posición 10 hasta el final de a 1 salto
print(text[10:16:2]) # ir desde la posición 10 hasta el final de a 2 saltos
print(text[::2]) # ir del inicio al final y saltar de a 2

# Para poder tener las palabras al reves
text = "Ella sabe python"
print(text[::-1])

# para escoger alguna parte del string y voltearla:
print(text[16:9:-1])


#
#
#
text = "Ella sabe Python"
print(text[0])
print(text[1])

print(text[999])  # Si le das una posicion que no existe, da error

size = len(text)

print('size ', size)
print(text[size])  # Como empieza en 0, no llega a la última

print(text[size - 1])

print(text[-1])

# Slicing
print(text[0:5])  # Obtener del índice 0 al índice 4 excluyendo el índice 5

print(text[:10])  # Obtendrá siempre desde 0 si no se específica

# Obtendrá siempre hasta el final de la cadena desde donde específicaste el inicio
print(text[5:])

# Sí se agrega un salto, regresa del inicio al final por los saltos
print(text[10:16:2])

print(text[::2])  # Inicio al final en saltos de 2
