user_option = input('piedra, papel o tijera  ')
user_option = user_option.lower()
print(user_option)

computer_option = 'papel'

if user_option == computer_option:
    print('Empate'+ user_option)

elif computer_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra gana a tijera')
        print('Computer gano!')
    else:
        print('Papel gana a piedra')
        print('User gano!')

elif computer_option == 'papel':
    if computer_option == 'piedra':
        print('Papel gana a piedra')
        print('Computer gano!')
    else:
        print('tijera gana a papel!')
        print('User gano!')

elif computer_option == 'tijera':
    if computer_option == 'papel':
        print('tijera gana a papel')
        print('Computer ganos')
    else:
        print('piedra gana a tijera')
        print('User gano')
