#program to make a number guessing game between (1-100)
import random 
target = random.randint(1,100)
print("Rule 1: No. of attempts is 7")
print("Rule 2: Guess no. only between 1-100")
for i in range(7):
    num = input("Guess the target number or Quit (Q) : ")
    if (num=='Q'):
        break
    x = int(num)
    if (x==target):
        print("Congrats! You won")
        break
    elif (x>100):
        break
    elif (x<1):
        break
    elif (x<target):
        print("Your guess is too small. Take a bigger guess")
    elif (x>target):
        print("You guessed too large. Take a smaller guess")
    elif (i>5):
        print("No. of attempts exceeded")
    else:
        print("Wrong input")

print("-----GAME OVER-----")