import urllib.request
countries_pib = []

def open_url(url):
    '''
    Esta funcion abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea
    y pregunta por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.

    Parametros:
        - file: fichero que muestra informacion de los paises de la UE.
    Salidas: No devuelve nada
    '''
    file = urllib.request.urlopen(url)
    lines = []
    for line in file:
        lines.append(str(line.decode("utf-8")))
    claves = lines[0].split("\t")
    for line in lines[1:]:
        country = {}
        valores = line.split("\t")
        for id in range(len(claves)):
            country[claves[id]] = valores[id]
        countries_pib.append(country)
    print(countries_pib)
    return

help(open_url)