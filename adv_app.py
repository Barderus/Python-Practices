'''
    This is a make your own adventure game. 
    Written by Gabriel dos Reis
    Storytelling by Henry Waterman
'''

def main():
    print("Welcome to the Adventure Zone Game! \nAre you ready to play? (yes or no)")
    response = input().lower()
    if response == "yes":
        print("Great! Let's get started.")
        start_game()
    else:
        print("Okay, farewell!")
        

def start_game():
    print("You wake up in the middle of dirty road. You look around you are surrounded by trees. You have no idea how you got here. What do you do? (walk, run, or stay)")
    response = input().lower()
    if response == "walk":
        print("After a few seconds you noticed a wired trap. You are relieved that you took your time and have the chance to just walk over the trap without activing it.")
        cave()
    elif response == "run":
        bobby_trap()
    elif response == "stay":
        killer_attack()
    else:
        print("Invalid input. Let's try again...")
        start_game()

def bobby_trap():
        print("You trip on a wire and a boulder fall from a tree and smashes you. You died.\n\tGAME OVER!") # Bobby trap 1
        #print("You failed to notice a slight difference on the terrain and fell onto a spiky pit. You died.\n\tGAME OVER!") # Bobby trap 2
        #print("You failed to notice that the grass is not in fact grass it is moving, it coming at you with venomous sharp fangs. You died.\n\tGame Over") # Bobby trap 3
        
        play_again()
        

def killer_attack():
    print("The static in the air changes and you feel there is someone or something close. You can hear your heart beating faster and faster. You are not alone anymore.\nA man jumps out of the bushes and lunge himself towards you with a bright and sharp knife.")
    response = input("What would you like to do? (fight / run/ yell !").lower()
    if response == "fight":
        print("Everything happens so fast, before you even realize the man has his knife on your back, it's in, it's out, in and out. The world gets colder and much darker, you feel heavy, but soon you will not feel anything else. You died.")
        play_again()
    elif response == "run":
        print("You use all your body strength to run away from whoever was trying to hurt you.")
        river()
    elif response == "yell":
        print("You duck to side and yell for help, you pray that someone is nearby and can help you, you wish someone was there.")
        x_help()
    else:
        print("You entered an invalid action. Let's try again...")
        killer_attack()
        
def x_help():
    print("The man stomps his way towards you. Maybe you could have enough time to run, or maybe not. But before you have a chance to do anything, another man hurries himself to you. Something in guts tells you can trust him. For now.")
    response = input("Would like to fight alongside the stranger, or signal the stranger to run away or run away from both men? (fight/ run with/ run without)").lower()
    if response == "fight":
        print("The newcomer and you jump onto the man, each standing on one side, dividing his attention. After a few punches, kicks and dodges. You both are able to subdue the man.")
        fight_k()
    elif response == " run with":
        print("You and the newcomer change looks and it is obvious this fight might no go well. Without a single exchange of words, you both run away to somewhere safe. ")
        run_away()
    elif response == "run without":
        print("You look at the newcomer and the man armed with a machete. Who should you trust? Should you trust any of them? Maybe it would be easier by yourself. You legs move withou hesitation, leaving both men behind.")
        run_without()
    else:
        print("Invalid action. Let's try again...")
        x_help()

def river():
    print("You hear from a short distance a familiar sound. The sound of running water, it must be very near. You approach an area close to the river, it seems to be a good locality to build a shelter or to keep pushing forward.")
    response = input("Would you like to build a shelter, try to swim past the river, or walk alongside the river? (shelter / swim / walk)").lower()
    if response == "shelter":
        print("You start collecting branches and leaves nearby, some rocks for fire and wonder where you are or who are you in the first place.")
        y_arrives()
    elif response == "swim":
        print("You decide that maybe would it be best to keep pushing forward. As you have half of waist in the water you notice a few aligators far away from you.")
        answer = input("Would you like to try your luck and swim fast or try to build a little boat? (swim / boat)").lower()
        if answer == "swim":
            print("The aligators move faster than you were expecting. The aligators chomp you before you get to safety. You died.")
            play_again()
        else:
            print("You build a small boat that is safe enough to pass through the river in security.")
    elif response == "walk":
        print("Walking up the river, you note a few small fishes swiming in it. Maybe that could be a source of food, water and safety. It would smarter to investigate further though. As the light starts to fade, you find yourself where the river divides in three branches. Across from the river, you see a big wooden chest.")
        find_rsc_chest()
    else:
        print("Invalid input.Let's try again...")
        river()
    
def y_arrives():
    print("A woman approaches you coming from south of the river. She does not look dangerous or in pain, but you feel prepared to secure your shelter area.")
    response = input("Would you like to waryly talk to the woman, kill her or ask her to join you? (wary / kill / join)").lower()
    if response == "wary":
        print("")
    elif response == "kill":
        print("You advance on her before any other move can bed done. Using all your strength and your speed, you push her towards the river where the hungry aligators are waiting for their next meal.")
    elif response == "join":
        print()
    else:
        print("Invalid input. Let's try again...")
def cave():
    print("You walked for a short period of time without much change in the enviroment until you see a rock formation that appears a cave entrance.")
    response = input("Would you like to enter the cave, go around it or head back? (enter/around/back)").lower()
    if response == "enter":
        inside_cave(0)
    elif response == "around":
        river()
    elif response == "back":
        killer_attack()
    else:
        print("Invalid answer. You must enter either 'enter' or 'around' or 'back'")
        cave()
        
def inside_cave(n):
    print("You carefully make your way inside this dark place. The walls are slimy and the ground is slippery. The little of the sunlight left guide your way thrugh until you find nothing more than a locked door.")
    response = input("Would you like to try to open the door, go back, or use something to open the door? (open/back/unlock)").lower()
    if response == "open":
        print("You try to open the door but the door is very well locked and not brute force seemes to work. You walk back to the surface.")    
        answer = input("You walk back outside and the warm sunlight greets you. Would you like to go back or keep pushing forward? (back/forward)").lower()
        if answer == "back":
            killer_attack()
    elif response == "back":
        print()
    elif response == "unlock":
        if n == 0:
            print("It does not seem you have anything to help you with this task. You make note of the door and head back outside. Would you like to go back or keep going?")
            print(  )
        if n != 0:
            print("The key fits the keyhole perfectly. You wonder, what is ahead of this door.")
            door()
    else:
        print("Invalid input.")
        inside_cave()
        
def door():
    print("You opened the door")
    print("You won the game.")
    
def play_again():
    death = 0
    print("Would you like to play again? (yes or no)")
    response = input().lower()
    if response == "yes":
        death += 1
        start_game()
    else:
        print(f"Thank you for playing the Adventure Zone Game. You died {death} times. I'm sure you'll do better next time... I hope.")
    

main()

