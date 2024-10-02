import random

options = ("batu", "gunting", "kertas")
player = None
computer = random.choice(options)
playing= True

while playing:
    player= None
    computer=random.choice(options)

    while player not in options:
        player = input("masukan opsi (batu, gunting, kertas):")

    print (f"player : {player}")
    print (f"computer : {computer}")

    if player==computer:
        print ("jir sama")
    elif player == "batu" and computer == "gunting":
        print ("yes menang")
    elif player == "gunting" and computer == "kertas":
        print ("yes menang")
    elif player == "kertas" and computer == "batu":
        print ("yes menang")
    else:
        print ("huu poke")

    if not input ("main lagi kagak?? (y/n)"). lower() == "y":
        if input ("dih nyerah?? (y/n)"). lower() == "y":
            playing =False


print ("makasih ya udah main ^_^")