def intro():
    print("\n\t\t\t<-------- CODE WITH AMINA NOOR -------->\n")
    print("\t\t\t\t<-------- WELCOME TO THE ADVENTURE GAME -------->\n")
    print("\t\tYou Find Yourself In a Dark Forest with two Paths.\n")
    print("Do you want to go left or right?\n")
    
def left_path(inventory):
    print("You walk down the left path and encounter a Wild Bear!\n")
    print("Do you want to fight the bear or run away?")
    choice = input("> ").lower()
    if choice == "fight":
        fight_bear(inventory)
    elif choice == "run":
        run_away(inventory)  
    else:
        print("Invalid Choice. Please try Again.")
        left_path(inventory)
        
def right_path(inventory):
    print("\nYou walk down the right path and find a peaceful village.")
    print("Do you want to explore the village or continue walking?")
    choice = input("> ").lower()
    if choice == "explore":
        explore_village(inventory)
    elif choice == "continue":
        continue_walking(inventory)
    else:
        print("Invalid choice. Please try again.")
        right_path(inventory)

def fight_bear(inventory):
    if "sword" in inventory:
        print("\nYou decide to fight the bear.")
        print("After a fierce battle, you defeat the bear but suffer some injuries.")
        print("You win the game! Congratulations!")
    else:
        print("\nYou try to fight the bear with your bare hands.")
        print("Unfortunately, you are no match for the bear and it defeats you.")
        print("Game Over.")

def run_away(inventory):
    print("\nYou run away from the bear and find a hidden cave.")
    print("Inside the cave, you discover a treasure chest filled with gold.")
    print("You also find a sword.")
    inventory.append("sword")
    print("You add the sword to your inventory.")
    print("You win the game! Congratulations!")

def explore_village(inventory):
    print("\nYou explore the village and meet friendly villagers.")
    print("They offer you food and shelter for the night.")
    if "map" in inventory:
        print("Using the map, you discover a secret path leading to a beautiful garden.")
        print("You win the game! Congratulations!")
    else:
        print("A villager gives you a map.")
        inventory.append("map")
        print("You add the map to your inventory.")
        print("You win the game! Congratulations!")

def continue_walking(inventory):
    print("\nYou continue walking and find a magical portal.")
    print("The portal transports you to a beautiful island.")
    if "amulet" in inventory:
        print("Using the amulet, you activate the portal and are transported to a beautiful island.")
        print("You win the game! Congratulations!")
    else:
        print("You find an amulet on the ground.")
        inventory.append("amulet")
        print("You add the amulet to your inventory.")
        print("You win the game! Congratulations!")

def start_game():
    inventory = []
    intro()
    choice = input("> ").lower()
    if choice == "left":
        left_path(inventory)
    elif choice == "right":
        right_path(inventory)
    else:
        print("Invalid choice. Please try again.")
        start_game() 
        
    print("\n\t\t\t\t<-------- Be Happy😊 -------->\n")
    print("\t\t\t\t<-------- Khuda Hafiz...!👋 ------->\n")  

if __name__ == "__main__":
    start_game()
    

    