def is_palindrome_iterative(word):
    if word == "":
        return False
    reverse_list = []
    for letter in word:
        reverse_list.insert(0, letter)
    reverse_word = "".join(reverse_list)
    return True if word == reverse_word else False
