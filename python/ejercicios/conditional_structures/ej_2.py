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
print("Pay: ", pay)