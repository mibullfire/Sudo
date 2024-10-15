import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

def k_valido(tabla, f, c, k):
    # Verifica la fila
    for x in range(9):
        if tabla[f][x] == k:
            return False
    # Verifica la columna
    for x in range(9):
        if tabla[x][c] == k:
            return False
    # Verifica la subcuadrícula 3x3
    inicio_fila = (f // 3) * 3
    inicio_columna = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if tabla[inicio_fila + i][inicio_columna + j] == k:
                return False
    return True

def imprimir_tabla(tabla, ultimo_f=None, ultimo_c=None):
    os.system('clear')
    for f in range(9):
        if f % 3 == 0 and f != 0:
            print("-" * 21)
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")
            num = tabla[f][c]
            if f == ultimo_f and c == ultimo_c:
                print(Fore.GREEN + str(num) if num != 0 else '.', end=" ")
            else:
                print(str(num) if num != 0 else '.', end=" ")
        print()
    time.sleep(0.05)

def solve(tabla, f=0, c=0):
    if f == 9:
        return True
    elif c == 9:
        return solve(tabla, f+1, 0)
    elif tabla[f][c] != 0:
        return solve(tabla, f, c+1)
    else:
        for k in range(1, 10):
            if k_valido(tabla, f, c, k):
                tabla[f][c] = k
                imprimir_tabla(tabla, f, c)
                if solve(tabla, f, c+1):
                    return True
                tabla[f][c] = 0
        return False

# Tablero inicial de Sudoku con algunas celdas llenas
tabla = [
[1, 0, 0, 6, 7, 0, 8, 0, 0], [0, 8, 0, 4, 0, 1, 7, 0, 0], [5, 7, 6, 0, 8, 2, 9, 1, 4], [8, 0, 0, 2, 3, 9, 0, 0, 1], [7, 4, 1, 5, 0, 8, 3, 9, 2], [9, 0, 2, 1, 0, 7, 6, 8, 0], [4, 0, 9, 0, 1, 0, 5, 3, 0], [6, 0, 7, 8, 5, 3, 2, 4, 9], [0, 5, 8, 9, 2, 0, 1, 0, 7]
]

# Resuelve el Sudoku y muestra el resultado
solve(tabla)
imprimir_tabla(tabla)