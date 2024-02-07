'''
    Tuples intro.
    A tuple is a sequence of values much like a list. The values stored in a tuple can be any type, and they are indexed by integers. 
    The important difference is that tuples are immutable. 
    Tuples are also comparable and hashable so we can sort lists of them and use tuples as key values in Python dictionaries.
'''

# Initialize a tuple
student_tuple = ()
# Adding items to a tuple
student_tuple = "John", "Green", 3.3
print("Content of the student tuple: ", student_tuple)

another_student_tuple = ("Mary", "Red", 3.3)
print("Length of the another student tuple", len(another_student_tuple))

# Adding item to a tuple
student_tuple += (another_student_tuple)
print("Adding the another student tuple to studet_tuple: ", student_tuple)

# Adding tuple to a list
num_list = [1, 2, 3, 4, 5]
num_tuple = (6, 7, 8, 9, 10)
num_list += num_tuple
print("Adding a tuple to a list:", num_list)

# Adding a list to a tuple
new_student = ("Amanda", "Blue", [98,75,87])
new_student[2][1] = 100
print(new_student)

# Unpacking a tuple
first_name, last_name, gpa = new_student
print("Student name: ", first_name)
print("Last name: ", last_name)
print("GPA: ", gpa)
