'''
    This is a make your own adventure game. 
    Written by Gabriel dos Reis
    Storytelling by Gabriel dos Reis
    Little helper: Henry Waterman
    
    
    X = Mad Scientist - Actually evil
    Y = Lady she has access to an open chest with tools and camping supplies
    Z = Helper scientist, has a key to open the chest that has a key to open the cave's door
    K = Killer 
'''

import random
death = 0

def main():
    print("\n\tWelcome to the Adventure Zone Game! \n\tAre you ready to play? (yes or no)")
    response = input().lower()
    if response == "yes":
        print("\tGreat! Let's get started.\n")
        start_game()
    else:
        print("\tOkay, farewell!")
        

def start_game():
    print("\nYou wake up in the middle of dirty road. \nYou look around you are surrounded by trees. You have no idea how you got here. What do you do? (walk, run, or stay)")
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
        print("\nThe newcomer and you jump onto the man, each standing on one side, dividing his attention. After a few punches, kicks and dodges.")
        blow_k()
    elif response == "run with":
        print("\nYou and the newcomer change looks and it is obvious this fight might no go well. Without a single exchange of words, you both run away to somewhere safe. ")
        run_away()
    elif response == "run without":
        print("\nYou look at the newcomer and the man armed with a machete. Who should you trust? Should you trust any of them? Maybe it would be easier by yourself. You legs move withou hesitation, leaving both men behind.")
        run_without()
    else:
        print("Invalid action. Let's try again...")
        x_help()
    
def kill_k():
    print("\nYou and the other man take turns smacking the man down, using your fists, the machete and rocks around you. You made sure he will not breath ever again.")
    print("""\t' We did the right thing, it was either him or us.' Said the man next to you, cleaning his hands from the blood. ' I'm X by the way.'
          \t'I'm...I'm... Sorry, I don't know my name... Actually, I don't remember anything.'
          \t'That's okay, I'm sure it will come back to you, I just remembered my name a few minutes ago. What should we do with him?'
          \nYou looked at the messed up body of the man and wonder what to do next. 
          """)
    response = input("\nPerhaps you could take the knife to protect yourself, perhaps you could check his body for the why of the attack, or you could leave it behind and walk away. (knife, loot, or walk away)").lower()
    if response == "knife":
        print("\nYou secure the machete in your hands. It emanates power, it emanates security. You have an upper hand now.")
        take_machete()
    elif response == "loot":
        print("\nYou approach the body, and with little disgust you check the man's pockets and clothes. Only to find a small folded piece of paper with the following instructions written:")
        print("\t 'EVERYONE HERE IS YOUR ENEMY. KILL THEM BEFORE THEY KILL YOU!")
        loot_k()
    elif response == "walk away":
        print("\nYou decided to leave the body to rot in peace. You look at X and with no need of other words, understand what you mean to do.")
        walk_with_x()
    else:
        print("\nIt seems you entered an invalid action. Please, try again.")
        kill_k()
        
def take_machete():
    print("\nYou look at your newfound friend who still grasps for air.")
    print("""
          \n'We did the right thing, yeah, we did it!' Said X stepping back.
        'Like you said, it was either us or him. Let's get out of here.' You said coldly still thinking about the blows you gave. Was it really the best thing to do? ' I appreciate you coming for help, if it wasn't for you, I would be very dead now.
        'i was close when I heard you yelling for help, I couldn't resist to stay put, I had to do something.' He replied. 'Do you have any idea where we could be?'
        You look around and let the sun light warm your skin and breath the fresh air of the forest. You had to be somewhere warm and tropical. 'Somewhere south.' You simply reply.
        'You are probably right. Do you wanna go to the river and wash up? I think I can guide us if I don't get my direction messed up.'` 
          """)
    response = input("Would you like to follow X to the river, or perhaps ? (finish, walk away, or attack?)").lower()
    if response == "finish":;
    
    
    play_again()

def loot_k():
    print("This area is still under construction. Please, come back later!")
    play_again()

def walk_with_x():
    print("This area is still under construction. Please, come back later!")
    play_again()
    
def blow_k():
    print("\nYou hit the man right on the side of his head sending him right to the ground. His chests move up and down slowly. He is under your mercy now.")
    print(""" 'You got him!' Said your helps. 'I am X by the way!'
          'I was scared for my life! I am...I... I don't remember my name...' You said with disappointment and confusion.
          ' That's okay I just remembered my name a few minutes ago. What are we gonna do to him now?""")
    response = input("You look at the man still alive on the ground. Would you like to let him live and run away, finish him off, or bind the man? (run away, finish, or bind)").lower()
    if response == "walk away":
        run_away()
    elif response == "finish":
        kill_k()
    elif response == "bind":
        bind_k()
    

def bind_k():
    print("\nYou and X work together on fetching some vines and tying them up so they turn into a big rope. \nX bring the unconcious man to the tree and you tie him up against the trunk. \nYou are surpised on how natural it was for you to complete the knot.")
    print("""
          'What should we do next? Asked X by your side looking at the man.'
          ' First let's secure the knife so he won't use it to 
          """)

        
def run_away():
    print("""\nYou and your new friend dash through the woods and bushes, panting, heart rate above the roof. You both stop to catch your breath and notice that you both are alone.\nOr It appears so.
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
    play_again()
       
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
    print("\nYou walk without much change in scenario around you. The cold breeze of dusk starts to pick up when you notice a small box on the other side of the river. It looks like a kid toy chest. You wonder what could be inside of it.")
    response = input("You could try to swim across the river to reach the chest, or you could ignore the chest and keep walking, or you could go back. (swim, walk, go back)").lower()
    if response == "swim":
        swim_to_chest()
    elif response == "walk":
        walk_to_x()
    elif response == "go back":
        river()
    else:
        print("\nInvalid Input. Why don't we try again...")
        find_rsc_chest()
        
def swim_to_chest():
    print("\n\t This area is still under construction. Come back later")
    play_again()

def walk_to_x():
    print("\n\t This area is still under construction. Come back later")
    play_again()
    
def boat():
    print("You head back and start looking what you could use to cross the water without triggering the aligators. Perhaps if you get some branches together and tie them with vines you could have at least something that floats.")
    print("It's a hard work to collect the big branches and tie them together, it took some of your attention away and you did not realize what was watching you.\n You see a man behind a tree watching you with a knife drawn.")
    print("""
          \n'Hey hey hey, you scared me dude!' You said as you feel your heart beating fast and faster, your mucles tightning up and something inside telling you to run.
          'Another one. This time you won't get away!' Said the man with a monotonous tone, as if he was bored.""")
    response = input("You don't have much time to think here. Will you run for your life? Jump in the river and try to swim across? Or prepare yourself to fight?").lower()
    if response == "run":
        run()
    elif response == "jump":
        jump_river()
    elif response == "fight":
        k_attack_river()
    else:
        print("\nInvalid input. Let's try again...")
        boat()
        
def run():
    print("\n\t This area is still under construction. Come back later")
    play_again()
    
def jump_river():
    print("\n\t This area is still under construction. Come back later")
    play_again()
    
def k_attack_river():
    print("\n\t This area is still under construction. Come back later")
    play_again()    
    
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
        y_join()
    else:
        print("\n\tInvalid input. Let's try again...")
        y_arrives()

def wary():
    print("""\n
          'Stay right where you are!' You yelled at the person standing your ground.
          'Hey hey hey! It's okay, I mean no harm. I was dumped into this place with no memories. Please, can you tell me where I am?' She plead with her hands up
          'I don't know. But I'm sure we're not alone in here.' You reply lowering you guard. 'I also have no memories.'
          'Geez, I wonder what happened to us. I see you trying to build something there. Where I woke up there was a litte camp already made. You could find shelter there.' She lowered her hands and walked in your direction.  
          """)
    response = input("\nWould you like to join her, refuse her invitation, or kill her as she approaches you? (join, refuse, kill)").lower()
    if response == "join":
        print("\nYou wonder for a moment if you would be able to build anything with the material you had in the first place. A camp sounds good after all.")
        join_y()
    elif response == "refuse":
        print("\nYou do not know this woman yet, she might be lying. She might know what is going on here. Perhaps trusting her at first sight would not be a good idea.")
        refuse_y()
    elif response == "kill":
        print("\nYou advance on her before any other move can bed done. Using all your strength and your speed, you push her towards the river where the hungry aligators are waiting for their next meal.")
        kill_y()
        
def refuse_y():
    print("""\n
          'I woke up in the middle of nowhere without nowing who I am and who to trust. Maybe we should stay away until I figure out what is going on.'
          'I understand, but together we can do some much more! Look, I'm just really happy I found someone and I'm not alone in here' 
          'You should go now. Sorry, but I need to understand a few things before being all nice and friendly.'
          'Well, if you go back this way, there is a passage between the shore so you don't need to swim. From there, you can see some hill formations, and there's where I will be if you need help or anything.'
          'Thank you, be careful out there.' You say as she turn around and head back to wherever she came from. 
          """)
    response = input("\nYou are alone again. Would you like to return to build your shelter, follow Y or walk around a little more? You do notice it is starting to get dark (shelter, follow, walk)").lower()
    if response == "shelter":
        build_shelter()
    elif response == "follow":
        follow_y()
    elif response == "walk":
        find_rsc_chest()
    print()
    
def build_shelter():
    print("\n\t This area is still under construction. Come back later")
    play_again()
    
def follow_y():
    print("\n\t This area is still under construction. Come back later")
    play_again()
            
def kill_y():
    print("\nYou watch as the aligators jump on her to chomp every single piece, leaving nothing behind when they submerge again.")
    print("\nYou sense that the aligators had enough food for today and it might be safe to swim across.\n Without the interference of that person you could finish your shelter before nightfall.\nThe aligators come back during the night to finish you, so perhaps going back to woods might be safer.")
    response = input("\nWould you like to swim across the river, build the shelter, or go back to the woods? (swim, shelter, or go back)").lower()
    if response == "swim":
        swim_across()
    elif response == "shelter":
        shelter()
    elif response == "go back":
        killer_attack()
    else:
        print("\nInvalid input. Why don't we try again?")
        kill_y()
        
def swim_across():
    print("\nThis area is still under construction. Please, come back later.")
    
def shelter():
    print("\nThis area is still under construction. Please, come back later.")


def join_y(): # Join Y to go to her camp
    print("\n""""
          'That sounds good to me. How do we get back to your camp?' You say while dropping the materials.
          'It's not far! It's on the other side of the river though.'
          'I understand.' You look at her clothes but none of them look very wet. 'Should we just swim across here?'
          'Oh, I wouldn't personally cross the river here, on my hike to her I saw some nasty things in there.' She looked back before continuing. 'There is a passage back there where the river is pretty shallow to cross.'
          'Okay, sounds good! Why don' you lead the way?'
          She takes the lead and you follow right behind her.
          """)
    print("""
          \n on the short duration of your hike to the river you learn a few things from that lady, first, her name is Y. It sounds unusuall and short, but you go along with.
          She, just like you, wake up on the middle of these clearing, by some hills without remembering anything about herself or knowing where she was. Just like you.
          By the clearing there was a chest, once she opened it was full of camping gear. Without much trouble, she was able to make small camp. 
          She then started to walk around trying to find food and water, until she found you.
          """)
    response = input("Would you like to tell her your own story, ask more questions, or kill her now ? (story, questions or kill?)")
    if response == "story":
        print("After she finishes sharing what she remembers, you go ahead and starts to describe to her everything you remember to this point.")
        tell_story()
    elif response == "questions":
        print("You wonder how she built the camp without any help and remembering everything. There might be more she is not telling you.")
        ask_questions()
    elif response == "kill":
        kill_y()
        
def tell_story():
    print("\n\t This area is still under construction. Come back later")
    play_again()
    
def ask_questions():
    print("\n\t This area is still under construction. Come back later")
    play_again()
            
def y_join(): # Y joins you to build the shelter
    print("""\n
          """)
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
        print("\nYou try to open the door but the door is very well locked and no brute force seems not to work. You walk back to the surface.")    
        answer = input("\nYou walk back outside and the warm sunlight greets you. Would you like to go back or keep pushing forward? (back/forward)").lower()
        if answer == "back":
            killer_attack()
    elif response == "forward":
        river()
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
    death = 1
    print("\nWould you like to play again? (yes or no)")
    response = input().lower()
    if response == "yes":
        death += 1
        start_game()
    else:
        print(f"\n\tThank you for playing the Adventure Zone Game. You died {death} times. I'm sure you'll do better next time... I hope.")
        exit()
    
main()