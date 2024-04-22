# User enters height in meters
height = float(input("Enter your height in meters: "))
# User enters weight in Kilos
weight = int(input("Enter your weight in Kilograms: "))
BMI = round (weight / height ** 2, 2)
if BMI <= 18.5:
  print (f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print (f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
  print (f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
  print (f"Your BMI is {BMI}, you are obese.")
elif BMI >= 35:
  print (f"Your BMI is {BMI}, you are clinically obese.")