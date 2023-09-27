#Guess a number
import random
secret_number = random.randint(0,10)
user_number = int(input("Enter the user number = "))
print(secret_number)
if secret_number == user_number:
    print("You won")
else:
    print("You lose. The number is", secret_number)
