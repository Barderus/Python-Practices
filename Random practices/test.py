'''
    This is a make your own adventure game. 
    Written by Gabriel dos Reis
    Storytelling by Henry Waterman
'''

def main():
    print("Welcome to the Adventure Zone Game! \nAre you ready to play? (yes or no)")
    response = input().lower()
    if response == "yes":
        print("Great! Let's get started.\n")
        start_game()
    else:
        print("Goodbye!")

def start_game():
    print("You wake up in the middle of dirty road. You look around you are surrounded by trees. You have no idea how you got here. What do you do? (walk, run, or stay)")
    response = input().lower()
    if response == "walk":
        print("You walk and find a house. You knock on the door and someone comes to help you.")
    elif response == "run":
        bobby_trap()
    elif response == "stay":
        mummy_attack()
    

def bobby_trap(perception):
    if perception:
        print("You see a trip wire and avoid it.")
    else:
        print("You trip the wire and a boulder fall from a tree and smashes you.")
        # Game over
        

def mummy_attack():
    print("A mummy comes out of the woods and attacks you. You are dead.")
    play_again()
    

def play_again():
    print("Would you like to play again? (yes or no)")
    response = input().lower()
    if response == "yes":
        start_game()
    else:
        print("Goodbye!")
    

main()