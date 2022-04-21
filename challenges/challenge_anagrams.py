def is_anagram(first_string, second_string):
    first_word = convert_word_to_numbers(first_string.lower())
    second_word = convert_word_to_numbers(second_string.lower())
    if sort_list(first_word) == sort_list(second_word):
        return True
    else:
        return False


def convert_word_to_numbers(string):
    numbers = []
    for letter in string:
        number = ord(letter) - 96
        numbers.append(number)
    return numbers


def sort_list(number_list):
    new_list = []
    while(len(number_list) > 0):
        little_element = min(number_list)
        new_list.append(little_element)
        number_list.remove(little_element)
    return new_list
