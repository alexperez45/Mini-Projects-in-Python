import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

number = random.randint(1,3)

print ("Lets play rock, paper, scissors!")
choice = input ("Type 1 for rock, 2 for paper, 3 for scissors: ")

if choice == "1" and number == 1:
    print (rock)
    print ("It's a tie!")
    print (rock)
elif choice == "1" and number == 2:
    print (rock)
    print ("You Lose!")
    print (paper)
elif choice == "1" and number == 3:
    print (rock)
    print ("You win!")
    print (scissors)
elif choice == "2" and number == 1:
    print (paper)
    print ("You Win!")
    print (rock)
elif choice == "2" and number == 2:
    print (paper)
    print ("Its a tie!")
    print (paper)
elif choice == "2" and number == 3:
    print (paper)
    print ("You Lose!")
    print (scissors)
elif choice == "3" and number == 1:
    print (scissors)
    print ("You Lose!")
    print (rock)
elif choice == "3" and number == 2:
    print (scissors)
    print ("You Win!")
    print (paper)
elif choice == "3" and number == 3:
    print (scissors)
    print ("Its a tie!")
    print (scissors)
