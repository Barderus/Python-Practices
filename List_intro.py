'''
    Lists are mutable, which means that their elements can be changed unlike tuples. 
    You can add, remove, or search for items in a list.
'''

# How to create a list
my_list = [-45, 6, 0, 72, 1543]
my_list_name = ["Mary", "Smith", 3.57, 2022]

print("Length of the first list: ", len(my_list))
print("Length of the second list: ", len(my_list_name))
print("Accessing the 3rd element of the first list: ", my_list[2])

# Adding items to a list

for number in range(1, 5):
    my_list.append(my_list[number] + 1)
    my_list += "/"
    
print("New length of the first list: ", len(my_list))

# Printing the elements of a list
print("Elements of the first list: ", my_list)

# Using for loop to print the elements of a list
print("Elements of this list: ", end="")
for element in my_list:
    print(element, sep= ", ", end= " ")
    

# List comprehension
def isprime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
print()
comprehension_list = [x for x in range(1, 101)] # Creates a list with the numbers from 1 to 10
even_list = [x for x in range(1, len(comprehension_list)) if x % 2 == 0] # Creates a list with the even numbers from the comprehension_list
odd_list = [x for x in range(1, len(comprehension_list)) if x % 2 != 0] # Creates a list with the odd numbers from the comprehension_list
prime_list = [x for x in range(1, len(comprehension_list)) if isprime(x)] # Creates a list with the prime numbers from the comprehension_list
print("\nList comprehension: ", comprehension_list)
print("\nEven list: ", even_list)
print("\nOdd list: ", odd_list)   
print("\nPrime list: ", prime_list)


