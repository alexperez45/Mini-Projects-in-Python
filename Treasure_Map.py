line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()
letter = (position[0])

if letter == "A":
  letter = 0
elif letter == "B":
  letter = 1
elif letter == "C":
  letter = 2
  
number = int(position[1]) -1
map[number][letter] = "X"
print(f"{line1}\n{line2}\n{line3}")