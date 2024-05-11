line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
position = input("Type a letter in between A-C and a number between 1-3: ")
letter = (position[0])

if letter.upper() == "A":
  letter = 0
elif letter.upper() == "B":
  letter = 1
elif letter.upper() == "C":
  letter = 2
  
number = int(position[1]) -1
map[number][letter] = "X"
print(f"{line1}\n{line2}\n{line3}")