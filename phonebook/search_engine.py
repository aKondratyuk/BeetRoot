import json


def search_by(key: str, searching_for: str, phonebook: dict):
    search_result = []

    if key == "phone_number":
        if phonebook.get(searching_for):
            search_result.append(searching_for)
        return search_result

    for phone_number in phonebook.keys():
        if key in ["state", "city"]:
            if phonebook[phone_number]["address"][key] == searching_for:
                search_result.append(phone_number)

        if phonebook[phone_number][key] == searching_for:
            search_result.append(phone_number)

    return search_result


def print_search_result(search_result: dict):
    print(json.dumps(search_result, indent=4))
