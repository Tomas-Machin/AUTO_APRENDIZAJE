# rewrite your pay computaion with time-and-a-half for over time and createa  function called 
# computepay() which takes two parameters (hours, rate)

def computepay(hours, rate):
    if hours > 40:
        print("Overtime")
        pay = hours * rate + (hours - 40) * (rate * 1.5)
    else: 
        print("Regular")
        pay = hours * rate
    print("Pay: ", pay)

hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Not a number")
    quit()  # como un exit() en C
computepay(hours, rate)
