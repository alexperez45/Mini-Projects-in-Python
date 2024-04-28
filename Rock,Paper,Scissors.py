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

number = random.randint(0,2)
images = [rock, paper, scissors]

print ("Lets play rock, paper, scissors!")
choice = int (input ("Type 0 for rock, 1 for paper, 2 for scissors: "))

if choice <=2:
    print (images[choice])
    print (images[number])
    if choice == number:
        print ("It's a tie!")
    elif choice == 0 and number == 1:
        print ("You Lose!")
    elif choice == 0 and number == 2:
        print ("You win!")
    elif choice == 1 and number == 0:
        print ("You Win!")
    elif choice == 1 and number == 2:
        print ("You Lose!")
    elif choice == 2 and number == 0:
        print ("You Lose!")
    elif choice == 2 and number == 1:
        print ("You Win!")
else:
    print ("You did not enter a correct value. You Lose!")
