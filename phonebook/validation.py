# +380 - default input 96-123-40-50
def valid_phone_number(phone_number: str):
    phone_number = phone_number.split('-')  # ['96', '123', '40', '50']
    if len(phone_number) != 4:
        print("Not valid format!")
        return False

    format_of_elements = [2, 3, 2, 2]
    for index, digits in enumerate(phone_number):

        if not format_of_elements[index] == len(digits):
            print("Not valid format!")
            return False

        if not digits.isnumeric():
            print("Only digits can be in phone number!")
            return False

    return True


def valid_first_or_last_name(name: str):
    if len(name) > 50:
        print("Too many characters!")
        return False

    if not name.isalpha():
        print("Name must contains only alphabet letters!")
        return False

    return True


def valid_city_or_state(place_name: str):
    set_of_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- "

    if "  " in place_name:
        print("Too many spaces!")
        return False

    if len(place_name) > 50:
        print("Too many characters!")
        return False

    if (place_name[0] == "-") or (place_name[-1] == "-"):
        print("- can not be in the first place")
        return False

    for letter in place_name:
        if letter not in set_of_characters:
            print("Should only contain alphabet or -")
            return False

    return True


def correct_input(valid_func, prompt: str, hint=False):
    valid = False

    if hint:
        print(hint)

    while not valid:
        value = input(prompt)
        valid = valid_func(value)

    return value
