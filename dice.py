#!/usr/bin/env python3
import random
import sys

# MAIN
diceSelect = int(input("How Many Sides Do You Want On Your Dice? (1 or greater) "))
print(diceSelect, "sided di(c)e selected")
roll = "y"
while (roll != "n"):
    roll = input("Roll? (y/n): ")
    if (roll == "y"):
        print(random.randrange(1,diceSelect+1,1))
    elif (roll == "n"):
        sys.exit("Goodbye")
    else:
        print("Bad Input")
