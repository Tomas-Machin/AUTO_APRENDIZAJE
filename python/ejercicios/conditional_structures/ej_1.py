<<<<<<< HEAD
# rewrite your pay computation to give the employee 1.5 tomes the hourly rate for 
# hours worked above 40 hours.
hours = input("Enter hours: ")
hours = float(hours)
rate = input("Enter rate: ")
rate = float(rate)
if hours > 40:
    print("Overtime")
    pay = hours * rate + (hours - 40) * (rate * 1.5)
else: 
    print("Regular")
    pay = hours * rate
print("Pay: ", pay)

=======
# rewrite your pay computation to give the employee 1.5 tomes the hourly rate for 
# hours worked above 40 hours.
hours = input("Enter hours: ")
hours = float(hours)
rate = input("Enter rate: ")
rate = float(rate)
if hours > 40:
    print("Overtime")
    pay = hours * rate + (hours - 40) * (rate * 1.5)
else: 
    print("Regular")
    pay = hours * rate
print("Pay: ", pay)

>>>>>>> 70eeabf7fe0392c3aa721948c166730523aa1e3e
