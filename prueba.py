import time

# Inicializamos el primer valor
caracter = '1'

while True:
    # Mostramos el carácter
    print(caracter, end='\r')  # Mostramos el carácter en la misma línea
    time.sleep(1)  # Esperamos 1 segundo
    
    # Mostramos un espacio para que desaparezca el carácter
    print(' ', end='\r')  # Borramos el carácter con un espacio
    time.sleep(1)  # Esperamos 1 segundo
    
    # Cambiamos el valor del carácter
    if caracter == '1':
        caracter = '0'
    else:
        caracter = '1'