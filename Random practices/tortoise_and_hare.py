"""
    Tortoise: 50% fast pod - 3 squares ahead
              20% slip     - 6 squares back
              30% slow pod - 1 square to the right

    Hare:     20% sleep     - No move at all
              20% big hop   - 9 Squares to the right
              10% big slip  - 12 squares back
              30% small hop - 1 square ahead
              20% small slip - 2 squares back
"""

import random


def tortoise_move():
    move = 0
    percentage = random.randint(1, 10)

    if percentage <= 5:
        print("The tortoise rushes with its little pawn.")
        move += 5
    elif 6 <= percentage <= 7:
        print("The tortoise slips and fall behind")
        move -= 6
        if move < 0:
            move = 1
    elif 8 <= percentage <= 10:
        print("The tortoise is catching its breath while slow-walking.")
        move += 1
    return max(1,move)


def hare_move():
    move = 0
    percentage = random.randint(1, 10)

    if percentage <= 2:
        print("The hare finds a cozy place to lay down and take a little nap.")
    elif 3 <= percentage <= 4:
        print("The Hare gets a huge hop and gain lots of terrain!")
        move += 9
    elif percentage == 5:
        print("The hare slips and falls behind. It looks like the hare is taking a while to recuperate.")
        move -= 12
    elif 6 <= percentage <= 8:
        print("The hare hops around gaining some terrain.")
        move += 1
    else:
        print("The hare slips and lose some of the advancement.")
        move -= 2
    return max(1,move)


def game_on():
    win = 70
    t_moves = 0
    h_moves = 0

    while True:
        t_moves += tortoise_move()
        print(f"Tortoise position: {t_moves}")
        h_moves += hare_move()
        print(f"Hare position: {h_moves}")
        print()
        if t_moves >= 70 or h_moves >= 70:
            break
    
    if t_moves >= win and h_moves >= win:
        print("It's a tie!")
    elif t_moves >= win:
        print(f"Tortoise wins! Final position: {t_moves}")
    else:
        print(f"Hare wins! Final position: {h_moves}")

            
    
    print(f"Hare was in postion {h_moves} and tortoise in postion {t_moves}")
    



def main():
    print("""This is the famous tortoise and hare race with a little modifications. """)
    print("Are you ready?")
    print("""   \n\t\tBANG!!! 
                AND THEY ARE OFF !!!!!\n""")
    game_on()


main()
