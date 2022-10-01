import json

from CRUD import add_new_entry, delete_phone_number, update_contact_info
from search_engine import search_by, print_search_result
from validation import correct_input, valid_city_or_state, valid_first_or_last_name, valid_phone_number


menu_options = {
    1: "Add new entries",
    2: "Search by first name",
    3: "Search by last name ",
    4: "Search by full name",
    5: "Search by telephone number",
    6: "Search by state",
    7: "Search by city",
    8: "Delete a record for a given telephone number",
    9: "Update a record for a given telephone number",
    0: "Exit the program"
}


def print_menu():
    print("\n")
    for key in menu_options.keys():
        print(key, "--", menu_options[key])
    print("\n")


def option1(phonebook, phonebook_name):
    add_new_entry(phonebook)
    print("Record added to phonebook.\n")
    #print_menu()


def option2(phonebook, phonebook_name):
    searching_for = input("For what first name you are searching for: ")
    search_result = search_by("first_name", searching_for, phonebook)
    print("Your's search result:.\n")
    print_search_result(search_result)
    #print_menu()


def option3(phonebook, phonebook_name):
    searching_for = input("For what last name you are searching for: ")
    search_result = search_by("last_name", searching_for, phonebook)
    print("Your's search result:.\n")
    print_search_result(search_result)
    #print_menu()


def option4(phonebook, phonebook_name):
    searching_for = input("For what full name you are searching for: ")
    search_result = search_by("full_name", searching_for, phonebook)
    print("Your's search result:.\n")
    print_search_result(search_result)
    #print_menu()


def option5(phonebook, phonebook_name):
    searching_for = input("For what phone number you are searching for: ")
    search_result = search_by("phone_number", searching_for, phonebook)
    print("Your's search result:.\n")
    print_search_result(search_result)
    #print_menu()


def option6(phonebook, phonebook_name):
    searching_for = input("For what state you are searching for: ")
    search_result = search_by("state", searching_for, phonebook)
    print("Your's search result:.\n")
    print_search_result(search_result)
    #print_menu()


def option7(phonebook, phonebook_name):
    searching_for = input("For what city you are searching for: ")
    search_result = search_by("city", searching_for, phonebook)
    print("Your's search result:.\n")
    print_search_result(search_result)
    #print_menu()


def option8(phonebook, phonebook_name):
    phone_number = "+380" + correct_input(valid_phone_number, "Enter the phone number: +380-",
                                          "Enter the phone number in next format: +380-XX-XXX-XX-XX. Country code by default +380 (Ukraine)")
    delete_phone_number(phone_number, phonebook)
    #print_menu()


def option9(phonebook, phonebook_name):
    phone_number = "+380" + correct_input(valid_phone_number, "Enter the phone number: +380-",
                                          "Enter the phone number in next format: +380-XX-XXX-XX-XX. Country code by default +380 (Ukraine)")
    update_contact_info(phone_number, "first_name", phonebook)
    #print_menu()


def option0(phonebook, phonebook_name):
    with open(phonebook_name, "w") as phonebook_file:
        json.dump(phonebook, phonebook_file, indent=4)

    raise Exception("Phonebook saved! Exit.")


menu_func = {
    1: option1,
    2: option2,
    3: option3,
    4: option4,
    5: option5,
    6: option6,
    7: option7,
    8: option8,
    9: option9,
    0: option0
}


def main_menu(phonebook, phonebook_name):
    print_menu()

    while True:
        try:
            menu_choice = int(input("Enter your menu choice: "))
            break
        except ValueError:
            print("you typed wrong menu number!")

    menu_func[menu_choice](phonebook, phonebook_name)
