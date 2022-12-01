# Esta fue mi solución. Plantee usar números en lugar de las palabras para jugar.
# (La función o_pc elige un número aleatorio entre el 0 y 2)

import random

# Interfaz
print('Juego Piedra, Papel y tijera')
print('                      ')
print('0- Piedra             ')
print('1- Papel              ')
print('2- Tijera             ')
print('                      ')

# Eleccion del jugador
o_user = int(input('Elegir una opcion (0 - 1 - 2):'))

# Elecion aleatoria de la pc
o_pc = random.randrange(2)

# Logica
if o_user == o_pc:
    print('Empate!')
elif (o_user == 0 and o_pc == 1) or (o_user == 1 and o_pc == 2) or (o_user == 2 and o_pc == 0):
    print('Perdiste! :(')
else:
    print('Ganaste! :)')

# (Faltaría validar el input para controlar que se ingresen únicamente los números indicados)

# Esta sería la opción final con las validaciones y un mensaje para saber qué opción elegiste y cuál eligió la computadora
import random

# Interfaz
print('Juego Piedra, Papel y tijera')
print('                      ')
print('0- Piedra             ')
print('1- Papel              ')
print('2- Tijera             ')
print('                      ')

# Eleccion del jugador
o_user = int(input('Elegir una opcion (0 - 1 - 2):'))
while (o_user!=0 and o_user!=1 and o_user!=2):
    print('Ingresar una de las opciones indicadas!')
    o_user = int(input('Elegir una opcion (0 - 1 - 2):'))

# Elecion aleatoria de la pc
o_pc = random.randrange(2)

op = ['Pierda','Papel','Tijera']

#Logica
if o_user == o_pc:
    print('Empate! <Ambos eligieron',op[o_user],'>')
elif (o_user == 0 and o_pc == 1) or (o_user == 1 and o_pc == 2) or (o_user == 2 and o_pc == 0):
    print('Perdiste! :(  <',op[o_pc],' le gana a',op[o_user],'>')
else:
    print('Ganaste! :) <',op[o_user],' le gana a',op[o_pc],'>') 