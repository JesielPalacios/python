# En este desafío vas a recibir un número como parámetro y tu reto es identificar si ese número es par o impar y según eso retornar un mensaje de "Es par" en el caso de los pares y "Es impar" en el caso de los impares.

# Para solucionarlo vas a encontrar una función llamada is_even_or_odd que recibe un parámetro de entrada:

# number: Un número que puede ser positivo o negativo
# Dentro del cuerpo de la función is_even_or_odd debes escribir tu solución.

# Ejemplo 1:

# Input: 2
# Output: "Es par"

# Ejemplo 2:

# Input: 3
# Output: "Es impar"

number = int(input('Digita un número => '))
print(number)

# Escribe tu solución 👇
if number % 2 == 0:
    print("el numero “, number, " es par”)

else:
    print("el numero “, number, " es impar”)
