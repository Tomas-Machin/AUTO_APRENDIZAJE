
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff")
print(n)
#----------------------------
while True:
    line = input('> ')
    if line == "done":
        break
    print(line)  # imprime lo puesto por el terminals
print("Done!")
#----------------------------
for i in [5, 4, 3, 2, 1]:
    print(i)  # imprime los numeros dentro de la lista
#---------------------------
friends = ["Joseph", "Glenn", "Sally"]
for friend in friends:  # friend en una nueva variable
    print("Happy New Year: ", friend)
#----------------------------
largest_so_far = -1  # puedo declararlo "None" (sin valor) para q "coja el primer valor"
print("Largest before checking the list:", largest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if num > largest_so_far:
        largest_so_far = num
    # print(largest_so_far, num)
print("Largest after checking the list:", largest_so_far)

smallest = None 
print("Smallest before checking the list:", largest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num
    # print(largest_so_far, num)
print("Smallest after checking the list:", smallest)
#----------------------------
for n in "banana":
    print(n)   # deletrea la palabra/frase
