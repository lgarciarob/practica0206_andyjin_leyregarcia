import urllib.request
def read_url(url):
    '''
    Esta función se encarga de acceder a un fichero de internet mediante su url
    y muestra el numero de palabras que contiene
    Parametros:
        - url: en este caso hemos elegido la web oficial de Python
    Salidas:
        - contenido: palabras que contiene la pagina web
    '''
    file = urllib.request.urlopen(url)
    contenido = file.read()
    print(len(contenido.split()))
    return

url = "https://www.python.org/downloads/"
(read_url(url))
help(read_url)