""" This is the main file to my data base manager app. The 'stock_data' file will initially populate the 
data base with set items and information.  from this file a user may create, update, view, or delete any
data. """

# Begin with importing necessary modules
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# connect to database
cred = credentials.Certificate("CSE 310 non-Github items\service_key.json")
firebase_admin.initialize_app(cred)

# create shortcut to make life easier
db = firestore.client()

def find_letter_code(col):
    """ This function prepares the user's input to be matched with an item's key."""
    if col == "Hats":
        code = "H"
    elif col == "Shirts":
        code = "S"
    elif col == "Sweat Shirts":
        code = "SW"
    return code

def create_new_item(col,num,code):
    """This function will take a user's input and store it into a dictionary and then push it to the
    data base."""
    
    # put the user into a loop to keep adding until they choose not to.
    add_more = True
    while add_more == True:

        # create empty dictionary
        info = dict()
        key = input("Enter key: ") 
        value = input("Enter value: ") 

        # set key to it's value
        info[key] = [value]
        num = str(num)

        # push dictionary to database
        db.collection(col).document(code + num).set(info, merge=True)

        # display new item for user to preview
        preview = db.collection(col).document(code + num).get()
        print("\n   ** New Item Preview **")
        print(preview.to_dict())

        # ask if they want to continue, if not close the loop
        keep_adding = input("\nAdd more info to new item?(y/n): ")
        if keep_adding.lower() == "n":
            add_more = False

    return

def delete_item(col, item_code):
    """This function will delete the indicated item from the data base."""

    # plug in variables and push delete statement to database
    db.collection(col).document(item_code).delete()
    return

def edit_existing(col, item_code):
    """This function will allow the user to add information to an existing item."""

    # put the user into a loop to keep adding until they choose not to.
    add_more = True
    while add_more == True:

        # create empty dictionary
        info = dict()
        key = input("Enter new key: ") 
        value = input("Enter new value: ") 

        # set key to it's value
        info[key] = [value]

        # update database
        db.collection(col).document(item_code).update(info)

        # display new item for user to preview
        preview = db.collection(col).document(item_code).get()
        print("\n   ** Item Preview **")
        print(preview.to_dict())

        # ask if they want to continue adding, if not close the loop
        keep_adding = input("\nAdd more info to item?(y/n): ")
        if keep_adding.lower() == "n":
            add_more = False
    return

def view_all():
    """ This function will display the entire data base for the user to see. """

    # display all the hats from the data base
    hats = db.collection("Hats").get()
    print("\n   --- Hats ---")
    for hat in hats:
        print(hat.to_dict())
    
    # display all the shirts from the data base
    shirts = db.collection("Shirts").get()
    print("\n   --- Shirts ---")
    for shirt in shirts:
        print(shirt.to_dict())
    
    # display all the sweat shirts from the data base
    sweat_shirts = db.collection("Sweat Shirts").get()
    print("\n   --- Sweat Shirts ---")
    for sweat_shirt in sweat_shirts:
        print(sweat_shirt.to_dict())
    
    return

def main():
    """This is the main function that will run the program."""
    # begin loop to handle user interactions
    view_data = True
    while view_data == True:

        # Display main menu and take input
        print("\nType a category to view or exit\n\n  Hats\n  Shirts\n  Sweat Shirts\n  All (view entire database)\n  Exit\n")
        col = input().capitalize()

        # quit program if user indicates
        if col == "Exit":
            view_data = False
            break
        elif col == "All":
            view_all()
            continue

        # begin loop to process user interaction within specified category
        edit_data = True
        while edit_data == True:
            num = 1

            # display category and receive user input
            category = db.collection(col).get()
            for doc in category:
                print(num, doc.to_dict())
                num += 1
            print("\nType the number to edit/delete an item, new to add an item, or back to return to previous menu.\n")
            edit = input()

            # store variable to handle case where user wants to add an item
            code = find_letter_code(col)
            # store variable 'item_code' with the code and user's input
            item_code = code + edit

            # return to main menu if user indicates
            if edit == "back":
                edit_data = False
                break

            #handle case that user wants to add new item
            elif edit == "new":
                create_new_item(col,num,code)
                continue

            else:
                # display item's information and recieve input
                view_item = db.collection(col).document(item_code).get()
                print(view_item.to_dict())
                choice = input("delete or edit?")

                # case where user wants to delete item: call delete function
                if choice == "delete":
                    delete_item(col, item_code)
                    continue
                
                # case where user wants to edit item:
                elif choice == "edit":
                    edit_existing(col, item_code)
                    continue


# call the main function to begin program.
main()


# thank you message :)
print("Thanks for using the Data Base manager.")

