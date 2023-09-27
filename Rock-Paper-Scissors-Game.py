#Rock, Paper, Scissors Game
import random
options = ["rock","paper", "scissors"]
computer_choice = random.choice(options)
user_choice = input("Guess between rock, paper, scissors = ").lower()
if  (computer_choice == "scissors") and (user_choice=="paper"):
    print("Computer won","The computer choice is",computer_choice)
elif (computer_choice == "paper") and (user_choice=="scissors"):
    print("User won","The computer choice is",computer_choice)
elif (computer_choice == "scissors") and (user_choice=="rock"):
    print("User won", "The computer choice is",computer_choice)
elif (computer_choice == "rock") and (user_choice=="scissors"):
    print("Computer won", "The computer choice is",computer_choice)
elif (computer_choice == "rock") and (user_choice=="paper"):
    print("Computer won", "The computer choice is",computer_choice)
elif (computer_choice == "paper") and (user_choice=="rock"):
    print("User won", "The computer choice is",computer_choice)
else:
    print("Neither won", "The computer choice is",computer_choice)