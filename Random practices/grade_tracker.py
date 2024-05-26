'''
Student Grade Tracker:
    Build a program that allows teachers to input student grades for various assignments and calculate overall grades. 
    You can use dictionaries to store student names and their corresponding grades.
'''

# WORKING ON SAVING THE STUDENT DATA WITH JSON.
# Error: Exception has occurred: TypeError. Object of type Student is not JSON serializable
import json

class Student():
    
    def __init__(self,name, major, gpa):
        self.__name = name
        self.__major = major
        self.__gpa = gpa
        
    # Setters using decorators
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def major(self):
        return self.__major
    @major.setter
    def major(self, major):
        self.__major = major

    @property
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def gpa(self, gpa):
        self.__gpa = gpa

    def __str__(self):
        string = f"{self.__name} {self.__major} {self.__gpa}"
        return string
    
def main():
    try:
        choice = int(menu())
        if choice > 3 or choice < 1:
            raise ValueError
        elif choice == 1:
            create_student()
    except ValueError:
        print("Invalid input. Enter a number between 1 and 3 for the correspond action.")
        choice = int(menu())
    

def menu():
    print("""\n\t
        1. Create Student
        2. Load Student
        3. Calculate grade
        """)
    choice = input()
    return choice

    
def create_student():
    gradebook_dict = {"Students":[], "Assignments":[], "Grades":[]}
    
    while True:
        name = input("Enter student name:\t")
        major = input("Enter student major:\t")
        gpa = input("Enter student gpa\t")
        n = int(input("How many assignments and grades would you like to enter for this student?:\t"))
        stu = Student(name, major, gpa)
        gradebook_dict["Students"].append(stu)
            
        for i in range(n):
            assignment  = input("Enter the assignment name:\t")
            grade = input("Enter the grade in numbers:\t")
            gradebook_dict["Assignments"].append(assignment )
            gradebook_dict["Grades"].append(grade)
        
            i += 1 
        more = input("Would you like to add more students' grades and assignments? (y/n)").lower()
        if more != "y":
            break
        
    save_file(gradebook_dict)
    print("Saving file...")
    

def calc_grade(gradebook_dict):
    
    grade = 0
    if grade > 89:
        print("The student grade is A")
    elif grade > 79:
        print("The Student grade is B")
    elif grade > 69:
        print("The Student Grade is C")
    elif grade > 59:
        print("The Student grade is D")
    else:
        print("The Student grade if F.")

def save_file(gradebook_dict):
    
    with open("gradebook.json", "w") as outfile:
        json.dump(gradebook_dict, outfile)

def load_file():
    
    lst = []
    with open("gradebook.json", "r") as infile:
        data = json.load(infile)
        lst.append[data]
    
    print(lst)


#main()
create_student()