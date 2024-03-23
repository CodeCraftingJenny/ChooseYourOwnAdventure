def start_game():
    print("You wake up in a dark and damp dungeon, your head throbbing. The last thing you remember is being captured by the king's guards." +
    "\nYou must find a way to escape before it's too late!")

    print("You look around the cell and see a rusty iron bar loose in the wall and a small key lying on the floor. What do you do?")

    print("You try to pry open the cell door with the iron bar")
    print("Or you try to reach the key through the bars")

    pry_or_open = input("Choose 'pry' or 'get key'")

    if (pry_or_open.lower() == "pry"):
        pry()
    elif (pry_or_open.lower() == "get key"):
        print("Game over, you have been caught by the guard.")
    else:
        print("Invalid choice")
        start_game()

def pry():
    print("With all your strength, you manage to pry open the cell door. You step into a dimly lit corridor. To your left, you see a staircase leading up. " +
 "\nTo your right, you see a hallway stretching into darkness.")

    left_right = input("Choose 'left' or 'right' ")

    if (left_right.lower() == "left"):
        go_left()
    elif (left_right.lower() == "right"):
        go_right()
    else:
        "Invalid choice, restart the game"
        start_game()

def go_left():
    print("You climb the staircase and find yourself in a storeroom filled with crates and barrels." +
        "\nAt the far end of the room, you see a ladder leading up to a trapdoor.")
    print("Do you search the room for useful items or climb the ladder to the trapdoor?")
    search_climb = input("Choose 'search' or 'climb' ")
    if (search_climb.lower() == "search"):
        print("You find a map of the dungeon and find a secret passageway out!")
    elif (search_climb.lower() == "cimb"):
        print("You climb up the trapdoor that led into the guard's room. You were caught.")
    else:
        print("Invalid choice, restart the game")
        start_game()

def go_right():
    print("You make your way down the dark hallway, felling your way along the" +
          "\n rough stone walls. Suddenly you hear footsteps approaching.")
    hide_fight = input("Choose to 'hide' or 'confront' ")
    if (hide_fight.lower() == "hide"):
        print("You hide behind the pillar, but was caught by the guards. Game Over")
    elif(hide_fight.lower() == "confront"):
        print("It was a fellow prisoner who knows the secret way out. Together you manage to escape.")
    else:
        print("Invalid choice, restart the game")
        start_game()
        


start_game()
