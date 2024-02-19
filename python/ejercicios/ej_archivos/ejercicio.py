# write a program to read through a file and print the contents of the file (line by line) all in upper case.

# name = input("Enter the name of the file: ")
# name = "file.txt"
try:
    file = open(".\ejercicios\ej_archivos\document.txt")
except:
    print("File not found")
    quit()

for line in file:
    line = line.rstrip()
    print(line)