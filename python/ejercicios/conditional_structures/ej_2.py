<<<<<<< HEAD
# rewrite your pay program using try and except  so that your program handles non-numeric
# input gracefully by printing a message and exiting the program.
hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Not a number")
    quit()  # como un exit() en C
if hours > 40:
    print("Overtime")
    pay = hours * rate + (hours - 40) * (rate * 1.5)
else: 
    print("Regular")
    pay = hours * rate
=======
# rewrite your pay program using try and except  so that your program handles non-numeric
# input gracefully by printing a message and exiting the program.
hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Not a number")
    quit()  # como un exit() en C
if hours > 40:
    print("Overtime")
    pay = hours * rate + (hours - 40) * (rate * 1.5)
else: 
    print("Regular")
    pay = hours * rate
>>>>>>> 70eeabf7fe0392c3aa721948c166730523aa1e3e
print("Pay: ", pay)