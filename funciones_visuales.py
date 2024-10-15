import time

def imprimir_tablero(tablero):
    for fila in range(len(tablero)):
        if fila % 3 == 0 and fila != 0:
            print("-" * 21)
        for columna in range(len(tablero[fila])):
            if columna % 3 == 0 and columna != 0:
                print("|", end=" ")
            if columna == 8:
                print(tablero[fila][columna])
            else:
                print(tablero[fila][columna], end=" ")

def contador(tiempo):
    for i in range(tiempo):
        print(f'{tiempo - i}', end='\r')
        time.sleep(1)