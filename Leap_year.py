# User enters year
year = int(input("Type a year: "))
# Make calculation to determine if year is a leap year
if year % 4 > 0:
  print (f"{year} is NOT a leap year")
elif year % 100 > 0:
  print (f"{year} is a leap year!")
elif year % 400 == 0:
    print (f"{year} is a leap year!")
else:
  print (f"{year} is NOT a leap year")