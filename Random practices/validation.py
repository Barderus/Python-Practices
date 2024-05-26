'''
    Password, login and card validation
'''
# Import pickle
import pickle
# Import random
import random
# Import date
from datetime import *

def main():
    '''
    # Filename to store login from the user
    filename = "login.dat"
    
    # Open file to store the login in writing binary
    with open(filename, "ab") as outfile:
        # Call the get_password function to get login
        create_login(outfile)
    
    display_login(filename)
    '''
    
    create_card()
    
def create_login(outfile):
    
    # Initialize dictionary
    login_list = []
    print("Login Creation")
    # Get user login and password
    login = input("Enter your login: ")
    
    password = input("Enter your password. \nIt must contains at least one capital letter, one number, and one symbol and more than 7 characters.\n")
    
    validated_pass = validate_password(password)
    
    # Add the log in and password to the dictionary
    login_list.append((login,validated_pass))

    pickle.dump(login_list, outfile)
    print("Login stored with success!")

def display_login(filename):
    print("Displaying login...")
    with open(filename, 'rb') as file:
        try:
            while True:
                login_list = pickle.load(file)
                for login, password in login_list:
                    print(f"\tLogin: {login}\n\tPassword: {password}\n")
        except EOFError:
            pass
    
def valid_length(password):
    # Check if the password has the right amount of characters
    return len(password) >= 7

def capital_letter(password):
    # Check if the password has at least one capital letter
    return any(char.isupper() for char in password)

def has_symbol(password):
    # Check if the password has at least one special symbol
    symbol_set = set("!@#$%^&*(),.?\":{}|<>")
    return any(char in symbol_set for char in password)

def validate_password(password):
    '''
        Must make sure the password follows the following criteria:
            * At least 7 characters
            * At least one capital letter
            * At least one special symbol
    '''
    
    # Loop to validate the password
    while not (valid_length(password) and capital_letter(password) and has_symbol(password)):
        print("Invalid password. It must have at least 7 characters, one capital letter, and one symbol.")
        password = input("Enter your password: ")
    return password

def create_card():
    
    '''
        Get the user name and create a card based on the user information.
    '''
    #card_name = input("Enter the name on the card: ")
    
    #card_number = input(int("Enter your card number: "))
    # Loop to populate the card_code
    code = ""
    while len(code) < 3:
        rand_number = random.randrange(1,11)
        code += str(rand_number)
    print(code)
    
    # Create a random date in 5 years from today
    exp_date = date.today()
    
    # mm/dd/y
    d3 = exp_date.strftime("%m/%Y")
    print(d3)

def create_cv():
    pass

def create_exp_date():
    pass

def create_card_num():
    pass


def validade_card():
        patterns = {
            'visa': r'^4[0-9]{12}(?:[0-9]{3})?$',
            'mastercard': r'^5[1-5][0-9]{14}$',
            'amex': r'^3[47][0-9]{13}$',
            'discover': r'^6(?:011|5[0-9]{2})[0-9]{12}$',
        }

if __name__ == "__main__":
    main()