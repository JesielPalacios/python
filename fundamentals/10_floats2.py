# La razon de porque la division no es exacta es:

# Python utiliza la IEEE 754-2008 para la representación de números de punto flotante, que es la norma internacional para la representación y el cálculo de números de punto flotante. Sin embargo, esta norma tiene sus limitaciones y, por lo tanto, python también tiene limitaciones en la representación y el cálculo de números de punto flotante.

# Una de las limitaciones principales de la IEEE 754-2008 es que sólo permite representar un número finito de dígitos decimales. Esto significa que, en algunos casos, los números de punto flotante no se pueden representar de forma exacta y se producen errores de redondeo o truncamiento. Estos errores pueden ser pequeños y pueden no tener un impacto significativo en el cálculo, pero en algunos casos pueden ser muy grandes y afectar significativamente al resultado final.

# Hola, les comparto como evalue otro valores booleanos prácticando un poco con funciones como:
# isalnum(), isinstance(), isnumeric()

# Evaluate True values
print("\n*****True values*****")
print(10 <= 16)
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = '15'

print(bool(x))
print(bool(y))

# Evaluate False values
print("\n*****False values*****")
print(10 >= 16)
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Evaluate a booleans with functions
print("\nEvaluate booleanda with isinstance() functions")
print(isinstance(14, str))

print("\nEvaluate booleanda with isalnum() functions")
x = "ghg5448"
print(x.isalnum())

print("\nEvaluate booleanda with isnumeric() functions")
x = "gghg5874"
print(x.isnumeric())
