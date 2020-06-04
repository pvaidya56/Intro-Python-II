from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Priya', room['outside'], [])
print(room["outside"])

user = input("Directions: \n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n Which direction would you like to travel:" )
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while not user == "q":
    if player1.current_room == "outside":
        if user == "n":
           player1.current_room = room[player1.current_room].n_to
           user = ""
        if user == "s":
            print("nope, try again")
        if user == "e":
            print("nope, try again")
        if user == "w":
            print("nope, try again")

    if player1.current_room == "foyer":
        if user == "n":
           player1.current_room = room[player1.current_room].n_to
           user = ""
        if user == "s":
           player1.current_room = room[player1.current_room].s_to
           user == ""
        if user == "e":
           player1.current_room = room[player1.current_room].e_to
           user == ""
        if user == "w":
            print("foyer west")

    if player1.current_room == "overlook":
        if user == "n":
           print("nope, try again")
        if user == "s":
           player1.current_room = room[player1.current_room].s_to
           user == ""
        if user == "e":
           print("nope, try again")
        if user == "w":
           print("nope, try again")

    if player1.current_room == "narrow":
        if user == "n":
           player1.current_room = room[player1.current_room].n_to
           user == ""
        if user == "s":
           print("nope, try again")
        if user == "e":
           print("nope, try again")
        if user == "w":
           player1.current_room = room[player1.current_room].w_to
           user == ""

    if player1.current_room == "treasure":
        if user == "n":
           print("nope, try again")
        if user == "s":
           player1.current_room = room[player1.current_room].s_to
           user == ""
        if user == "e":
           print("nope, try again")
        if user == "w":
           print("nope, try again")

    print(f"You find yourself in the {player1.current_room}")

    user = input("Options for travel are: \n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n In what direction would you like to travel:" )

print("Game Ended")