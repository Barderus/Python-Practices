'''
    This is a make your own adventure game. 
    Written by Gabriel dos Reis
    Storytelling by Henry Waterman
'''

def main():
    print("\n\tWelcome to the Adventure Zone Game! \n\tAre you ready to play? (yes or no)")
    response = input().lower()
    if response == "yes":
        print("\tGreat! Let's get started.\n")
        start_game()
    else:
        print("\tOkay, farewell!")
        

def start_game():
    print("You wake up in the middle of dirty road. \nYou look around you are surrounded by trees. You have no idea how you got here. What do you do? (walk, run, or stay)")
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
    print("\nThe static in the air changes and you feel there is someone or something close. You can hear your heart beating faster and faster. \nYou are not alone anymore.\nA man jumps out of the bushes and lunge himself towards you with a bright and sharp knife.")
    response = input("What would you like to do? (fight / run/ yell)\n").lower()
    if response == "fight":
        print("\nEverything happens so fast, before you even realize the man has his knife on your back, it's in, it's out, in and out. \nThe world gets colder and much darker, you feel heavy, but soon you will not feel anything else. You died.")
        play_again()
    elif response == "run":
        print("\nYou use all your body strength to run away from whoever was trying to hurt you.")
        river()
    elif response == "yell":
        print("\nYou duck to side and yell for help, you pray that someone is nearby and can help you, you wish someone was there.")
        x_help()
    else:
        print("You entered an invalid action. Let's try again...")
        killer_attack()
        
def x_help():
    print("The man stomps his way towards you. Maybe you could have enough time to run, or maybe not. \nBut before you have a chance to do anything, another man hurries himself to you. Something in guts tells you can trust him.\nFor now.")
    response = input("Would like to fight alongside the stranger, or signal the stranger to run away or run away from both men? (fight/ run with/ run without)").lower()
    if response == "fight":
        print("\nThe newcomer and you jump onto the man, each standing on one side, dividing his attention. After a few punches, kicks and dodges. You both are able to subdue the man.")
        fight_k()
    elif response == " run with":
        print("\nYou and the newcomer change looks and it is obvious this fight might no go well. Without a single exchange of words, you both run away to somewhere safe. ")
        run_away()
    elif response == "run without":
        print("\nYou look at the newcomer and the man armed with a machete. Who should you trust? Should you trust any of them? Maybe it would be easier by yourself. You legs move withou hesitation, leaving both men behind.")
        run_without()
    else:
        print("Invalid action. Let's try again...")
        x_help()
        
def fight_k():
    print("You and your new friend subdue your attacker. He's laying on the ground, dizzy and very low response.")
    response = input("Would you like to kill your attacker, another blow on the head, or bind him with vines? (kill / blow / bind)").lower()
    if response == "kill":
        kill_k()
    elif response == "blow":
        blow_k()
    elif response == "bind":
        bind_k()
        
def kill_k():
    print("\nThis is area is still under construction. Please, return later.")
    play_again()
    
def blow_k():
    print("\nThis area is still under construction. Please, come back later.")
    play_again()
    
def bind_k():
    print("\nThis area is still under construction. Please, come back later.")

        
def run_away():
    print("""\nYou and your new friend dash through the woods and bushes, panting, heart rate above the roof. You both stop to catch your breath and notice that you are not being followed. It appears so.
            'My...my name...X. My name is X.' Says your while taking deep breaths. ' I suppose you do not remember anything either huh?
            'Not really, I just woke up a little dizzy with no memory of who I am or where am I.' You hear your voice for the first time since you wake up.
            'And what was up with that dude? Why would someone just attack a person like that? He was ready to kill' said X wiping sweat from his forehead
            'I don't know but to be honest, I just want to find a safe place to be for a while and try to understand what is going on.'
            'Where I woke up there was a little hut, maybe we should go that way. It is not far, not really.'
            '""")
    response = input("\nWould you like to follow X, explore more or kill X? (follow / explore / kill)").lower()
    if response == "follow":
        print("\nYou nod and X leads the way to his hutt where it seems to be a safer place to be than in the middle of the woods with a maniac with a machete out there.")
        follow_x()
    elif response == "explore":
        print(""" \n'I think we should explore the ground a little more while we still have some sunlight left.'
                    'Sure! I think that would be helpful to understand where we are.' Replied X allowing you to lead the way.""")
        explore()
    elif response == "kill":
        print("\nYou feel that X cannot be trusted. Specially after a maniac attack you out of the blue. What if you were surround by them with different killing methods? You would be safer if you finish him before he can do anything to you")
        print("\nYou notice a rock on the ground, pretending to be tie you shoes, you grab the rock and smash against X's skull, taking him by surpise. You jump on him and you keep hitting until there is no more response. X is no more.")
        kill_x()
        
def follow_x():
    print("\nThis area is still under construction. Please, come back later.")

def explore():
    print("\nThis area is still under construction. Please, come back later.")

def kill_x():
    print("\nThis area is still under construction. Please, come back later.")

        
        
def run_without():
    print("\nYou run until your legs fail you and you are too tired to keep moving. \nYou heart rate is through the roof, you are panting and having a hard time to grasp for air.")
    print("\nYou keep moving, you must keep distance from those two men. Although you are high alert, it takes you sometime to realize a familiar sound. \nThe sound of water crashing on the shore. You walk towards the direction as your wet your limps, lusting for some water.")
    river_alone() 
    
def river_alone():
    print("\nThis area is still under construction. Please, come back later.")
       
def river():
    print("\nYou hear from a short distance a familiar sound. The sound of running water, it must be very near. \nYou approach an area close to the river, it seems to be a good locality to build a shelter or to keep pushing forward.")
    response = input("\nWould you like to build a shelter, try to swim past the river, or walk alongside the river? (shelter, swim, or walk)\n").lower()
    if response == "shelter":
        print("\nYou start collecting branches and leaves nearby, some rocks for fire and wonder where you are or who are you in the first place.")
        y_arrives()
    elif response == "swim":
        print("\nYou decide that maybe would it be best to keep pushing forward. As you have half of waist in the water you notice a few aligators far away from you.")
        answer = input("Would you like to try your luck and swim fast or try to build a little boat? (swim or boat)\n").lower()
        if answer == "swim":
            print("\nThe aligators move faster than you were expecting. The aligators chomp you before you get to safety. \nYou died.")
            play_again()
        else:
            print("\nYou build a small boat that is safe enough to pass through the river in security.")
            boat()
    elif response == "walk":
        print("\nWalking up the river, you note a few small fishes swiming in it. Maybe that could be a source of food, water and safety. It would smarter to investigate further though. As the light starts to fade, you find yourself where the river divides in three branches. Across from the river, you see a big wooden chest.")
        find_rsc_chest()
    else:
        print("\n\tInvalid input.Let's try again...")
        river()
        
def find_rsc_chest():
    print("\nThis area is still under construction. Please, come back later.")

def boat():
    print("This area is still under construction. Please, come back later.")
    
def y_arrives():
    print("\nA woman approaches you coming from south of the river. She does not look dangerous or in pain, but you feel prepared to secure your shelter area.")
    response = input("Would you like to warily talk to the woman, kill her or ask her to join you? (wary / kill / join)\n").lower()
    if response == "wary":
        print("")
    elif response == "kill":
        print("\nYou advance on her before any other move can bed done. Using all your strength and your speed, you push her towards the river where the hungry aligators are waiting for their next meal.")
        kill_y()
    elif response == "join":
        print("""\n'Oh my god! I'm so happy to find someone!' Says the lady as she approaches with a relief expression on her face.
              'I can't agree more! I thought I was alone in all of this. Would you like to help me build a shelter? There are some leaves and branches around here.'
              'Yeah, yeah, of course!' Said the woman as she started to gather resources. 'I am Y, by the way.'""")
        join_y()
    else:
        print("\n\tInvalid input. Let's try again...")
        y_arrives()

def wary():
    print("\nThis area is stil under construction. Please come back later.")
    play_again()
         
def kill_y():
    print("\nThis area is still under construction. Please, come back later.")
    play_again()

def join_y():
    print("\nThis area is still under construction. Please, come back later.")
    play_again()

        
def cave():
    print("\nYou walked for a short period of time without much change in the enviroment until you see a rock formation that appears a cave entrance.")
    response = input("Would you like to enter the cave, go around it or head back? (enter/around/back)\n").lower()
    if response == "enter":
        inside_cave(0)
    elif response == "around":
        river()
    elif response == "back":
        killer_attack()
    else:
        print("\n\tInvalid answer. You must enter either 'enter' or 'around' or 'back'")
        cave()
        
def inside_cave(n):
    print("\nYou carefully make your way inside this dark place. The walls are slimy and the ground is slippery. The little of the sunlight left guide your way thrugh until you find nothing more than a locked door.")
    response = input("Would you like to try to open the door, go back, or use something to open the door? (open/back/unlock)").lower()
    if response == "open":
        print("\nYou try to open the door but the door is very well locked and no brute force seemes to work. You walk back to the surface.")    
        answer = input("\nYou walk back outside and the warm sunlight greets you. Would you like to go back or keep pushing forward? (back/forward)").lower()
        if answer == "back":
            killer_attack()
    elif response == "back":
        print()
    elif response == "unlock":
        if n == 0:
            print("\nIt does not seem you have anything to help you with this task. You make note of the door and head back outside.")
            answer = input("Would you like to go back or keep going? (back / keep going)").lower()
            if answer == "back":
                killer_attack()
            elif answer == "keep going":
                river()
            else:
                print("\n\tInvalid input. You died.")
                play_again()
            print()
        if n != 0:
            print("\nThe key fits the keyhole perfectly. You wonder, what is ahead of this door.")
            door()
    else:
        print("\n\tInvalid input. Let's try again...")
        inside_cave()
        
def door():
    print("\n\tYou opened the door")
    print("\n\tYou won the game.")
    play_again()
    
def play_again():
    death = 0
    print("\nWould you like to play again? (yes or no)")
    response = input().lower()
    if response == "yes":
        death += 1
        start_game()
    else:
        print(f"\n\tThank you for playing the Adventure Zone Game. You died {death} times. I'm sure you'll do better next time... I hope.")
        exit()
    
main()