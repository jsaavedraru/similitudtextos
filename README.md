# Similitud entre palabras
## Objetivo

El objetivo del programa es comparar textos (de cualquier tipo) y encontrar el de mayor similitud para cada uno de ellos.

## Requerimientos

### Instalación
* Linux/Windows
* Python 3.4 o mayor
* Librerías:
  * numpy: `pip install -U numpy`
  * pandas: `pip install -U pandas`
  * scipy: `pip install -U scipy`
  * scikit-learn: `pip install -U scikit-learn`
  * stop_words:`pip install -U stop_words` (opcional)

## Instrucciones de uso

El programa debe estar en la misma carpeta que el dataset (donde están todos los archivos ".txt").

Para ejecutarlo se debe abrir la consola de comandos desde la carpeta en que se encuentra el programa. Por ejemplo:

```C:\Users\Usuario\dataset>python Programa.py```

## Resultado

El programa entrega un archivo de texto llamado "similitud.txt" que contiene 3 columnas:
```
Primera columna: Archivo procesado.
Segunda columna: Archivo de mayor similitud al archivo procesado.
Tercera columna: Valor de similitud coseno entre estos dos archivos (distancia).

```
