import os.path

def valor():
    """
    Esta funcion sirve para crear un fichero en formato .txt
    Parametros:
        - n: es el numero que esta predeterminado, en este caso es 2
    Salidas: no devuelve nada
    """
    numero = int(input('Introduce un número entero entre 1 y 10: '))
    if numero > 10 or numero < 1:
        print("El número introducido no es valido")
    file = 'tabla-' + str(numero) + '.txt'

    if os.path.isfile(file):
        f = open(file, 'r')
        f.read()
    else:
        print('No existe el fichero con la tabla del', numero)


valor()