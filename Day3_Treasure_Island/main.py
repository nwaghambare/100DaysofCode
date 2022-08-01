print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!!!")
print("Your mission is to find the TREASURE")

valid = 0
while not valid:
    resp = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
    if resp == 'left' or resp == 'right':
        valid = 1
    else:
        print("Invalid Input. Try Again.")

valid = 0
while not valid:
    if resp == 'left':
        resp = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for '
                     'a boat. Type "swim" to swim across. \n').lower()
        if resp == 'swim' or resp == 'wait':
            valid = 1
        else:
            print("Invalid Input. Try Again.")
            resp = 'left'
    elif resp == 'right':
        print("You fell into a hole. Game Over.")
        valid = 1

valid = 0
while not valid:
    if resp == 'wait':
        resp = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and "
                     "one blue. Which colour do you choose? \n").lower()
        if resp == 'blue' or resp == 'red' or resp == 'yellow':
            valid = 1
        else:
            print("Invalid Input. Try Again.")
            resp = 'wait'
    else:
        print("You get attacked by an angry trout. Game Over.")
        valid = 1

if resp == 'blue':
    print("You enter a room of beasts. Game Over.")
elif resp == 'red':
    print("It's a room full of fire. Game Over.")
elif resp == 'yellow':
    print("You found the treasure! You Win!")
