print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

name1 = name1.upper()
name2 = name2.upper()

nameTrue1 = name1.count("T") + name2.count("T")
nameTrue2 = name1.count("R") + name2.count("R")
nameTrue3 = name1.count("U") + name2.count("U")
nameTrue4 = name1.count("E") + name2.count("E")

nameLove1 = name1.count("L") + name2.count("L")
nameLove2 = name1.count("O") + name2.count("O")
nameLove3 = name1.count("V") + name2.count("V")
nameLove4 = name1.count("E") + name2.count("E")

true_total = nameTrue1 + nameTrue2 + nameTrue3 + nameTrue4
love_total = nameLove1 + nameLove2 + nameLove3 + nameLove4
total = int(str(true_total) + str(love_total))

if total < 10 or total > 90:
  print (f"Your score is {total}, you go together like coke and mentos.")
elif total < 50 and total > 40:
  print (f"Your score is {total}, you are alright together.")
else:
  print (f"Your score is {total}.")