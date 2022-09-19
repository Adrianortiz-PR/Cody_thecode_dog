def dog():
 print("  /^-----^\       ")
 print("  V  o o  V       ")
 print("   |  Y  |        ")
 print("    \ Q /         ")
 print("    / - \         ")
 print("    |    \        ")
 print("    |     \     ) ")
 print("    || (___\====  ")


    
User=input("Hello, I'm Cody the code dog!! What is your name?: ")
dog()
print("Hello!", User, "would you like to play rock,paper and scissors? ")
import random
while True:
 F1moves=["rock","paper","scissors"]
 F2moves=["rock","paper","scissors"]
 F1=input("I made my move what will you pick? ")
 F2=random.choice(F2moves)

 if F1==F2:
    print(F1, "and", F2, "looks like a draw!")
 elif F1=="rock" and F2 == "scissors":
    print("Wow! well played your rock beats my scissors!")
 elif F1=="scissors" and F2 == "paper":
    print("Wow! well played your scissors beats my paper!")
 elif F1=="paper" and F2 == "rock":
    print("Wow! well played your paper beats my rock")
 elif F1=="rock" and F2 == "paper":
    print("Sorry! paper beats rock!")
 elif F1=="paper" and F2 == "scissors":
    print("Sorry! scissors beats paper!")
 elif F1=="scissors" and F2 =="rock":
    print("Sorry! rock beats scissors!")