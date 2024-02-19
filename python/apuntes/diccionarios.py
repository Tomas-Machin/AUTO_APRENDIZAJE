"""
la posicion se fija por el orden en el q se añaden elemento aunq no hay orden (el index pasa a ser el nombre q le des a ese valor)
hay q buscar asi: "diccionario"["lo_que_buscas"] (tmb le puedes asignar valores o cambiarlos)
"""

purse = dict() # declaracion
purse["money"] = 12
purse["candy"] = 3
print(purse) # {'money': 12, 'candy': 3}
# print(purse[0]) - no se puede hacer esto
print(purse["money"]) # esto si funciona

dict = {"Fri": 20, "Thu": 6, "Sat": 1}
dict["Thu"] = 13  # actualiza valores
dict["Sat"] = 2
dict["Sun"] = 9  # como no existe lo crea dentro de la lista

# para hacer conteos (modo elegir delegado pizarra)
"""
counts = dict()
counts = {"csev", "cwen", "csev", "zqian", "cwen"}
for name in counts:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
--------------------------
VERSION SIMPLIFICADA
--------------------------
counts = dict()
counts = {"csev", "cwen", "csev", "zqian", "cwen"}
for name in counts:
    counts[name] = counts.get(name, 0) + 1
print(counts)
--------------
"""
# podemos ver si hay algun elemento en la lista asi: "nombre_elemento" in "diccionario"

# funcion .get("name", 0 "default_value")
algo = None
if algo in purse:
    x = purse[algo]
else:
    x = 0
x = purse.get(algo, 0)  
print(x)
# -------------------------------
counts = {}  # para crearlo vacio

print("Enter a line of text: ")
line = input("")
words = line.split()

print("Words: ", words)
print("Counting...")

for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Counts ", counts)

# coger las llaves (keys) - .keys()
# coger los valores (values) - .values()
# coger conjunto/tuplas (keys + valores) - .items()
# se pueden usar para iterar: for "nombre_keys", "nombre_values" in counts.items()


