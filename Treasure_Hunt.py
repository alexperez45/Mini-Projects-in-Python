print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print ("Welcome to my treasure game!")
print ("Your goal is to find the tresure.")
print("You've come across a cross road. One road is colored blue and the other yellow.")
path = input ('Which one do you choose? Type "blue" or "yellow"\n')

if path.upper() == "YELLOW":
    print ("You go down the road and find a river.")
    river = input ('Type "build" to build a boat. Type "swim" to swim across.\n')
    if river.upper() == "SWIM":
        print ("You start swimming but then get attacked by a sea monster. You died.")
    if river.upper() == "BUILD":
        print ("Yay you made it across the river! Now you approach 3 houses.")
        house = input('Type "1" for house 1, "2" for house 2, or "3" for house 3.\n')
        if house == "1":
            print ("Hooray, you found the treasure! You win!")
        elif house == "2":
            print ("You walk inside the house and get hit by all the booby traps. You died.")
        elif house == "3":
            print ("You walk inside the house and get attacked by piranhas. You died.")
elif path.upper() == "BLUE":
    print ("Oh no you were attacked by a pack of wolves! You died.")



