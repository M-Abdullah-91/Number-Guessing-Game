import random

key = random.randint(1, 100)
print("Welcome to the guessing game!")

count = 0
num = int(input("Enter a Number to guess: "))

while num != key:

  if num > key:
    print("Enter Lower Number")
  else:
    print("Enter Higher number")
  num = int(input("Enter a Number to guess: "))
  count +=1

print("Correct")
print(f"Number of Attempts: {count}")

