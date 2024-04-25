print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

name12 = name1.upper() + name2.upper()

nameTrue1 = name12.count("T")
nameTrue2 = name12.count("R")
nameTrue3 = name12.count("U")
nameTrue4 = name12.count("E")

nameLove1 = name12.count("L")
nameLove2 = name12.count("O")
nameLove3 = name12.count("V")
nameLove4 = name12.count("E")

true_total = nameTrue1 + nameTrue2 + nameTrue3 + nameTrue4
love_total = nameLove1 + nameLove2 + nameLove3 + nameLove4
total = int(str(true_total) + str(love_total))

if total < 10 or total > 90:
  print (f"Your score is {total}, you go together like coke and mentos.")
elif total < 50 and total > 40:
  print (f"Your score is {total}, you are alright together.")
else:
  print (f"Your score is {total}.")