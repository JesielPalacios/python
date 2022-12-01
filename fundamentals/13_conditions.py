# Conditions

# https://www.w3schools.com/python/python_conditions.asp

if True:
    print('deberÃ­a ejecutarse')

if False:
    print('nunca se ejecuta')

'''
pet = input('Â¿CuÃ¡l es tu mascota favorita? ')

if pet == 'perro':
  print('genial tienes buen gusto')
elif pet == 'gato':
  print('espero tengas suerte')
elif pet == 'pez':
  print('eres lo maximo')
else:
  print('no tienes ninguna mascota interesante')


stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('el stock es incorrecto')

'''

number = int(input('Ingrese un numero => '))
result = number % 2
if (result == 0):
    print('Es par')
else:
    print('Es impar')

# https://aprendeconalf.es/docencia/python/ejercicios/condicionales/


# Condicionales anidados en Python(elif)

# Cuando se anidan varios niveles de enunciados if/else, puede ser difícil determinar cuáles expresiones lógicas deben ser verdaderas(o falsas) con la finalidad de ejecutar cada conjunto de enunciados. La función elif le permite comprobar criterios múltiples mientras se mantiene el código fácil de leer.

a = int(input('¿Cuantos años tiene tu computador?: '))
if a >= 0 and a <= 2:
    print('Tu computador es nuevo')
    print('Puedes continuar con tu PC')
else:
    print('Tu computador es Viejo')
    print('Considera comprar uno nuevo')

print('-'*20)
