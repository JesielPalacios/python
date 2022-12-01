# Playgrounds: Imprime el formato adecuado
# En este desafío vas a tener un código base el cual usa la función input para solicitar tu nombre, apellido y edad, tu reto es crear un formato usando un string que como resultado realice un print en la Terminal con el siguiente mensaje:

# Hola mi nombre es Nicolas Molina, tengo 29 años y en 10 años tendré 39 años

# Fíjate que debes hacer un cálculo para la edad y calcular cuál será la edad en 10 años según el valor ingresado.

# Ejemplo 1:

# Input:
# ¿Cuál es tu nombre? = > Juan
# ¿Cuál es tu apellido? = > Perez
# ¿Cuál es tu edad? = > 10

# Output:
# Hola mi nombre es Juan Perez, tengo 10 años y en 10 años tendré 20 años

# Ejemplo 2:

# Input:
# ¿Cuál es tu nombre? = > Andrea
# ¿Cuál es tu apellido? = > Casas
# ¿Cuál es tu edad? = > 22

# Output:
# Hola mi nombre es Andrea Casas, tengo 22 años y en

name = input('¿Cuál es tu nombre? => ')
print(name)
last_name = input('¿Cuál es tu apellido? => ')
print(last_name)
age = input('¿Cuál es tu edad? => ')
print(age)


template = f"Hola mi nombre es {name} {last_name}, tengo {age} años y en 10 años tendré {age+10} años"
print(template)
