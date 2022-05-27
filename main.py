import random

print("Enter your guess word")
choices = ["agege", "ketu", "yaba"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("agege, ketu or yaba?: " ).lower()

if player == computer:
    print("computer: ", computer)
    print("player: ", player)
    print("tie")
elif player == "agege":
    if computer == "ketu":
        print("computer: ", computer)
        print("player: ", player)
        print("you lose")