#!/usr/bin/env python3 

print("""You enter a dark room with three doors. 
Do you go through door #1, door #2, or door #3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ============================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door Number 2 Logic =====================
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.\n")
    
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    # == Insanity Logic ======================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":
        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
    else:
        print("N) The insanity rots your eyes into a pool of muck.")
        print("N) Good job!")
# == Door Number 3 logic =======================
if door == "3":

    print("Rick Astley says he's never gonna give you up.")
    print("What do you do?\n")

    print("1. Believe him.")
    print("2. Doubt him.")

    # == Rick logic ============================
    rick = input("-> ")

    if rick == "1":
        print("1) You and Rick dance awkwardly for all eternity in cheesey 80s music video meme glory!")
    elif rick == "2":
        print("2) You don't believe Rick Astley when he says he's never gonna give you up? You heartless monster!")
    else:
        print(f"You still got Rickrolled, and now all of your friends and family are laughing at you!")
        print("Rick continues dancing and singing forever!")
else:
    print("You did not select a door??? Good Call :)")

