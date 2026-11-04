



def main():
    while True:
        print()
        print("****MYSTERY ISLAND🌴****")
        print("〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️")
        name=input("Player Name:")
        if name.isdigit():
            print("invalid; use only letters a-z")
            continue
        else:
            print(f"🤗 {name}! Welcome to Mystery Island!")
            break
    print("""Game Task: 
            You wake up on Mystery Island after a storm 
            The lighthouse is dark, the bridge is locked, 
            and a rescue boat will arrive only if you restore the beacon.
            player explores the location to be able to pick the objects to restore the
            beacon, each successful movement is determined by answering 3 correct answer,
            player energy reduces as player take a successful movement or fail the question,
            once the player energy hit 0, the game ends, if player reaches destination before
            the energy hits 0, player wins, if energy finishes before destination, player fails.
            invalid input or option does not reduces energy as you will have to input the correct input.
    """)
            
main()