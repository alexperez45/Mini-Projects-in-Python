# User enters year
year = int(input("Type a year: "))
# year_by_4 = year % 4 
# year_by_100 = year % 100
# year_by_400 = year % 400
if year % 4 > 0:
  print ("Not leap year")
elif year % 100 > 0:
  print ("Leap year")
elif year % 400 == 0:
    print ("Leap year")
else:
  print ("Not leap year")