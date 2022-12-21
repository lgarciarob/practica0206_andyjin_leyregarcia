import os.path

def multiplicacion():
    '''
    Esta funcion pide dos numeros al usuario lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
    y muestre por pantalla la línea m del fichero.

    Parametros:
        - n: numero introducido por el usuario entre 1 y 10
        - m: numero introducido por el usuario entre 1 y 10

    Salidas: no devuelve nada
    '''
    n = int(input('Introduce un número entero entre 1 y 10: '))
    m = int(input('Introduce un número entero entre 1 y 10: '))

    file = 'tabla-' + str(n) + '.txt'

    if os.path.isfile(file):
        f = open(file, 'r')
        f.read(m)
    else:
        print('No existe el fichero con la tabla del', n)
    return

multiplicacion()