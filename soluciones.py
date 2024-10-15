def es_valido(grid, r, c, k):
    # Verifica si el número k puede ser colocado en la posición (r, c) de la cuadrícula
    no_en_fila = k not in grid[r]  # Verifica que k no esté en la fila r
    no_en_columna = k not in [grid[i][c] for i in range(9)]  # Verifica que k no esté en la columna c
    no_en_caja = k not in [grid[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]  # Verifica que k no esté en la caja 3x3 correspondiente
    return no_en_fila and no_en_columna and no_en_caja  # Devuelve True si k no está en la fila, columna ni caja


def resolver(grid, r=0, c=0):
    # Resuelve el Sudoku utilizando backtracking
    if r == 9:
        # Si se ha llegado a la fila 9, se ha completado una solución
        yield [fila[:] for fila in grid]  # yield una copia de la cuadrícula como solución
    elif c == 9:
        # Si se ha llegado a la columna 9, pasa a la siguiente fila
        yield from resolver(grid, r + 1, 0)
    elif grid[r][c] != 0:
        # Si la posición (r, c) ya está llena, pasa a la siguiente columna
        yield from resolver(grid, r, c + 1)
    else:
        # Intenta colocar los números del 1 al 9 en la posición (r, c)
        for k in range(1, 10):
            if es_valido(grid, r, c, k):
                # Si k es válido en la posición (r, c), colócalo
                grid[r][c] = k
                # Continúa resolviendo el resto de la cuadrícula
                yield from resolver(grid, r, c + 1)
                # Si no se encuentra una solución, deshace la colocación de k
                grid[r][c] = 0


''' Ejemplo de uso
cuadricula = [
    [0, 0, 0, 4, 0, 0, 9, 0, 0],
    [0, 0, 0, 8, 0, 1, 0, 1, 2],
    [0, 0, 0, 0, 1, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [1, 0, 2, 3, 0, 0, 0, 5, 0],
    [0, 7, 4, 0, 9, 0, 1, 0, 0],
    [0, 0, 8, 2, 0, 4, 0, 0, 5],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 3, 0]
]
for solucion in resolver([fila[:] for fila in cuadricula]):
    print(*solucion, sep='\n')
    print('-' * 20)
'''