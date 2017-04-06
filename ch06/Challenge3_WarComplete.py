# WarComplete.py
import random
suits = ['clubs', 'diamonds', 'hearts', 'spades']
faces = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
         'ten', 'jack', 'queen', 'king', 'ace']
keepGoing = True
hands = 0
ties = 0
my_score = 0
your_score = 0
while keepGoing and (hands < 26):
    hands += 1
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print ("I have the", my_face, "of", my_suit)
    print ("You have the", your_face, "of", your_suit)
    if faces.index(my_face) > faces.index(your_face):
        print ("I win!")
        my_score += 1 + ties
        ties = 0
    elif faces.index(your_face) > faces.index(my_face):
        print ("You win!")
        your_score += 1 + ties
        ties = 0
    else:
        print ("It's a tie!")
        ties += 1
    print ("Score: Computer",my_score, ", You",your_score)
    answer = input("Hit [Enter] to keep going, any other keys to exit: ")
    keepGoing = (answer == "")
print("Game Over")
if my_score > your_score:
    print ("I win the game!")
elif your_score > my_score:
    print ("You win the game!")
else:
    print ("It was a tie game!")
