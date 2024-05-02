print("Welcome to the tip Calculator!\n")
total = float(input("What was the total bill? $"))
people = int(input("How many people do you want to split the bill in? "))
tip = float(input("What percentage of the bill would you like to tip? "))
tip = tip / 100

total = total + (total * tip)
average = round(total / people, 2)

print("Each person should pay $"+str(average))