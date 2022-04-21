def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    elif word[high_index] != word[low_index]:
        return False
    elif high_index <= low_index:
        return True
    return is_palindrome_recursive(word, low_index+1, high_index-1)
