# Sudoku

Este proyecto es una implementación de un juego de Sudoku en Python.

## Descripción

El juego de Sudoku es un rompecabezas basado en la lógica. El objetivo es llenar una cuadrícula de 9x9 con dígitos de tal manera que cada columna, cada fila y cada una de las nueve subcuadrículas de 3x3 contengan todos los dígitos del 1 al 9.

En este proyecto se implementan algunas funciones relacionadas con este juego. Como la generación o la resolución de Sudokus. Y algunas funciones visuales para entender como funcionan los métodos de resolución.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/mibullfire/Sudokus.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd sudoku
    ```

## Uso

Para iniciar el programa, ejecuta el siguiente comando:
```bash
python main.py
```

## Estructura del Proyecto

- `main.py`: Archivo principal que inicia el programa.
- `funciones_visuales.py`: Función visual para resolver un Sudoku (solo es visual).
- `config.py`: Configuraciones varias.
- `generador.py`: Contiene las funciones necesarias para generar Sudokus.
- `soluciones.py`: Contiene las funciones necesarias para obtener las soluciones del Sudoku creado.