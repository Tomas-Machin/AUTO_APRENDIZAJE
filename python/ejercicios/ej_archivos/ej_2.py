try:
    file = open(".\ejercicios\ej_archivos\mbox-short.txt")
except:
    print("File not found")
    quit()

for line in file:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3: continue
    if words[0] != "From":
        continue
    print(words[2])