print("hello from a file")
# comandos para el cmd de python:
# ejecutar un programa: python "nombre programa" | "nombre programa"

# NO HAY Q DECLARAR EL TIPO DE VALOR Q ES DE NADA

x = 1
x = x + 1
print(x)

# para los if: se hace enter y se tabula y eso es lo q esta dentro del if
# tabular para caba if hecho (for y while tmb)

x = 5
if x < 10:
    print("Smaller")
if x > 20:
    print("Larger")
print("End")
# mostrara: Smaller y End
while x > 0:
    print(x)
    x = x - 1
print("Blasstoff")
# mostrara los numeros desde x = 5 hasta x = 1 de uno en uno y luego Blasstoff
# operadores: + - / * % ** (suma, resta, div, mult, modulo, potencia)

e = "hello " + "world" 
print(e) # hello world
type(e)  # devuelve el tipo de variable q es (String, int, float...) EN CMD

# convertir un int a float --> i = 1; float(i) | float("numero")
# igual pero convertir a int --> s = "123" ; int(s) | int("valor")  (PERO SOLO NUMEROS)

name = input("Who are you? ")  
#imprime el texto y espera a q escribamos algo por el terminal
# y luego se imprime el print + lo introducido (el resto del codigo)
# else if en python --> elif
# NO SE USAN CORCHETES SINO ":""
print("welcome", name)      
# try - exception -> try - except en python  
