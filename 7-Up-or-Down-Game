# 7 Up or Down Game
import random
number = random.randint(1,13)
user_choice = input("Enter the user choice (above7, below7, equal7) = ").lower()
if (user_choice not in ("below7", "above7", "equal7")):
    print("Invalid")
elif (number > 7) and (user_choice == "above7"):
    print("You win!")
    print("The number is", number)
elif (number < 7) and (user_choice == "below7"):
    print("You win!")
    print("The number is", number)
elif (number == 7) and (user_choice == "equal7"):
    print("You win!")
    print("The number is", number)
else:
    print("Sorry, you lose.")
    print("The number is", number)