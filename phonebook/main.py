from CRUD import add_new_entry, open_phonebook, init_phonebook, update_contact_info, delete_phone_number
from menu import main_menu

PATH_TO_PHONEBOOKS_FOLDER = "phonebooks/"


if __name__ == "__main__":
    phonebook, phonebook_name = init_phonebook(PATH_TO_PHONEBOOKS_FOLDER)

    while True:
        main_menu(phonebook, phonebook_name)