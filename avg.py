import sys

for elemento in sys.argv:
    print(elemento)

suma_argumentos =  sum([int(i) for i in sys.argv[1:]])

#contamos cuantos elementos tiene
longitud_lista = len(sys.argv[1:])

media = f"{suma_argumentos / longitud_lista:.2}"

print (media)
 