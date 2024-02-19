"""
--- GUIA ---
^ - principio de una linea
$ - final de una linea
. - es cualquier caracter
\s - espacio en blanco
\S - cualquier caracter q no sea un espacio en blanco
* - repite un caracter 0 o mas veces
*? - igual q * pero no voraz (non-greedy)(quiere decir q no coge la opcion mas larga)
+ - repite un caracter una o mas veces
+? - igual q + pero no voraz
[aeiou] - es un caracter en la lista creada
[^XYZ] - es un caracter q no esta en la lista creada
[a--z0-9] - rango de caracteres?
( - extraccion de string apunto de empezar
) - extraccion de string apunto de acabar

!!! import re !!!
re.search() ~ find() - conjuntos (devuelve true | false)
# "if line.find("From:") >= 0:" = "if re.search("From:", line):
re.search() ~ startswith() 
# "if line.startswith("From:") >= 0:" = "if re.search("^From:", line):
re.findall() ~ find(var[5:10]) - porciones (devuelve strings)

"""
import re
x = "My 2 favorite number are 19 and 42"
y = re.findall("[0-9]+", x)  # en strings intenta imprimir la cadena mas larga q cumpla los requisitos (se le llama greedy)
print(y)
y = re.findall("[aeiou]+", x) # devuelve las vocales minus y no mayus ("[AEIOU]")
print(y)
#-------------------------------------
print("-----------------------------")
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
"""
atpos = data.find("@")
print(atpos) # 21
sppos = data.find(' ', atpos)
print(sppos) # 31
host = data[atpos + 1 : sppos]
print(host) # uct.ac.za
""" # esto es igual a:
y = re.findall("@([^ ]*)", data) #[^ ] - significa no espacio en blanco
y = re.findall("^From .*@([^ ]*)", data)
print(y)
# para poder buscar $ se usa \$