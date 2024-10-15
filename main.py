from generador import *
from soluciones import *
from config import *
from funciones_visuales import *
from colorama import Fore

def saludo_inicial():
    print(Fore.YELLOW + """     
     _____       _     _       
    |   __|_ _ _| |___| |_ _ _ 
    |__   | | | . | . | '_| | |
    |_____|___|___|___|_,_|___|     
                                                                
          """ + Fore.RESET)
    print(f'\nBienvenido al generador de sudokus {nombre}!\n')

def main():
    saludo_inicial()
    dificultad = input('Ingrese la dificultad del sudoku (facil, medio, dificil): ')
    print(Fore.LIGHTBLUE_EX + '\nSudoku Generado:\n', Fore.RESET)
    cuadricula = generar_sudoku(dificultad)
    imprimir_tablero(cuadricula)
    
    contador(tiempo)

    input(Fore.RED + '\n\nPresione Enter para ver las posibles soluciones del sudoku...\n' + Fore.RESET)
    print(Fore.LIGHTRED_EX + '\nSoluciones:\n', Fore.RESET)
    print(f'Hay {len(list(resolver([fila[:] for fila in cuadricula])))} solucion/es posible/s.')
    print('Una de las soluciones es:\n' + Fore.GREEN)
    imprimir_tablero(next(resolver([fila[:] for fila in cuadricula])))
    Fore.RESET
    ''' Ejemplo de uso para mostrar todas las soluciones
    for solucion in resolver([fila[:] for fila in cuadricula]):
        print(*solucion, sep='\n')
        print('-' * 20)
    '''

if __name__ == '__main__':
    main()