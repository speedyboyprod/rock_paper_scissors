import random

computerChoice = random.choice(["scissors", "rock", "paper"])
usersChoice = input("What are you gonna choose? ")

if computerChoice == usersChoice:
    print("You both chose the same thing.")
    print("It's a tie!")
elif usersChoice == "rock" and computerChoice == "scissors":
    print("They chose scissors.")
    print("You win!")
elif usersChoice == "scissors" and computerChoice == "paper":
    print("They chose paper.")
    print("You win!")
elif usersChoice == "paper" and computerChoice == "rock":
    print("They chose rock.")
    print("You win!")
else:
    print("You lose.")
