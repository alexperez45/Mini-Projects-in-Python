print("Welcome to your local Python Pizzeria!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size.upper() == 'S':
    bill += 12
elif size.upper() == 'M':
    bill += 16
elif size.upper() == 'L':
    bill += 20

if add_pepperoni.upper() == 'Y' and size == 'S':
    bill += 2
elif add_pepperoni.upper() == 'Y':
    bill += 3

if extra_cheese.upper() == 'Y':
    bill += 1

print (f'Your final bill is: ${bill}.')