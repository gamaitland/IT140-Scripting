#Gabrielle Maitland
# Sample function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands

    # In this solution, the player’s status would be shown in a separate function.
    # You may organize your functions differently.
    # Show the player the different commands they can enter (such as “go North”, “go West”, and “get [item Name]”).
    # Show the player’s status by identifying the room they are currently in,
    # showing a list of their inventory of items, and displaying the item in their current room.

    print("SLYR: A Text Adventure Game")
    print("Welcome to SLYR. After years of hard work as a demon slayer in training, "
          "it is now time for you to pass your final test.")
    print("Collect 6 items to defeat your Headmaster or die trying.")
    print("Travel throughout 8 rooms using the commands: North, East, South, West.")
    print("To add an item to your inventory, type Collect 'item name'.")
    print("This game is cAsE sEnSiTiVe!")


# A dictionary linking a room to other rooms
# and linking one item for each room except the Start room (Great Hall) and the room containing the villain
rooms = {
    'Main Dojo': {'South': 'Basement', 'North': 'Armory', 'East': 'My Quarters', 'West': 'Courtyard'},
    'My Quarters': {'North': 'Masters Quarters', 'West': 'Main Dojo', 'item': 'Healing Potion'},
    'Masters Quarters': {'South': 'My Quarters', 'item': 'Ball and Chain'},
    'Sandpit': {'West': 'Armory'},  # villain
    'Armory': {'East': 'Sandpit', 'South': 'Main Dojo', 'item': 'Sword'},
    'Courtyard': {'East': 'Main Dojo', 'item': 'Smoke Bomb'},
    'Basement': {'North': 'Main Dojo', 'East': 'Attic', 'item': 'Chest Plate'},
    'Attic': {'West': 'Basement', 'item': 'Poison Mask'}
}


def main():
    show_instructions()
    current_room = 'Main Dojo'
    command = 'None'
    inventory = []

    while command != 'Exit':
        print()
        print('You are here: ', current_room)
        print("Inventory:", inventory)
        room_dict = rooms[current_room]
        if "item" in room_dict:
            item = room_dict["item"]
            if item not in inventory:
                print("You see a", item)
                user_input = input("Enter 'Collect *item name*: ")
                if user_input == "Collect " + item:
                    print(item, "collected")
                    inventory.append(item)
                else:
                    print("Invalid entry")
                continue

        command = input('Enter a direction or Exit game: ')
        if command == 'Exit':
            current_room = 'Exit'
            print('Thanks for playing!')

        elif command in rooms[current_room]:
            current_room = rooms[current_room][command]
            if current_room == "Sandpit":
                if len(inventory) == 6:
                    print("Uh oh! You have crossed paths with your Headmaster!"),
                    print("Luckily, you have successfully acquired all of the items, allowing for a flawless victory."),
                    print("You win, Slayer!!!")
                    break
                else:
                    print("Uh oh! You have crossed paths with your Headmaster! "),
                    print("You have failed to acquire all of the items"),
                    print("necessary to defeat your Headmaster before running into them. "),
                    print("You LOSE."),
                    break

        else:
            print('You cannot go that way!')


main()

###
