def menu():
    print("\nWelcome to the addy dump. \n".upper())
    print("1. Add a phone number")
    print("2. Lookup phone number")
    print("3. Print contacts")
    print("4. Delete contact")
    print("5. Quit\n")

"""class contact:
    def __init__(self, first, last, phone):
        self.first = first
        self.last = last
        self.phone = phone
"""

num = {}

menu_choice = 0
menu()
while menu_choice != 5:
    menu_choice = int(input("Select between (1-5) to choose your operation. : \n"))
    if menu_choice == 1:
          first_name = input("Contact first name: ")
          last_name = input("Contact last name: ").casefold()
          phone_number = input("Contact phone number: ")
          print(" ")
          num[last_name] = phone_number
        

    elif menu_choice == 2:
        last_name = input("\nEnter contect's last name: ")
        name = first_name + "\t" + last_name
        if last_name in num:
            print("\nYour contact is:","\n", name,"\n", num[last_name], "\n")

        if last_name not in num:
            print("\nNo contact exist by that name.\n")
            menu()


    elif menu_choice == 3:
        for x in num.keys():
            name = last_name + "\t" + first_name
            print("Name: ",name, "\tNumber: ", num[x] )
        print("\nThese are all your saved contacts.\n")

    elif menu_choice == 4:
        delete_contect = str(input("\nYou wish to delete a contact? [Y/N]: "))
        if delete_contect == "Y".casefold():
            last_name = input("\nPlease enter last name of contact. \n").casefold()
            if last_name in num:
                del num[last_name]
                print("\nYour contact has been successfully deleted. \n\nThat's cold.\n\n")
            else:
                print("\nThere is not contact by said name, thus no deletions were made.\n")
        if delete_contect == "N".casefold():
            menu()


    elif menu_choice == 5:
        quit("""\n\nThanks for using the addy dump. \n\nYou've been bumped.\n\n""")












"""first_name = input("First name: ")
last_name = input("Last name: ")
phone_number = input("Phone number: ")

print("Thank you, your input has been received.")

print("Here it what I recall: ")
person = {
    "first_name": input(first_name),
    "last_name": input(last_name),
    "phone_number": input(phone_number)
}

"""
