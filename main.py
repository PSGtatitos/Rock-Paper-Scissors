import random

choose = "RPS"

comp = ""

for i in range(1):
    comp += random.choice(choose)
print(comp)
game = input("Rock (R) " \
"Paper (P) " \
"Scissors (S) ")

if game == "R" or "r" and comp == "R":
        print("It's a tie.")
elif game == "R" or "r" and comp == "P":
    print("I won!!")
elif game == "R" or "r" and comp == "S":
    print("You won.")
elif game == "P" or "p" and comp == "R":
    print("You won.")
elif game == "P" or "p" and comp == "P":
        print("It's a tie.")
elif game == "P" or "p" and comp == "S":
        print("I won!!")
elif game == "S" or "s" and comp == "P":
        print("You won.")        
elif game == "S" or "s" and comp == "S":
        print("It's a tie.")
elif game == "S" or "s" and comp == "R":
        print("I won!!")        
