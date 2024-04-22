print ("Welcome to the Tip Calucator!")
bill = float (input ("What is the total bill? $"))
tip = float (input ("What percentage would you like to tip? 10, 12, 15, or 20? "))
people = float (input ("How many people will split the bill? "))
tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / people
rounded_amount = "{:.2f}".format(bill_per_person)
print (f"Each person should pay ${rounded_amount}")
