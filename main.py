import random

choose = "RPS"

comp = ""

for i in range(1):
    comp += random.choice(choose)

game = input("Rock (R) " \
"Paper (P) " \
"Scissors (S) ")

if game == "R" and comp == "R":
        print("It's a tie.")
elif game == "R" and comp == "P":
    print("I won!!")
elif game == "P" and comp == "R":
    print("You won.")
elif game == "P" and comp == "P":
        print("It's a tie.")
elif game == "P" and comp == "S":
        print("I won!!")
elif game == "S" and comp == "P":
        print("You won.")        
elif game == "S" and comp == "S":
        print("It's a tie.")
elif game == "S" and comp == "P":
        print("I won!!")
elif game == "S" and comp == "R":
        print("You won.")        