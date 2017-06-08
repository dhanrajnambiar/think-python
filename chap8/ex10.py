def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False
a = input('enter a word\n')
print(is_palindrome(a))
