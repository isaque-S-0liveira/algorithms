def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    reverse_str = "".join(reversed(word))
    if word == reverse_str:
        return True
    else:
        return False
