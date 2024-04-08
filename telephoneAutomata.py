def spanish_phone_number(phone_number):
    # Definir los estados del autómata
    states = {
        'start': {'3': 'prefijo', '6': 'valid', '7': 'valid', '8': 'valid', '9': 'valid'},
        'prefijo': {'4': 'prefijo_valid'},
        'prefijo_valid': {'6': 'valid', '7': 'valid', '8': 'valid', '9': 'valid'},
        'valid': {'0': 'valid', '1': 'valid', '2': 'valid', '3': 'valid', '4': 'valid', '5': 'valid', '6': 'valid', '7': 'valid', '8': 'valid', '9': 'valid'}
    }

    # Definir el estado inicial
    state = 'start'

    # Iterar sobre cada dígito del número de teléfono
    for digit in phone_number:
        # Cambiar al estado correspondiente
        if digit in states[state]:
            state = states[state][digit]
        else:
            # Si el dígito no está en el diccionario de estados, devolver False
            return False

    # Si el estado final es 'valid' o '34valid', devolver True
    return state == 'valid' or state == 'prefix_valid'


# Ejemplo de uso
phone_number = input("Introduce un número de teléfono: ")
if spanish_phone_number(phone_number):
    print("El número de teléfono es español.")
else:
    print("El número de teléfono no es español.")