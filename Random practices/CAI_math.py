''' Computer Assisted Instruction - Math Quiz'''
import random

def message(n):
    '''
        This receives a string as an argument and returns a message depending if the user got the question right or wrong.
    '''

    praise_list = ["Good job!", "Nice work, pal!", "Keep up the good work!", "Very good!", "I could swear you were Einstein!", "You are a genius!", "It looks like you know what you're doing!"]
    bad_list = ["Sorry, that's not correct.", "Invalid response.", "No. Keep trying though.", "Wrong, next...", "Even a troll could have gotten this right", "Disappointment...", "Why are you even trying?"]
    praise_index = len(praise_list) - 1
    bad_index = len(bad_list) - 1
    rand_index = random.randint(0, praise_index)
    rand_index2 = random.randint(0, bad_index)

    if n == "correct":
        return praise_list[rand_index]
    else:
        return bad_list[rand_index2]


def addition(level):
    '''
        This is the addition function that receives as an argument the level of the questions. Each level apply a multiplier to the random numbers.
        This function prompts the user to answer a simple addition question. 
    '''
    correct_answers = 0
    wrong_answers = 0
    
    while True:
        if correct_answers < 10:
            print(level)
            level == 1
        elif correct_answers < 20:
            print(level)
            level == 2
        elif correct_answers < 30:
            print(level)
            level == 3
        else:
            level == 5

        num1 = random.randint(1,9) * level
        num2 = random.randint(1,9) * level
        result = num1 + num2
        prompt = int(input(f"\nWhat is the result of {num1} + {num2}?: "))

        if prompt == -1:
            print(f"\nThank your playing! Your score is:\nCorrect Answers: {correct_answers}\nIncorrect Answers: {wrong_answers}")
            break
        elif prompt == result:
            correct_answers += 1
            print(message("correct"))
        else:
            wrong_answers += 1
            print(f"{message("incorrect")}. The correct answer is {result}")

def subtraction(level):
    pass

def multiplication(level):
    pass

def division(level):
    pass

def menu():
    pass

def main():
    addition(1)

if __name__ == "__main__":
    main()