# funciones
# def --> defined function: def "funncion()":
def thing():  #no ejecuta nada sino es la creacion de un metodo
    print("Hello")
    print("fun")

thing()  # llama al metodo para ejecutarlo
print("Zip")
thing()

# len()   - para calcular el tamaño del string; en listas devuelve la cantidad de elemntos en la lista
print(len("banana"))  # 6

# .lower() - imprime en minusculas a pesar de q haya mayus (pasa lo contrario con .upper())
print("PEne".lower()) #pene

# find() - buscar una cadena de caracteres dentro de otra, devuelve la posicion de substring en el string original y sino hay devuelve -1

# .replace() - reemplaza algo por otra cosa
greet = "Hello Bob"
nstr = greet.replace("Bob", "Jane")  # tmb puedo hacerlo con letras, etc
print(nstr)  # "Hello Jane"

# .lstrip() | rstrip() - quitar los espacios de la izq o der respectivamente
# .strip() - para quitar los espacios a ambos lados

# .startswith() - para saber si un string empieza por algo en especifico (distingue entre mayus y minus)
n = "Hola genio"
print(n.startswith("H")) # true, si fuera "h" eri false

# range(n) - devuelve una lista de numeros desde 0 hasta el parametro n - 1
friends = ["Joseph", "Sally", "Glenn"]
for i in range(len(friends)):
    friend = friends[i]
    print(friend)

# sorted("lista"|"diccionario", "atributos") atributos: reverse = True | False

# ord() - para obtener el valor numerico de un carracter ASCII (letra)