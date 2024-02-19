# se pueden coger partes de cosas [1:10] como en R (tambien se pueden omitir el principio o final para emezar al principio o acabar al final o hacer ambas)
frase = "me cago en tu puta madre"
print(frase[14:18]) # puta
print(frase[:7]) # me cago
print(frase[14:]) # puta madre
print(frase[:]) # me cago en tu puta madre
print('n' in frase) # true
#----------------------------
"""word = "banana"
if word == "banana":
    print("All right bananas")

if word < "banana":
    print("Your word, " + word + ", comes before banana")
elif word > "banana":
    print("Your word, " + word + ", comes after banana")
else: print("All right banana")"""
#----------------------------
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print(atpos) # 21
sppos = data.find(' ', atpos)
print(sppos) # 31
host = data[atpos + 1 : sppos]
print(host) # uct.ac.za
