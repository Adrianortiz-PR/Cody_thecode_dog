def print_dog():
    print("  /^-----^\       ")
    print("  V  o o  V       ")
    print("   |  Y  |        ")
    print("    \ Q /         ")
    print("    / - \         ")
    print("    |    \        ")
    print("    |     \     ) ")
    print("    || (___\====  ")

def play_game():
    F1_moves = ["rock", "paper", "scissors"]
    F2_moves = ["rock", "paper", "scissors"]

    user_input = input("Hello, I'm Cody the code dog!! What is your name?: ")
    print_dog()
    print("Hello,", user_input, "would you like to play rock, paper, and scissors? ")

    while True:
        F1 = input("I made my move. What will you pick? ")
        F2 = random.choice(F2_moves)

        if F1 == F2:
            print(F1, "and", F2, "It's a draw!")
        elif (F1 == "rock" and F2 == "scissors") or \
             (F1 == "scissors" and F2 == "paper") or \
             (F1 == "paper" and F2 == "rock"):
            print("Wow! Well played, your", F1, "beats my", F2 + "!")
        else:
            print("Sorry! My", F2, "beats your", F1 + "!")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break

import random

if __name__ == "__main__":
    play_game()
