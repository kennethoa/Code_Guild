__author__ = 'student'

import random

#hit enter to continue function
def wait():
    user_move_on = raw_input("Hit enter to continue")
    if user_move_on == "":
        return
    else: wait()

#enemy choices
def enemy_name():
    random_enemy_options = ["Doghead", "Stinkyfeet", "Dirtbag"]
    random_enemy = random.choice(random_enemy_options)
    return random_enemy

#player class
class Player():
    def __init__(self, name, weapon, pet, costume, health):
        self.player_name = name
        self.player_weapon = weapon
        self.player_pet = pet
        self.player_costume = costume
        self.player_health = health
        self.backpack = []

#not working look for key in backpack
def check_for_key():
    have_key = False
    for items in player_1.backpack:
        if item == "key":
            have_key = True
        return have_key

#enemy class
class Enemy():
    def __init__(self, name, weapon, health):
        self.enemy_name = name
        self.enemy_weapon = weapon
        self.enemy_health = health

#player status
def player_status():
    print "^"*64
    print " "
    print ("Crusader {}:".format(player_1.player_name))
    print ("Your health is {} ".format(player_1.player_health))
    print ("Looking good in that {}".format(player_1.player_costume))
    print ("A {} shall keep you safe".format(player_1.player_weapon))
    print ("And {} has your back".format(player_1.player_pet))
    print " "
    print "^"*64
    print " "
    wait()
    print " "

#player dead
def player_dead_status():
    print "^"*64
    print " "
    print ("Defeated {}:".format(player_1.player_name))
    print ("Your health is {} ".format(player_1.player_health))
    print ("That {} is torn".format(player_1.player_costume))
    print ("The {} is gone".format(player_1.player_weapon))
    print ("{} ran away".format(player_1.player_pet))
    print " "
    print "Sad day"
    print " "
    wait()
    print " "
    print "^"*64
    print "Game Over"
    print "^"*64
    print " "

#room one
def room_one():
    print "The room you enter is dark and smells a little off"
    print " "
    print "There is a lightswitch behind you, a door on the left, and a small hole to the right."
    print " "
    print "-"*64
    print "Choose 1 to turn on the light"
    print "Choose 2 to open the door"
    print "choose 3 to crawl through the hole"
    print "-"*64
    print " "

#room two
def room_two():
    print " "
    print "In this large room you find a telephone"
    print " "
    wait()
    print " "
    answer()

#room two phone answer
def answer():
    answer_phone = raw_input("So, are you going to answer that phone? yes or no? > ")
    if answer_phone == "yes":
        print " "
        print ("Hello, {}, this is your mother. Stop playing games. It is time for dinner.".format(player_name))
        print " "
        wait()
        random_enemy = enemy_name()
        print " "
        print ("Oh, no! {} is coming for you!".format(random_enemy))
        print " "
        fight_or_flight()

    else:
        print " "
        print "You must answer the phone. It is your mother calling."
        print " "
        wait()
        print " "
        print ("Hello, {}, this is your mother. Stop playing games. It is time for dinner".format(player_name))
        print " "
        wait()
        random_enemy = enemy_name()
        print " "
        print ("Oh, no! {} is coming for you!".format(random_enemy))
        print " "
        fight_or_flight()

#player creating functions starts at full health

player_health = 100
print " "
print "Welcome to the Dungeon of Doom"
print " "

#player name create
player_name = raw_input("Tell me your name > ")
print " "

print ("Welcome, {}. hahaha".format(player_name))
print " "

#player weapon choice
print "To your left, you will notice three items on the table:"
print " "

print "Item 1 is a can of spraypaint."
print "Item 2 is a horseshoe."
print "Item 3 is a flashlight."
print " "

player_weapon = raw_input("Which item do you choose? > ")
if player_weapon == "1":
    player_weapon = "can of spraypaint"
elif player_weapon == "spraypaint":
    player_weapon = "can of spraypaint"
elif player_weapon == "2":
    player_weapon = "horseshoe"
elif player_weapon == "3":
    player_weapon = "flashlight"
else:
    player_weapon = "unidentified object"
print " "

print ("A {} is your weapon of choice, {}.".format(player_weapon, player_name))
print " "

#sidekick choice
player_pet = raw_input("Do you say you are a skunk person or a turtle person? > ")
if player_pet == "turtle":
    player_pet = "Myrtle"
elif player_pet == "skunk":
    player_pet = "Mr Funk"
else:
    player_pet = "a rock"
print " "
print ("{} is your new sidekick!".format(player_pet))
print " "

#costume choice
print "pick a color...."
player_costume = raw_input("pink? orange? black? > ")
if player_costume == "pink":
    player_costume = "tutu"
elif player_costume == "orange":
    player_costume = "life jacket"
elif player_costume == "black":
    player_costume = "ninja suit"
else:
    player_costume = "birthday suit"
print " "

print ("That {} looks amazing on you, {}.".format(player_costume, player_name))
print " "

#class create for first player
player_1 = Player(player_name, player_weapon, player_pet, player_costume, player_health)

#exit
def exit():
    print ("Farewell, {}. You truly are a coward.".format(player_name))
    player_1.player_health = 0
    print " "
    player_dead_status()
   # break

#fight
def fight_or_flight():
    fight_or_exit = raw_input("What's your choice....fight?.....or flight? > ")
    print " "
    if fight_or_exit == "fight":
        print """Let's do this!"""
        print " "
        wait()
        print " "
        player_1.player_health = 0
        print " "
        print "Ooops, you died"
        print " "
        wait()
        print " "
        player_dead_status()
    else:
        print " "
        print ("Too slow, {}".format(player_name))
        print " "
        wait()
        print " "
        exit()

#key hiding spot
def hole():
    print "You are now in a small hole"
    print " "
    print "That sharp pain in your side is the key that you just found!"
    print " "
    player_1.backpack.append('key')
    print "Use your new key to unlock the door"
    print " "
    wait()
    room_two()
    print " "

print player_status()
print " "
room_one()

action_one = raw_input("Which option do you choose? > ")
print " "


if action_one == "1":
    enemy_select = int(input("Before you turn on the light.... pick a number between 1 and 10 > "))
    if enemy_select <= 3:
        random_enemy = enemy_name()
        print " "
        print ("Oh, no! {} is waiting for you!".format(random_enemy))
        print " "
        fight_or_flight()
    else:
        print " "
        print "This room is empty"
        print " "
        print wait()
        print " "
        print "-"*64
        print "Choose 2 to open the door"
        print "choose 3 to crawl through the hole"
        print "-"*64
        print " "
        option_one = raw_input("Which option do you choose? > ")
        if option_one == "2":
            room_two()
        elif option_one == "3":
            hole()
        else:
            print "please choose an option"
            print " "


elif action_one == "2":
    print "You do not have the hidden key, hidden in the hole"
    print " "
    print "Go to the hole!"
    print " "
    wait()
    print " "
    hole()

elif action_one == "3":
    hole()

