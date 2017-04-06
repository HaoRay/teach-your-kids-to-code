# FiveDice.py
import random
# Game loop 
keep_going = True
while keep_going:
    # "Roll" five random dice
    dice = [0,0,0,0,0]          # Set up an array for five values dice[0]-dice[4]
    for i in range(5):          # "Roll" a random number from 1-6 for all 5 dice
        dice[i] = random.randint(1,6)
    print("You rolled:", dice)  # Print out the dice values
    # Sort them
    dice.sort()
    # Check for five of a kind, four of a kind, three of a kind
    # Yahtzee - all five dice are the same
    if dice[0] == dice[4]:
        print("Yahtzee!")
    # FourOfAKind - first four are the same, or last four are the same
    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print("Four of a kind!")
    # ThreeOfAKind - first three, middle three, or last three are the same
    elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
        print("Three of a kind")
    keep_going = (input("Hit [Enter] to keep going, any key to exit: ") == "")

    
    
    
