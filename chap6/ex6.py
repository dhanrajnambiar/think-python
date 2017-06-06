def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(s):
    if len(s) == 1:
        return True
    if len(s) == 2:
        if first(s) == last(s):
            return True
        else:
            return False
    if len(s) >= 2:
        if first(s) == last(s):
            x = is_palindrome(middle(s))
            return x
        else:
            return False

a = input('enter the word\n')
print(is_palindrome(a))
