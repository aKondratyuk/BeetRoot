import json
import os

from validation import correct_input, valid_city_or_state, valid_first_or_last_name, valid_phone_number


def add_new_entry(phonebook: dict):
    phone_number = "+380" + correct_input(valid_phone_number, "Enter your phone number: +380-",
                                          "Enter your phone number in next format: +380-XX-XXX-XX-XX. Country code by default +380 (Ukraine)")

    first_name = correct_input(valid_first_or_last_name, "Enter your name: ",
                               "Name should be less than 50 characters and contains only letters").lower().title()

    last_name = correct_input(valid_first_or_last_name, "Enter your last name: ",
                              "Last name should be less than 50 characters and contains only letters").lower().title()

    full_name = first_name + " " + last_name

    state = correct_input(valid_city_or_state, "Enter your state: ").strip()
    city = correct_input(valid_city_or_state, "Enter your city: ").strip()

    phonebook[phone_number] = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "address": {
            "state": state,
            "city": city
        },
    }


def delete_phone_number(phone_number: str, phonebook: dict):
    try:
        del phonebook[phone_number]
        print(f"Contact with phone number {phone_number} deleted.")
    except KeyError:
        print("Phone number is not exists!")


def update_contact_info(phone_number: str, key: str, phonebook: dict):
    try:
        phonebook[phone_number]
    except KeyError:
        print("Phone number is not exists!")

    if key == "phone_number":
        temp_contact_info = phonebook.get(phone_number)
        delete_phone_number(phone_number, phonebook)

        phone_number = "+380" + correct_input(valid_phone_number, "Enter your phone number: +380-",
                                              "Enter your phone number in next format: +380-XX-XXX-XX-XX. Country code by default +380 (Ukraine)")
        phonebook[phone_number] = temp_contact_info

    if key in ["state", "city"]:
        new_value = correct_input(valid_city_or_state, f"Enter your {key}: ").strip()
        phonebook[phone_number]["address"][key] = new_value

    if key in ["first_name", "last_name"]:
        new_value = correct_input(valid_first_or_last_name, f"Enter your {key.replace('_', ' ')}: ",
                                  "Name should be less than 50 characters and contains only letters").lower().title()
        phonebook[phone_number][key] = new_value

        contact = phonebook[phone_number]
        contact["full_name"] = contact["first_name"] + " " + contact["last_name"]

    if key == "full_name":
        new_first_name = correct_input(valid_first_or_last_name, f"Enter your first name: ",
                                       "Name should be less than 50 characters and contains only letters").lower().title()

        new_last_name = correct_input(valid_first_or_last_name, f"Enter your last name: ",
                                      "Name should be less than 50 characters and contains only letters").lower().title()

        contact = phonebook[phone_number]
        contact["first_name"] = new_first_name
        contact["last_name"] = new_last_name
        contact["full_name"] = contact["first_name"] + " " + contact["last_name"]


def open_phonebook(phonebook_name):
    with open(phonebook_name, "r+") as phonebook_file:
        try:
            phonebook = phonebook_file.read()
            phonebook = json.loads(phonebook)
        except json.JSONDecodeError:
            phonebook = {}

    return phonebook


def init_phonebook(PATH_TO_PHONEBOOKS_FOLDER):
    files = os.listdir("phonebooks")
    num_files = len(files)

    if not len(files):
        print("There are no phonebooks if folder.")
        print("Program automatically will create phonebook.json by default.")

        with open(PATH_TO_PHONEBOOKS_FOLDER + "phonebook.json", "w") as phonebook_file:
            pass

        phonebook = open_phonebook(PATH_TO_PHONEBOOKS_FOLDER + "phonebook.json")
        return phonebook, "phonebook.json"

    print("Choose the phonebook to start the program:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file};")

    while True:
        try:
            phonebook_choice = int(input("\nEnter phonebook file number: "))
            break
        except ValueError:
            print("You need to type the number.")

    while not 1 <= phonebook_choice <= num_files:
        phonebook_choice = input("You typed wrong number! Enter menu choice: ")
    else:
        phonebook_name = files[phonebook_choice-1]
        phonebook = open_phonebook(PATH_TO_PHONEBOOKS_FOLDER + phonebook_name)

        return phonebook, phonebook_name



