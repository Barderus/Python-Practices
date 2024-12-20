# Need to add input validation
def add_items():
    new_list = []

    while True:
        new = input("What would you like to add to the list? (One at a time. 0 to exit.): ")
        print()
        if new == "0":
            break
        else:
            new_list.append(new)
    return new_list


# At the moment, it is not removing items. Need to check this asap
def remove_items(grocery_list):
    out_list = []

    while True:
        #print(grocery_list)
        out = input("What would you like to remove from the list? (One at at time. 0 to exit.): ")
        print()
        if out == "0":
            break
        elif out in grocery_list:
            #print("Sorry, this item does not exist in the list.")
            print(f"Removing {out} out of the list...\nDone! ")
        else:
            out_list.append(out)
    print(out_list)
    return out_list

# Gotta make a better display of the grocery list
def view_list(grocery_list):
    for index, value in enumerate(grocery_list):
        print(index, value)


# Need to implement to save the list on a file
def save_list():
    pass


# Need to implement load a list from a file
def load_list():
    pass


# Need to implement clear list to start fresh
def main():
    grocery_list = []

    while True:

        choice = int(input("""
                Would you like to:
                    1. View grocery list
                    2. Add items to the grocery list
                    3. Remove items from the grocery list
                    4. Sort list in alphabetical order
                    5. Save list
                    6. Exit  
                        """))
        if choice == 1:
            view_list(grocery_list)

        elif choice == 2:
            new_items = add_items()
            grocery_list.append(new_items)

        elif choice == 3:
            out_list = remove_items(grocery_list)
            print(out_list)
            for item in range(len(out_list)):
                grocery_list.remove(item)

        elif choice == 4:
            grocery_list = grocery_list.sort()

        elif choice == 5:
            save_list(grocery_list)

        else:
            exit()

main()