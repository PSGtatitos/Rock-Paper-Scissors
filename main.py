import random

comppoint = 0
userpoint = 0
choose = "RPS"

while True:
    comp = random.choice(choose)  # Randomly choose one option for the computer
    print(comp)
    game = input("Rock (R), Paper (P), Scissors (S): ").strip()
    
    if game.lower() == "r" and comp == "R":
        print("It's a tie.")
    elif game.lower() == "r" and comp == "P":
        print("I won!!")
        comppoint += 1
    elif game.lower() == "r" and comp == "S":
        print("You won.")
        userpoint += 1
    elif game.lower() == "p" and comp == "R":
        print("You won.")
        userpoint += 1
    elif game.lower() == "p" and comp == "P":
        print("It's a tie.")
    elif game.lower() == "p" and comp == "S":
        print("I won!!")
        comppoint += 1
    elif game.lower() == "s" and comp == "P":
        print("You won.")
        userpoint += 1
    elif game.lower() == "s" and comp == "S":
        print("It's a tie.")
    elif game.lower() == "s" and comp == "R":
        print("I won!!")
        comppoint += 1
    else:
        print("Invalid input. Please choose R, P, or S.")
        continue

    print(f"Score - You: {userpoint}, Computer: {comppoint}")

    if comppoint == 3:
        print("I won the game.")
        break
    elif userpoint == 3:
        print("You won the game.")
        break
