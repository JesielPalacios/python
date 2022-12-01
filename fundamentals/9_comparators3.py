# Operadores de comparación

# Otro conjunto de operadores son aquellos que se aplican a dos elementos comparándolos y devuelven un resultado booleano (un Verdadero o Falso, o, en lenguaje Python, True o False). Entre estos operadores nos encontramos con la igualdad ( == ), desigualdad ( != ), mayor que ( > ), menor que ( < ), mayor o igual que ( >= ) y menor o igual que ( <= ).

# Algunos ejemplos:

# Operadores de comparación

# Obsérvese que la igualdad se comprueba con dos signos de igualdad("==") pues, como ya hemos visto, un único signo de igualdad("=") está reservado para asignar un valor a una variable. La desigualdad se comprueba con el operador “!=”, no con “<>” como ocurre en otros lenguajes de programación.


#
#
#
""" comparison signs """
# mayor ">"
print("Mayor")
print("19 > 8:", 19 > 8)
print("8 > 19:", 8 > 19)
print("7 > 7:", 7 > 7)

# menor "<"
print("Menor")
print("42 < 23:", 42 < 23)
print("23 < 42:", 23 < 42)
print("12 < 12:", 12 < 12)

# mayor o igual ">="
print("Mayor o igual")
print("73 >= 32:", 73 >= 32)
print("32 >= 73:", 32 >= 73)
print(f"92 >= 92: {92 >= 92}")

# menor o igual "<="
print("Menor o igual")
print(f"15 <= 62: {15 <= 62}")
print(f"62 <= 15: {62 <= 15}")
print(f"47 <= 47: {47 <= 47}")

# igual
print("Igual")
print(f"38 == 102: {38 == 102}")
print(f"19 == 19: {19 == 19}")

# diferente
print("Diferente")
print(f"13 != 27: {13 != 27}")
print(f"64 != 64: {64 != 64}")

# Ejemplos
print("Comparando Strings")
print(f"Apple == Apple: {'Apple' == 'Apple'}")
print(f"Apple == apple: {'Apple' == 'apple'}")

print("Comparando string con numbers")
print(f"table == 7: {'project' == 7}")
print(f"4 == 4: {'4' == 4}")
