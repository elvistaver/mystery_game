import random


def new_game(name):
    player = {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False,
    }
    return player


def action():
    riddles = [
        {
            "question": (
                "I have keys but open no locks. I have space but no room. You"
                " can enter but you can't go outside. What am I?"
            ),
            "options": "i.A map ii.A keyboard iii.A book",
            "answer": "ii",
        },
        {
            "question": (
                "What has hands but cannot clap, and runs but has no legs?"
            ),
            "options": "i.A clock ii.A river iii.A watchmaker",
            "answer": "i",
        },
        {
            "question": (
                "The more of them you take, the more you leave behind. What are"
                " they?"
            ),
            "options": "i.Shadows ii.Footsteps iii.Minutes",
            "answer": "ii",
        },
        {
            "question": (
                "I create no sound, yet I can mock anyone who speaks to me. I"
                " have no voice, but I speak back only when spoken to first."
                " What am I?"
            ),
            "options": "i.A shadow ii.A reflection iii.An echo",
            "answer": "iii",
        },
        {
            "question": (
                "I am a seed that grows three letters higher, yet I am consumed"
                " to make things expire. I am the boundary of the living, yet I"
                " am found in the dead. What am I?"
            ),
            "options": "i.An ash ii.A bone iii.A grave",
            "answer": "i",
        },
        {
            "question": (
                "I weigh next to nothing, but even the strongest giant cannot"
                " hold me for more than a few minutes. What am I?"
            ),
            "options": "i.A bubble ii.Your breath iii.A secret",
            "answer": "ii",
        },
        {
            "question": (
                "I have no flesh, no feathers, no scales, and no bone. Yet, I"
                " have fingers and thumbs of my own. What am I?"
            ),
            "options": "i.A glove ii.A skeleton iii.A shadow",
            "answer": "i",
        },
        {
            "question": (
                "I am light as a feather, but the longest breath cannot hold"
                " me. What am I?"
            ),
            "options": "i.A bubble ii.Your breath iii.Smoke",
            "answer": "ii",
        },
        {
            "question": (
                "I have cities but no houses, forests but no trees, and water"
                " but no fish. What am I?"
            ),
            "options": "i.A map ii.A painting iii.A globe",
            "answer": "i",
        },
        {
            "question": "What disappears the second you say its name?",
            "options": "i.A secret ii.Silence iii.A shadow",
            "answer": "ii",
        },
    ]

    while True:
        print("Answer 3 correct riddles to take a move.\n")

        # Pick 3 unique random riddles from the list
        selected_riddles = random.sample(riddles, 3)
        all_correct = True

        for index, riddle in enumerate(selected_riddles, start=1):
            print(f"{index}. {riddle['question']}\n  {riddle['options']}")

            while True:
                user_answer = input("  answer: ").strip().lower()
                if user_answer not in ("i", "ii", "iii"):
                    print("  invalid option❗")
                    continue
                else:
                    break

            if user_answer != riddle["answer"]:
                print("  ❌: Try again\n")
                all_correct = False
                break
            else:
                print("  ✅\n")

        # If the player got all 3 right, exit the loop so they can make their move
        if all_correct:
            print("🎉 You solved all 3 riddles! You may now take a move.")
            break

action()



