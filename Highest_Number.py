print ("Type some numbers to get the highest one: ")
numbers = input().split()
for n in range(0, len(numbers)):
  numbers[n] = int(numbers[n])

highest_number = 0
for score in numbers:
  if score > highest_number:
    highest_number = score

print(f"The highest number is: {highest_number}")