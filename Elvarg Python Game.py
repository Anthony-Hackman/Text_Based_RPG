# Hack's Text Based Dragon Game c. 2021
# /help for a list of commands in game.

# Definitions and imports
import random
import time

# Player starting room
current_room = 'Living Quarters'
sword = '<=={==================-\n'

# animation for time passing
def pass_time():
    pass_time = '.....\n'
    for char in pass_time:
        print(char, end='')
        time.sleep(.4)


# shows players location when called
def player_status():
    print('\n' + sword, end='')
    print('You are in the {}'.format(current_room))
    print(sword)


# Player action to get an item from the room
def get_item():
    rooms[current_room].keys()
    player_inventory.append(rooms[current_room]['item'])
    rooms[current_room]['item'] = 'NOTHING, what a surprise.'
    inventory()


# displays user inventory
def inventory():
    print('\n>    INVENTORY: ')
    for items in player_inventory:
        print('>   ', items)


# Search the room for items
def player_search():
    print('You cautiously search the ' + current_room + '.')
    pass_time()
    try:
        print('You find ' + rooms[current_room]['item'], '\n')
    except KeyError:
        print('There is nothing more to take in this room.')
        return current_room


# Moving between rooms
def player_move(current_room):
    # Prompted for direction after action = 'go'
    player_direction = input('Which direction would you like to go?\n').lower()
    if current_room == 'Bathrooms':
        if player_direction == '#2':
            pass_time()
            print('oh that\'s nasty')
            pass_time()
            return current_room
    if player_direction == 'north' or player_direction == 'south' or player_direction == 'east' or player_direction == 'west':
        # input validation through try, key error, return current room if invalid
        try:
            if item_check(rooms[current_room][player_direction]) == 1:
                current_room = rooms[current_room][player_direction]
            return current_room
        except KeyError:
            print('There is nothing there.\n')
            return current_room


# RuneScape Easter egg
def easteregg():
    egg = 'This book tells tales of Elvarg doing nothing in a cave from Gilenor.....\n\
It\'s an okay quest.....\n'
    for char in egg:
        print(char, end='')
        time.sleep(.05)
    pass_time()
    print('ALAS!')


# function to print valid inputs to help user
def instructions():
    print('\n', end='')
    print(">       Collect items to defeat the foe in space.")
    print(">       Move command: \"Go\"")
    print(">       Directions: \"North, East, South, West\"")
    print(">       Search room for items: \"Search\"")
    print(">       Add item to inventory: \"Get (or Take)\" \"Item\"")
    print(">       Check inventory: \"Inventory\"")
    print('>       Quit game: \"Quit\"\n')


# RANDOM CHANCE SUCCESS ~30/100 used for chancing the heat in final rooms
def success_check():
    player_number = random.randint(0, 10)
    cpu_number = 7
    if player_number < cpu_number:
        roll_good = 0
    elif player_number >= cpu_number:
        roll_good = 1
    return roll_good


# Random Number Success for no anti fire
def burn_player():
    roll_good = success_check()
    if roll_good == 1:
        pass
    elif roll_good == 0:
        print("The heat of the room is too much for you to handle without any protection. You are burned into ash.")
        print('Play again soon!')
        exit(0)


# Check for Items in inventory for next room requirements
def item_check(look_ahead):
    if look_ahead == 'Southern Docking Station' and 'some Anti Fire Supplements' not in player_inventory:
        burn_player()
        return 1
    elif look_ahead == 'Destroyed Ship' and 'a Deployable Shield' not in player_inventory:
        print('You enter the room with no protection. Elvarg blasts you with a ball of fire, melting your skin off.')
        exit(0)
    elif look_ahead == 'Destroyed Ship' and 'a Deployable Shield' in player_inventory:
        if 'some Anti Fire Supplements' not in player_inventory:
            burn_player()
        if 'a Proton Pack' in player_inventory:
            congrat()
            if 'an Oxygen Tank' in player_inventory:
                oxytank()
                if 'Batteries' in player_inventory:
                    batteries()
                    if 'an Astronaut Meal' in player_inventory:
                        meal()
                        mission_complete()
                    else:
                        no_meal()
                else:
                    no_batteries()
            else:
                no_oxytank()
        return 1
    else:
        return 1


# ANIMATED TEXT INTRODUCTION FOR GAME
def intro():
    title = '>>>--ELVARG--<<<\n\n\n'
    brief = "to the National Space Committee's interplanetary space station.\n" \
            "You are currently tasked with the elimination of the space dragon Elvarg.\n" \
            "We have no time to explain the details of your mission again.\n" \
            "Find a way to eliminate the dragon and repo....... \n" \
            "* Your radio has died *\n\n\n"
    # prints characters with a set speed in time.sleep(*TIME PAUSED*)
    for char in brief:
        print(char, end='')
        time.sleep(.05)
    for char in title:
        print(char, end='')
        time.sleep(.25)


# if player defeats elvarg
def congrat():
    congrat = '\nElvarg lunges toward ' + player_name + '. ' \
              + player_name + ' quickly dodges the swipe and takes aim with their Proton Pack. ' \
                              '\nElvarg shoots a beam of fire toward ' + player_name + '.\n' + player_name + 'yells' \
                                '... ' \
                                '\"DON\'T CROSS THE STREAMS!\" firing their Proton Pack at the beam of fire.\n'
    for char in congrat:
        print(char, end='')
        time.sleep(.05)


# Called if an Oxygen tank in inventory when elvarg is defeated
def oxytank():
    oxytank = player_name + ' quickly notices their oxygen reserves are low...\n' \
                            'Without hesitation, they quickly replace the oxygen tank from their inventory!\n'
    for char in oxytank:
        print(char, end='')
        time.sleep(.05)


# called if no oxygen tank in player inventory after elvarg defeated
def no_oxytank():
    no_oxytank = player_name + ' quickly notices their oxygen reserves are low...\n' \
                 + player_name + ' suffocates to death without reserves...\n\nPlease try again...\n'
    for char in no_oxytank:
        print(char, end='')
        time.sleep(.05)
    exit(0)


# Called if batteries are in inventory when elvarg is defeated
def batteries():
    batteries = player_name + ' retrieves batteries from their inventory and places them in the radio...\n' \
                              'Relieved, ' + player_name + ' calls back to headquarters requesting a rescue pod.\n'
    for char in batteries:
        print(char, end='')
        time.sleep(.05)


# Called if no batteries are present
def no_batteries():
    no_batteries = player_name + ' reaches in their bag to find no batteries for the radio.\n' \
                   + player_name + ' floats in space forever........................\n\nPlease try again...\n'
    for char in no_batteries:
        print(char, end='')
        time.sleep(.05)
    exit(0)


# Called if an Astronaut Meal in inventory when elvarg is defeated
def meal():
    meal = player_name + ' Is starting to feel hungry...\n' \
           + player_name + ' reaches in their inventory and eats an astronaut meal!\n'
    for char in meal:
        print(char, end='')
        time.sleep(.05)


# Called if no meal is present
def no_meal():
    no_meal = player_name + ' Is starting to feel hungry...\n' \
              + player_name + ' starves to death...\n\nPlease try again...\n'
    for char in no_meal:
        print(char, end='')
        time.sleep(.05)
    exit(0)


# called for winning the game
def mission_complete():
    mission_complete = '>\n>                 CONGRATULATIONS ' + player_name + '\nYou have completed your mission ' \
                                                                               'successfully, living another day!\n\n '
    for char in mission_complete:
        print(char, end='')
        time.sleep(.1)
    exit(0)


# ROOM DATA
# Rooms include Valid Directions along with item within room
# intention to give rooms descriptions called when entered for the first time.

rooms = {
    'Living Quarters': {'item': 'The Tales of Elvarg',
                        'south': 'Southern Docking Station',
                        'north': 'Northern Docking Station',
                        'east': 'Kitchen',
                        'west': 'Bathrooms'},
    'Northern Docking Station': {'item': 'an Oxygen Tank',
                                 'east': 'Docked Ship \"GLADIATOR\"',
                                 'south': 'Living Quarters', },
    'Docked Ship \"GLADIATOR\"': {'item': 'Batteries',
                                  'west': 'Northern Docking Station',
                                  'south': '\"GLADIATOR\" Arms Room'},
    '\"GLADIATOR\" Arms Room': {'item': 'a Proton Pack',
                                'north': 'Docked Ship \"GLADIATOR\"'},
    'Kitchen': {'item': 'an Astronaut Meal',
                'west': 'Living Quarters'},
    'Bathrooms': {'item': 'some Anti Fire Supplements',
                  'east': 'Living Quarters'},
    'Southern Docking Station': {'item': 'a Deployable Shield',
                                 'north': 'Living Quarters',
                                 'east': 'Destroyed Ship'},
    'Destroyed Ship': {'item': 'a pile of bones',
                       'west': 'Southern Docking Station'}
}

################################################################################################################

# Set player name
player_name = input('Please enter your name:\n')
# ANIMATION PRINTING PLAYER NAME
for char in '\nWelcome ' + player_name + '...\n':
    print(char, end='')
    time.sleep(.1)
# "#" inserted as a time save for testing purposes below
# INTRO ANIMATION + STORY
# TIME SAVER *** DELETE # WHEN PROJECT COMPLETE ***
intro()
# for testing player_inventory = ['The Tales of Elvarg', 'an Oxygen Tank', 'an Astronaut Meal', 'some Anti Fire
# Supplements', 'a Deployable Shield', 'a Proton Pack', 'Batteries']
player_inventory = []
# Player inventory is empty upon start
# Player Action is initially Defined
player_action = ''
# WHILE LOOP RAN ENTIRE TIME

################################################################################################################

while current_room != 'quit':
    # Prints Status
    player_status()
    player_action = input('Enter your move:\n').lower()
    if player_action == 'quit':
        current_room = 'quit'
        print('Play again soon!')
        continue
    elif player_action == 'help':
        # Assists Player with knowledge
        instructions()
        continue
    elif player_action == 'search':
        # Search the room
        player_search()
        continue
    elif player_action == 'inventory':
        inventory()
        continue
    elif player_action == 'go':
        # Moves Rooms
        current_room = player_move(current_room)
    elif player_action == 'read the tales of elvarg':
        if 'The Tales of Elvarg' in player_inventory:
            easteregg()
    elif player_action == 'show inventory':
        inventory()
    elif player_action == 'get ' + rooms[current_room]['item'].lower() or player_action == 'take ' + \
            rooms[current_room]['item'].lower():
        if rooms[current_room]['item'].lower() == 'nothing, what a surprise.':
            print('How would I even do that?')
        else:
            get_item()

    else:
        print('Invalid input, enter \"help\" for instructions.\n')
