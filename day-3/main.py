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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Ask for direction, if they don't go left it's game over
direction = input("You're at a crossroad. Where do you want to go? (L/R)")

if direction.lower() != "l":
    print("Fall into a hole.\nGame Over.")

else:
    # Ask for action, if they don't wait is game over
    action = input("You've come to a lake. There is an island in the middle of the lake. (S/W)")

    if action.lower() != "w":
        print("Attacked by trout.\nGame Over.")
    
    else:
        # Ask for a door to go through, if the user chooses anything but yellow is game over
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")

        if door.lower() == "yellow":
            print("You found the treasure.\nYou Win!")
        
        elif door.lower() == "red":
            print("Burned by fire.\nGame Over.")
        
        elif door.lower() == "blue":
            print("Eaten by beasts.\nGame Over.")
        
        else:
            print("You fell into a hole.\nGame Over.")
