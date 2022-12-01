name = "Nicolas"
last_name = 'Molina Monroy'
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Nicolas"
print(quote)

quote2 = ' She said "Hello"  '
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)

# Homework
name = "Eduardo"
last_name = "Domínguez"
age = 22

impresion = f"Hola {name} {last_name}, tu edad es {age}"
print(impresion)
print(f"Hi my name is {name} {last_name}, and I'm {age} years old")
print(f"""

Hi my name is {name} {last_name},

and I'm {age} years old

""")
print(f'''

Hi my name is {name} {last_name},

and I'm {age} years old

''')
