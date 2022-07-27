print("Welcome to Treasure Island. \nYour mission is to find the Treasure \n")

option1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'? \n").lower()

if option1 == "left":
    option2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    if option2 == "wait":
        option3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if option3 == "red":
            print("It's a room full of fire. Game Over.")
        elif option3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif option3 == "yellow":
            print("You win!")
        else:
    else:
      print("You get attacked by an angry trout. Game Over.")
  else:
    print("You fell into a hole. Game Over.")
