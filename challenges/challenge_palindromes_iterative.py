def is_palindrome_iterative(word):
    return True if len(word) > 0 and word == word[::-1] else False
