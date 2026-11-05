


def new_game(name):

    player={
        "name":name,
        "location":"Beach",
        "energy": 5,
        "inventory":[],
        "game_over":False,
        "won":False
    }
    return player


def action():
    print("answer 3 correct riddles to take a move.")

    print("1. I have keys but open no locks. I have space but no room. You can enter but you can't go outside. What am I?\n  i.A map ii.A keyboard iii.A book")
    answer1=input("answer:")#ii
    print()
    print("2. What has hands but cannot clap, and runs but has no legs?\n  i.A clock ii.A river iii.A watchmaker")
    answer2=input("answer:") #i
    print()
    print("3. The more of them you take, the more you leave behind. What are they?\n  i.Shadows ii.Footsteps iii.Minutes")
    answer3=input("answer:") #ii
    print()
    print("4. I create no sound, yet I can mock anyone who speaks to me. I have no voice, but I speak back only when spoken to first. What am I?\n  i.A shadow ii.A reflection iii.An echo")
    answer4=input("answer:") #iii
    print()
    print("5. I am a seed that grows three letters higher, yet I am consumed to make things expire. I am the boundary of the living, yet I am found in the dead. What am I?\n  i.An ash ii. A bone iii.A grave")
    answer5=input("answer:") #i
    print()
    print("6. I weigh next to nothing, but even the strongest giant cannot hold me for more than a few minutes. What am I?\n  i.A bubble ii.Your breath iii.A secret")
    answer6=input("answer:") #i
    print()
    print("7. I have no flesh, no feathers, no scales, and no bone. Yet, I have fingers and thumbs of my own. What am I?\n i.A glove ii.A skeleton iii.A shadow")
    answer7=input("answer:") #i
    print()
    print("8. I am light as a feather, but the longest breath cannot hold me. What am I?\n  i.A bubble ii.Your breath iii.Smoke")
    answer8=input("answer:") #ii
    print()
    print("9. I have cities but no houses, forests but no trees, and water but no fish. What am I?\n  i.A map ii.A painting iii.A globe")
    answer9=input("answer:")#i
    print()
    print("10. What disappears the second you say its name?\n  i.A secret ii.Silence iii.A shadow")
    answer10=input("answer:") #ii

action()