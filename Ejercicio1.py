def valor(n):
   """
   esta funcion sirve para crear un fichero en formato .txt
   Parametros:
   - n: es el numero que esta predeterminado, en este caso es 2
   salidas: no devuelve nada
   """
   if n in range(1,11):
       file = open("Tabla-" + str(n) + "txt","w")
       for numero in range(1,11):
           file.write(str(n * numero) + "\n")
   return
valor(2)
help(valor)