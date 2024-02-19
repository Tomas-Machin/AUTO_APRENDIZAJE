# concatenar listas
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b # [1, 2, 3, 4, 5, 6]
# recordar q puedes imprimir elementos como en R [1:10]...

# crear una lista: list() (con parentesis es crear un lista vacia (forma de constructor))
lista = list()
# añadir elememtos: append()
lista.append("algo")
lista.append(12345)
# preguntar saber si hay algo en la lista: "algo" (not) in "lista" ; devuelve true o false al hacer print

# ordenar elementos: .sort() (alfabeticamente o numericamente)
# numero maximo y min:max("lista") y min("lista")
# suma de elementos: sum("lista")
# conteo de elemtos: len("lista")

abc = "With three words"
stuff = abc.split()  # la funcion split() divide por espacios/palabras por defecto, puedes cmabiar el tipo de separador
print(stuff)
print("---------------------------------------------")
"""
-------- TUPLAS --------

no usar: .sort(), .sppend(), .reverse() con ellas
las tuplas no son modificables. las listas si.
se pueden declarar con: tuple() 
cosas q se pueden hacer -> count, index
se puede imprimir un solo miembro de la tupla:
    (a, b) = (4, "fred") -> a = 4, b = "fred"
puedo usar tuplas para imprimir elementos de un diccionario
se pueden comparar tuplas entre ellas (compara a1 con b1 y asi hasta q se cumpla la condicion sino es falsa)
comparar lo mismo con string es comparar letras en caso de empezar igual
"""
# ordenacion de listas de tuplas
d = {'a' : 10, 'c' : 22, 'b' : 1}
print(d.items()) # dict_itms([('a' : 10), ('c' : 22), ('b' : 1)])
print(sorted(d.items())) # [('a', 10), ('b', 1), ('c', 22)]
for a, b in sorted(d.items()):
    print(a, b) # imprimir value, si fuera solo la a es la key

print("-----------------------")
text = "mbox-short.txt"
counts = dict()

for line in text:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lista = list()
for key, value in counts.items():
    newtup = (value, key)
    lista.append(newtup)
lista = sorted(lista, reverse=True)

for value, key in lista[:10]:
    print(key, value)

# modo simplificado / mas corto
print( sorted ( [ (v,k) for k,v in d.items() ], reverse=True ) )