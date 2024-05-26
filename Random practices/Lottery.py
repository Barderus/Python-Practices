'''
    Lottery game
'''

import random

def main():
    msg = """WELCOME TO THE NEW BEGINNING LOTTERY.\n Choose 10 numbers. If you get:
    10 number correct = 100% of the prize
    9 numbers correct = 90% of the price
    8 numbers correct = 80% of the price
    7 number correct = 100% of the prize
    6 numbers correct = 90% of the price
    5 numbers correct = 80% of the price
    4 number correct = 100% of the prize
    3 numbers correct = 90% of the price
    2 numbers correct = 80% of the price
    1 number correct = 10% of the price"""
    
    price = random.randrange(100000, 999999999, 10000)
    
    print(msg)
    print()
    print(f"This lottery will be rewarding ${price:,.2f}!!!")
    print("Are you ready to test your luck?")
    
    
    user_set = get_user_numbers() # Call this function to get the user's number and store them in the user_set
    lottery_set = get_lottery_num() # Call this function to get the lottery numbers and store in the lottery_set
    match_num = compare_numbers(lottery_set, user_set) # Compare both numbers and return the length of the set's intersection
    get_prizes(match_num, price) # Return the prize

    
def get_user_numbers():
    '''
        This function initializes a set and add 10 numbers to the set through a for loop.
         Added a functionality so no number is being repeated.
    '''
    
    user_numbers = set()
    print("You must choose 10 numbers betwee 1 and 100.")
    for i in range(1, 11):
        user_num = 0
        while user_num in user_numbers or not 1 <= user_num <= 100:
            try:
                user_num = int(input(f"Enter number {i}: "))
                if not 1 <= user_num <= 100:
                    raise ValueError ("You must enter a valid integer between 1 and 100")
            except ValueError:
                print("You must enter a valid integer between 1 and 100")            

        user_numbers.add(user_num) # Add the numbers to the set
    
    return user_numbers
    
def get_lottery_num():
    
    # Initialize the set
    lottery_num = set()
    
    # For loop to choose 10 numbers between 1 and 100
    for i in range(1,11):
        rand_num = random.randrange(1,101)
        while rand_num in lottery_num:
            rand_num = random.randrange(1,101)
    
        lottery_num.add(rand_num)
    
    return lottery_num
    
def compare_numbers(lottery_set, user_set):
    
    print(f"Lottery numbers: {lottery_set}") # Print the lottery numbers
    print(f"Your numbers: {user_set}") # Print the user numbers
    print()
    # Add numbers that both sets have in common in the correct_numbers variable
    correct_numbers = set(lottery_set).intersection(user_set)
    num_correct = len(correct_numbers)
    print(f"You got {num_correct} numbers correct")
    
    return num_correct # Return how many number the sets have in common

    
def get_prizes(match_nums, price):
    
    balance = 0
    prize = 0
    # Check how many numbers were in common to give away the price
    match match_nums:
        case 9:
            prize = price * 0.9
        case 8:
            prize = price * 0.8
        case 7:
            prize = price * 0.7
        case 6:
            prize = price * 0.6
        case 5:
            prize = price * 0.5
        case 4:
            prize = price * 0.4
        case 3:
            prize = price * 0.3
        case 2:
            prize = price * 0.2
        case 1:
            prize = price * 0.1
        case _:
            print("\nI'm sorry, but you got no prize.")
    
    if match_nums > 0:
        print(f"Congratulations! You won ${prize:,.2f}")
    else:
        pass
    
  #  balance += prize
   # return balance
        
    
           
if __name__ == "__main__":
    main()