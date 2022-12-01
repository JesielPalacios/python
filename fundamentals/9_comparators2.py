# Operadores de comparación

# Estos operadores devuelven tipos de datos <boole>

# ( > / < ) Mayor / Menor
# ( >= / <= ) Mayor o igual / Menor o igual
# ( == ) Igual
# ( != ) Diferente


# Ejemplos:

# ( 2 > 1 ) --> True
# ( 2 > 3 ) --> False
# (5 > 5 ) --> False
# (1 < 2) --> True
# ( 2 >= 1 ) --> True
# ( 2 >= 3 ) --> False
# (1 <= 2) --> True
# (5 >= 5 ) -> True
# (4 == 4) --> True
# (‘Apple’ == ‘Apple’) --> True
# (‘Apple’ == ‘apple’) --> False
# (4 == 4) --> False
# (‘Apple’ == ‘Apple’) --> False
# (‘Apple’ == ‘apple’) --> True

# Operadores de comparacion-----------------------------------
# son operaores de logica y regresan booleanos

a = 10
b = 3

print(f"igual: {a == b}")  # compara si las variables son iguales
print(f"diferente: {a != b}")  # compara si las variables son diferentes
print(f"mayor: {a > b}")  # compara si la variable a es mayor que la variable b
print(f"menor: {a < b}")  # compara si la variable a es menor que la variable b
# compara si la variable a es mayor o igual que la variable b
print(f"mayor o igual: {a >= b}")
# compara si la variable a es menor o igual que la variable b
print(f"menor o igual: {a <= b}")
# compara si las dos variables son verdaderas
print(f"and: {a > b and a == b}")
print(f"or: {a > b or a == b}")  # compara si una de las variables es verdadera
