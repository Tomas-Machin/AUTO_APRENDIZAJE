
fname = input("Enter file:")
if len(fname) < 1: 
    fname = ".\ejercicios\ej_archivos\clown.txt" 

#fname = ".\ejercicios\ej_archivos\clown.txt"
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1

print(di)

tmp = list()
for k, v in di.items():
    # print(k, v)
    newtuple = (v, k)  # para darle la vuelta
    tmp.append(newtuple)

tmp = sorted(tmp[:5])  # los ordenamos por valores (v) y cogemos los primeros 5
print(tmp)
