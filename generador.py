import random  # Importa el módulo random para generar números aleatorios

def generar_sudoku(dificultad='media'):
    base = 3  # Define la base del Sudoku (3x3)
    lado = base * base  # Calcula el lado del Sudoku (9x9)

    # Función para definir el patrón de los números en el Sudoku
    def patron(r, c): return (base * (r % base) + r // base + c) % lado
    # Función para mezclar una lista de elementos
    def mezclar(s): return random.sample(s, len(s))

    rBase = range(base)  # Rango base (0, 1, 2)
    # Genera las filas mezcladas
    filas = [g * base + r for g in mezclar(rBase) for r in mezclar(rBase)]
    # Genera las columnas mezcladas
    columnas = [g * base + c for g in mezclar(rBase) for c in mezclar(rBase)]
    # Mezcla los números del 1 al 9
    numeros = mezclar(range(1, base * base + 1))

    # Genera el tablero de Sudoku basado en el patrón y las filas/columnas mezcladas
    tablero = [[numeros[patron(r, c)] for c in columnas] for r in filas]

    cuadrados = lado * lado  # Calcula el número total de cuadrados (81)
    vacios = cuadrados * 1 // 4  # Por defecto, 1/4 de los cuadrados estarán vacíos
    if dificultad == 'facil':
        vacios = cuadrados * 1 // 4  # Para dificultad fácil, 1/4 de los cuadrados estarán vacíos (20 vacíos)
    elif dificultad == 'media':
        vacios = cuadrados * 1 // 3  # Para dificultad media, 1/3 de los cuadrados estarán vacíos (27 vacíos)
    elif dificultad == 'dificil':
        vacios = cuadrados * 1 // 2  # Para dificultad difícil, 3/4 de los cuadrados estarán vacíos (40 vacíos)

    # Vacía los cuadrados seleccionados aleatoriamente
    for p in random.sample(range(cuadrados), vacios):
        tablero[p // lado][p % lado] = 0

    return tablero  # Devuelve el tablero de Sudoku generado
 

 
''' Ejemplo de uso
dificultad = 'media'  # Cambiar a 'facil', 'media', o 'dificil'
cuadricula = generar_sudoku(dificultad)
for fila in cuadricula:
    print(fila)  # Imprime cada fila del tablero de Sudoku
'''
if __name__ == '__main__':
    dificultad = 'media'  # Cambiar a 'facil', 'media', o 'dificil'
    cuadricula = generar_sudoku(dificultad)
    print(cuadricula)  # Imprime el tablero de Sudoku generado